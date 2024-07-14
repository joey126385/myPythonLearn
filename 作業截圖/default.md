## default

```sql
CREATE TABLE t1 (
	id int DEFAULT 110,
	name varchar(10)
);
```



方式一、沒有 insert into id

```sql
insert into t1(name) value("thenew"),("ameng");
```

```shell
mysql> insert into t1(name) value("thenew"),("ameng");
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from t1 ;
+------+--------+
| id   | name   |
+------+--------+
|  110 | thenew |
|  110 | ameng  |
+------+--------+
2 rows in set (0.00 sec)
```



方式二、有 insert into id 

```sql
insert into t1 value(1,'tongyao'),(55,'talent');
```

```shell
mysql> insert into t1 value(1,'tongyao'),(55,'talent');
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from t1;
+------+---------+
| id   | name    |
+------+---------+
|    1 | tongyao |
|   55 | talent  |
+------+---------+
2 rows in set (0.00 sec)
```



## not null

create table

```sql
CREATE TABLE t2 (
	id int NOT NULL,
	name varchar(20)
);
```

```sql
insert into t2(name) values("haha");
```

```shell
mysql> CREATE TABLE t2 (
    -> id int NOT NULL,
    -> name varchar(20)
    -> );
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    7
Current database: dba

Query OK, 0 rows affected (0.20 sec)

mysql> insert into t2(name) values("haha");
ERROR 1364 (HY000): Field 'id' doesn't have a default value
```



## unique key



create table 

```sql
CREATE TABLE t3 (
	id int UNIQUE,
	name varchar(20) NOT NULL
);
```

```sql
insert into t3 value(1,'xiaoming');
```

```shell
mysql> CREATE TABLE t3 (
    -> id int UNIQUE,
    -> name varchar(20) NOT NULL
    -> );
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    8
Current database: dba

Query OK, 0 rows affected (0.06 sec)

mysql> insert into t3 value(1,'xiaoming');
Query OK, 1 row affected (0.01 sec)

mysql> select * from t3
    -> ;
+------+----------+
| id   | name     |
+------+----------+
|    1 | xiaoming |
+------+----------+
1 row in set (0.00 sec)
```



```sql
insert into t3 value(1,'xiaoming');
```

```shell
mysql> insert into t3 value(1,'xiaoming');
ERROR 1062 (23000): Duplicate entry '1' for key 'id'
```





## primary key

```sql
CREATE TABLE t4 (
	id int PRIMARY KEY,
	name varchar(20) NOT NULL UNIQUE  key
);
```



```sql
insert into t4 values(1,'yy');
```







## one to one

```sql
CREATE TABLE chinese (
	id int PRIMARY KEY,
	name varchar(10)
);
```

```sql
INSERT INTO 
	chinese (id, name)
VALUES 
	(410410001, '张三'),
	(410410002, '李四'),
	(410410003, '王五'),
	(410410004, '宋六'),
	(410410005, '孙七')
;
```

```sql
CREATE TABLE chinese_msg (
	msg_id int PRIMARY KEY AUTO_INCREMENT,
	msg varchar(255),
	c_id int,
	FOREIGN KEY (c_id) REFERENCES chinese (id)
);
```

```sql
INSERT INTO 
	chinese_msg (msg, c_id)
VALUES 
	('湖南汉族喜欢吃臭豆腐', 410410001),
	('新疆维吾尔族喜欢吃哈密瓜', 410410002),
	('内蒙古汉族喜欢吃手把肉', 410410003),
	('西藏藏族喜欢喝青稞酒', 410410004);
```



