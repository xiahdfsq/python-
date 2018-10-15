python---解释型语言，可以运用在大数据，爬虫，AI，web等；缺点比java，C++慢

第三章
进制间的转换
2进制（0-1） --0b10  -2   bin(10         /0o12/0xA)
8进制（0-7） --0o7   -7   oct(20/0b10100      /0x14)
16进制（0-F）--0xF   -15  hex(30/0b11110/0o36)
ascll:   ord('a'); chr(66); 
		'abc'.encode('ascii',errors='ignore'); '中文'.encode('utf-8',errors='ignore');
		b'abc'.decode('ascii',errors='ignore'); b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore')

基本数据类型
整数 int 
浮点数 float  1.0 not= 1 
字符串 str   len('abc'),'abc'.[0],'abc'.[-1:]=='abc'[-1],Max('abc'),min('abc');'abc'.replace('a','A')
布尔值 bool  True/False-- [],{},'',None,0

其他数据类型或操作
list_var = [1,5,6]
dict_var = {'name': 'cindy'}
list  列表：len(list_var);list_var[0];list_var[-1];list_var.append('a');list_var.insert(1,5);
			list_var.pop();list_var.pop(i);max(list_var);min(list_var); 5 in list_var 3 not in list_var;
tuple 元组：(1,5,6) 不可改变，可读取，不可修改
dict  字典：dict_var['name']; 'name' in dict_var; dict_var.get('name','none');dict_var.pop('name')
set   集合: {1,2,3} in,len,min,max,&,|;{1,2,3}.add(4);{1,2,3}.remove(3);set([1,2,3])

变量
以字母，数字，下划线组成，不以数字开头，建议用下划线分割2个字母，不用驼峰法或者中划线

赋值运算： =,+=,-=,/=.%=
算术运算： //取整，**，%
关系运算： ==，!=, <,>,<=,>=
逻辑运算： and,or,not
成员运算： in , not in
身份运算： is, is not, 功能类似 ==
位运算：   &,|,~取反,^,>>, <<
类型运算： type();isinstance(a, int);isinstance(a,(int,str))

第六章  循环
for x in range(101):
	pass
while x:
	pass

break 可提前跳出本次逻辑循环语句
continue 跳出当次循环进入下一次循环