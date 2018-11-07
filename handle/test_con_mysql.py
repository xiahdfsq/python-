#pip install mysql-client
#http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
#实验python 是否可以连接上数据库
#python命令环境下 打印import MySQLdb
import MySQLdb

try:
	conn = MySQLdb.connet(
		host='127.0.0.1',
		user='root',
		passwd='',
		db='news',
		port=3308,
		charset='utf8'
	)
	#执行
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM 'news' ORDER BY 'created_at' DESC;')
	rest = cursor.fetchone()
	#cursor.fetchall()
	print(rest) 

	#关闭连接
	conn.close() 
except MySQLdb.Error as e:
	print('Error: %s' % e)

