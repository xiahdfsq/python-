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
			self.conn = MySQLdb.connect(
				host='localhost',
				user='root',
				passwd='',
				db='news',
				port=3306,
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
		sql = 'SELECT * FROM news WHERE types = %s ORDER BY id DESC;'
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
		sql = 'SELECT * FROM news WHERE types = %s ORDER BY id DESC LIMIT %S, %s;'
		#找到cursor
		cursor = self.conn.cursor()
		#执行SQL 元组
		cursor.execute(sql, ('百家', offset, page_size))
		#print(dir(cursor))
		#print(cursor.description)
		#拿到结果 
		#rest = cursor.fetchone()
		rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
		
		#处理数据
		#关闭cursor/连接
		cursor.close()
		self.close_conn()
		return rest

	def add_one(self):
		try:
			#准备SQL
			sql = (
				"INSERT INTO news (title,content,types,isValid) VALUES"
				"(%s,%s,%s,1);"
			) 
			#获取连接和cursor
			cursor = self.conn.cursor()
			#执行SQL
			#提交数据到数据库
			cursor.execute(sql, ('标题1','新闻内容', '推举',1))
			
			#提交事务
			self.conn.commit()
			cursor.close()
			self.close_conn()
			#关闭cursor/连接
		except:
			print('erro')
			#当发生错误的时候 正确的再次提交
			self.conn.commit()
			#当发生错误的时候 全部回滚
			self.conn.rollback()

def main():
	obj = MysqlSearch()
	# rest = obj.get_one()
	# print(rest)
	# print(rest['title'])
	# rest = obj.get_more()
	# for item in rest:
	# 	print(item)
	# 	print('-----')
	obj.add_one()


if __name__ == '__main__':
	main()





