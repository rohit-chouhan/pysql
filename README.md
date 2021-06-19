[](https://luciopaiva.com/markdown-toc/)
![PySQL Framework](https://i.ibb.co/3FmsWch/mWQTLXjU.gif)

PySQL is database framework for Python (v3.x) Language, Which is based on Python module mysql.connector, this module can help you to make your code more short and more easier. Before using this framework you must have knowledge about list, tuple, set, dictionary because all codes are designed using it. It's totally free and open source.

## Installation
Before we said that this framework is based on mysql.connector so you have to install mysql.connector first on your system. Then you can import pysql and enjoy coding!
> python -m pip install mysql-connector-python


After Install mysql.connector successfully create Python file download/install pysql on the same dir where you want to create program. You can clone is using git or npm command, and you can also downlaod manually from repository site.

#### Git Command
```sh
git clone https://github.com/rohit-chouhan/pysql
```
#### Npm Command
Go to [https://www.npmjs.com/package/pysql](https://www.npmjs.com/package/pysql) or use command
```sh
$ npm i pysql
```
## Table of contents

- [Table of contents](#table-of-contents)
  - [Connecting a Server](#connecting-a-server)
  - [Create a Database in Server](#create-a-database-in-server)
  - [Connecting a Database](#connecting-a-database)
  - [Creating Table in Database](#creating-table-in-database)
  - [Selecting data from Table](#selecting-data-from-table)
  - [Add New Column to Table](#add-new-column-to-table)
  - [Modify Column to Table](#modify-column-to-table)
  - [Drop Column from Table](#drop-column-from-table)
  - [Manual Execute Query](#manual-execute-query)
  - [Inserting data](#inserting-data)
  - [Updating data](#updating-data)
  - [Deleting data](#deleting-data)


### Connecting a Server
------------
To connect a database with localhost server or phpmyadmin, use connect method to establish your python with database server.

```python
import pysql

db = pysql.connectServer(
	"host",
	"username",
	"password"
 )
```
### Create a Database in Server
------------
Creating database in server, to use this method

```python
import pysql

db = pysql.connectServer(
	"host",
	"username",
	"password"
 )
 pysql.createDb(db,"demo")
 #execute: CREATE DATABASE demo
```
### Connecting a Database
------------
To connect a database with localhost server or phpmyadmin, use connect method to establish your python with database server.

```python
import pysql

db = pysql.connect(
	"host",
	"username",
	"password",
	"database"
 )
```
### Creating Table in Database
------------
To create table in database use this method to pass column name as key and data type as value.
##### Syntex Code -
```python

pysql.createTable([db,"table_name_to_create"],{
    "column_name":"data_type", 
    "column_name":"data_type"
})
```
##### Example Code -
```python

pysql.createTable([db,"details"],{
    "id":"int(11) primary", 
     "name":"text", 
    "email":"varchar(50)",
    "address":"varchar(500)"
})
```
##### 2nd Example Code -
Use can use any Constraint with Data Value
```python

pysql.createTable([db,"details"],{
    "id":"int NOT NULL PRIMARY KEY", 
     "name":"varchar(20) NOT NULL", 
    "email":"varchar(50)",
    "address":"varchar(500)"
})
```
### Selecting data from Table
------------
For Select data from table, you have to mention the connector object with table name. pass column names in set.
##### Syntex `For All Data (*)`-
```python
records = pysql.selectAll([db,"table_name"])
for x in records:
  print(x)
```
##### Example - -
```python
records = pysql.selectAll([db,"details"])
for x in records:
  print(x)
#execute: SELECT * FROM details
```
##### Syntex `For Specific Column`-
```python
records = pysql.select([db,"table_name"],{"column","column"})
for x in records:
  print(x)
```
##### Example - -
```python
records = pysql.select([db,"details"],{"name","email"})
for x in records:
  print(x)
#execute: SELECT name, email FROM details
```

##### Syntex `With Where`-
```python
records = pysql.selectWhere([db,"table_name"],{"column","column"},("column","data"))
for x in records:
  print(x)
```
##### Example - -
```python
records = pysql.selectWhere([db,"details"],{"name","email"},("county","india"))
for x in records:
  print(x)
#execute: SELECT name, email FROM details WHERE country='india'
```
### Add New Column to Table
------------
To add column in table, use this method to pass column name as key and data type as value.
Note: you can only add one column only one call
##### Syntex Code -
```python

pysql.addColumn([db,"table_name"],{
    "column_name":"data_type"
})
```
##### Example Code -
```python

pysql.addColumn([db,"details"],{
    "email":"varchar(50)"
})
#execute: ALTER TABLE details ADD email varchar(50);
```
### Modify Column to Table
------------
To modify data type of column table, use this method to pass column name as key and data type as value.
##### Syntex Code -
```python
pysql.modifyColumn([db,"table_name"],{
    "column_name":"new_data_type"
})
```
##### Example Code -
```python
pysql.modifyColumn([db,"details"],{
    "email":"text"
})
#execute: ALTER TABLE details MODIFY COLUMN email text;
```
### Drop Column from Table
------------
Note: you can only add one column only one call
##### Syntex Code -
```python
pysql.dropColumn([db,"table_name"],"column_name")
```
##### Example Code -
```python
pysql.dropColumn([db,"details"],"name")
#execute: ALTER TABLE details DROP COLUMN name
```
### Manual Execute Query
------------
To execute manual SQL Query to use this method.
##### Syntex Code -
```python
pysql.query(connector_object,your_query)
```
##### Example Code -
```python
pysql.query(db,"INSERT INTO users (name) VALUES ('Rohit')")
```

### Inserting data
------------
For Inserting data in database, you have to mention the connector object with table name, and data as sets.
##### Syntex -
```python
data = 	{
	"db_column":"Data for Insert",
	"db_column":"Data for Insert"
}
pysql.insert([db,"table_name"],data)
```
##### Example Code -
```python
data = 	{
	"name":"Komal Sharma",
	"contry":"India"
}
pysql.insert([db,"users"],data)
```

### Updating data
------------
For Update data in database, you have to mention the connector object with table name, and data as tuple.
##### Syntex `For Updating All Data`-
```python
data = ("column","data to update")
pysql.updateAll([db,"users"],data)
```
##### Example - -
```python
data = ("name","Rohit")
pysql.updateAll([db,"users"],data)
#execute: UPDATE users SET name='Rohit'
```
##### Syntex `For Updating Data (Where)`-
```python
data = ("column","data to update")
where = ("column","data")
pysql.update([db,"users"],data,where)
```
##### Example - 
```python
data = ("name","Rohit")
where = ("id",1)
pysql.update([db,"users"],data,where)
#execute: UPDATE users SET name='Rohit' WHERE id=1
```
### Deleting data
------------
For Delete data in database, you have to mention the connector object with table name.
##### Syntex `For Delete All Data`-
```python
pysql.deleteAll([db,"table_name"])
```
##### Example - -
```python
pysql.deleteAll([db,"users"])
#execute: DELETE FROM users
```
##### Syntex `For Deleting Data (Where)`-
```python
where = ("column","data")
pysql.delete([db,"table_name"],where)
```
##### Example - 
```python
where = ("id",1)
pysql.delete([db,"users"],where)
#execute: DELETE FROM users WHERE id=1
```
## --- Finish ---
#### Change Logs
```sh
 - ConnectSever() removed and merged to Connect() method (July 19, 21)
```

The module is designed by [Rohit Chouhan](https://www.linkedin.com/in/itsrohitchouhan/), contact us for any bug report, feature or business inquiry.
