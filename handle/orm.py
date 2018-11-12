# pip install sqlalchemy
# python命令环境下,如果有版本则为成功
# import sqlalchemy
# sqlalchemy.__version__

from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine('mysql://root:chindy2141@localhost:3306/news_test?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class News(Base):
	__tablename__ = 'news'
	id = Column(Integer, primary_key = True)
	title = Column(String(200), nullable = False)
	content = Column(String(2000), nullable = False)
	types = Column(String(10), nullable = False)
	image = Column(String(300))
	autoor= Column(String(20))
	view_count= Column(Integer)
	create_at= Column(DateTime)
	is_valid = Column(Boolean)

#python命令环境下,如果有版本则为成功生成数据库表
#from orm import News
#from orm import engine
#News.metadata.create_all(engine)



class OrmTest(object):
	"""docstring for OrmTest"""
	def __init__(self, arg):
		self.session = Session()

	def add_one(self):
		new_obj = News(
			title = '题目1',
			content = '内容1',
			types = '国际',
		)
		# self.session.all([
		# 	News(title = '题目1',content = '内容1',types = '国际'),
		# 	News(title = '题目2',content = '内容2',types = '财经')]) 
		self.session.add(new_obj)
		self.session.commit()
		return new_obj
	def get_one(self):
		'''查询一条数据'''
		#get是取第几条
		return self.session.query(News).get(1)
	def get_more(self):
		'''查询多条数据'''
		return self.session.query(News).filter_by(is_valid =  True)

	def update_date(self, pk):
		'''修改多条数据'''
		arr = self.session.query(News).filter_by(is_valid =  True)
		for item in arr:
			item.is_valid = 0
			self.session.add(item)
		self.session.commit()
		'''修改1条数据'''
		#obj = self.session.query(News).get(pk)
		# if obj:			
		# 	obj.is_valid = 0
		# 	self.session.add(obj)
		# 	self.session.commit()
		# 	return True
		# else:
		# 	return False
	def delete_date(self, pk):
		'''删除多条数据'''
		obj = self.session.query(News).get(pk)
		self.session.delete()
		self.session.commit(obj)

def main()
	obj = OrmTest()
	#rest = obj.add_one()
	#print(rest.id)


	# rest = obj.get_one()
	# if rest:
	# 	print('ID:{0}=> {1}'.format(rest.id, rest.title))
	# else: 
	# 	print('Not exist')

	# rest = obj.get_more()
	# print(rest.count())
	# for new_obj in rest:
	# 	print('ID:{0}=> {1}'.format(new_obj.id, new_obj.title))

	#print(obj.update_date(2))
	print(obj.delete_date(3)) 
if __name__ == '__main__':
	main()

#python命令环境下,
#python orm.py