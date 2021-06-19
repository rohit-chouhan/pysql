_C='ALTER TABLE '
_B='SELECT {} FROM {}'
_A=','
import mysql.connector
def table(x):global table;table=str(x)
def connect(*A):
	if len(A)==3:B=mysql.connector.connect(host=A[0],user=A[1],password=A[2])
	else:B=mysql.connector.connect(host=A[0],user=A[1],password=A[2],database=A[3])
	return B
def query(x,y):A=x.cursor();A.execute(y);x.commit()
def createDb(x,y):A=x.cursor();A.execute('CREATE DATABASE '+y+'');x.commit()
def select(x,y):
	B=[]
	for D in y:B.append(D)
	E=_A.join(B);C=x[0].cursor();A=_B;A=A.format(E,x[1]);C.execute(A);return C.fetchall()
def selectAll(x):B=x[0].cursor();A=_B;A=A.format('*',x[1]);B.execute(A);return B.fetchall()
def selectWhere(x,y,z):
	B=[]
	for D in y:B.append(D)
	E=_A.join(B);C=x[0].cursor()
	if type(z[1])==str:A="SELECT {} FROM {} WHERE {}='{}'"
	else:A='SELECT {} FROM {} WHERE {}={}'
	A=A.format(E,x[1],z[0],z[1]);C.execute(A);return C.fetchall()
def dropTable(x):A=x[0].cursor();B='DROP TABLE {}';A.execute(B.format(x[1]));x[0].commit()
def dropDb(x):A=x[0].cursor();B='DROP DATABASE {}';A.execute(B.format(x[1]));x[0].commit()
def createTable(db,data):
	A=[]
	for B in data:A.append(B+' '+data[B])
	C=_A.join(A);D='CREATE TABLE '+db[1]+' ({})';E=D.format(C);F=db[0].cursor();F.execute(E);db[0].commit()
def addColumn(db,data):
	A=[]
	for B in data:A.append(B);A.append(data[B])
	C=_C+db[1]+' ADD {} {}';D=C.format(A[0],A[1]);E=db[0].cursor();E.execute(D);db[0].commit()
def modifyColumn(db,data):
	A=[]
	for B in data:A.append(B);A.append(data[B])
	C=_C+db[1]+' MODIFY {} {}';D=C.format(A[0],A[1]);E=db[0].cursor();E.execute(D);db[0].commit()
def dropColumn(db,data):A='ALTER TABLE {} DROP COLUMN {}';A=A.format(db[1],data);B=db[0].cursor();B.execute(A);db[0].commit()
def insert(db,data):
	J='"';A=[];B=[];C=[]
	for D in data:A.append(D);B.append(str(J+data[D]+J));C.append(str('%s'))
	E=_A.join(A);F=_A.join(B);K=_A.join(C);G='INSERT INTO '+db[1]+' ({}) VALUES ({})';H=G.format(E,F);I=db[0].cursor();I.execute(H);db[0].commit()
def updateAll(x,d):
	B=x[0].cursor()
	if type(d[1])==str:A="UPDATE {} SET {}='{}'"
	else:A='UPDATE {} SET {}={}'
	B.execute(A.format(x[1],d[0],d[1]));x[0].commit()
def update(x,d,c):
	B=x[0].cursor()
	if type(d[1])==str:
		if type(c[1])==str:A="UPDATE {} SET {}='{}' WHERE {}='{}'"
		else:A="UPDATE {} SET {}='{}' WHERE {}={}"
	elif type(c[1])==str:A="UPDATE {} SET {}={} WHERE {}='{}'"
	else:A='UPDATE {} SET {}={} WHERE {}={}'
	B.execute(A.format(x[1],d[0],d[1],c[0],c[1]));x[0].commit()
def delete(x,d):
	B=x[0].cursor()
	if type(d[1])==str:A="DELETE FROM {} WHERE {}='{}'"
	else:A='DELETE FROM {} WHERE {}={}'
	B.execute(A.format(x[1],d[0],d[1]));x[0].commit()
def deleteAll(x):A=x[0].cursor();B='DELETE FROM {}';A.execute(B.format(x[1]));x[0].commit()
