#pip install mysql-client
#http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
#实验python 是否可以连接上数据库
#python命令环境下 打印import MySQLdb
import MySQLdb

class MysqlSearch(object): 
	def __init__(self):
		self.get_conn()
	def get_conn(self):
		try:
			self.conn = MySQLdb.connet(
				host='127.0.0.1',
				user='root',
				passwd='',
				db='news',
				port=3308,
				charset='utf8'
			)
			 
 
		except MySQLdb.Error as e:
			print('Error: %s' % e) 	

	def close_conn(self):
		try:	
			if self.conn: 
				#关闭连接
				self.conn.close()
		except MySQLdb.Error as e:
			print('Error: %s' % e)
	def get_one(self):
		#准备SQL
		sql = 'SELECT * FROM 'news' WHERE 'types' = %s ORDER BY 'created_at' DESC;'
		#找到cursor
		cursor = self.conn.cursor()
		#执行SQL 元组
		cursor.execute(sql, ('百家',))
		#print(dir(cursor))
		#print(cursor.description)
		#拿到结果 
		#rest = cursor.fetchone()
		rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
		return rest
		#处理数据
		#关闭cursor/连接
		cursor.close()
		self.close_conn()

	def get_more(self, page, page_size):
		offset = (page-1)*page_size
		#准备SQL
		sql = 'SELECT * FROM 'news' WHERE 'types' = %s ORDER BY 'created_at' DESC LIMIT %S, %s;'
		#找到cursor
		cursor = self.conn.cursor()
		#执行SQL 元组
		cursor.execute(sql, ('百家',))
		#print(dir(cursor))
		#print(cursor.description)
		#拿到结果 
		#rest = cursor.fetchone()
		rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
		return rest
		#处理数据
		#关闭cursor/连接
		cursor.close()
		self.close_conn()

def main():
	obj = MysqlSearch()
	# rest = obj.get_one()
	# print(rest)
	# print(rest['title'])
	rest = obj.get_more()
	for item in rest:
		print(item)
		print('-----')


if __name__ == '__main__':
	main()





