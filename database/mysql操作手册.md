## 登录
```shell script
> mysql -u root -p
> password
```

## 创建数据库
```shell sql
mysql> create database db_name;
```

## 删除数据库
```sql
mysql> drop database db_name;
```

## 选中数据库
```sql
mysql> use db_name;
```

## mysql数据类型
https://www.runoob.com/mysql/mysql-data-types.html  

数值类型: `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `BIGINT`, `FLOAT`, `DOUBLE`, `DECIMAL`  

日期和时间类型: `DATE`, `TIME`, `YEAR`, `DATETIME`, `TIMESTAMP`  

字符串类型: `CHAR`, `VARCHAR`, `TINYBLOB`, `TINYTEXT`, `BLOB`, `TEXT`, `MEDIUMBLOB`, `MEDIUMTEXT`, `LONGBLOB`, `LONGTEXT`  

## 创建数据表
```sql
create table tb_name (column_name column_type, );
```
一个例子:
```sql
create table user(
    uid INT AUTO_INCREMENT,
    username VARCHAR(128) NOT NULL,
    register_time DATETIME,
    sex VARCHAR(8),
    PRIMARY KEY(uid)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## 查看数据表的字段定义
```sql
show columns from tb_name;
```

## 删除数据表
```sql
drop table tb_name;
```

## 插入数据到表中
```sql
insert into tb_name (field_1, field_2, field_3, ..., field_n) 
values (value_1, value_2, value_3, ..., value_n);
```
继续使用上面的那个user表
```sql
insert into user (username, register_time, sex) values 
('小红', NOW(), 'female'), 
('小明', NOW(), 'male'), 
('小兵', NOW(), 'male'); 
```

## 查询数据
```sql
select column_name_1, column_name_2 
from tb_name 
[where clause] [limit n] [offset m]; 
```
继续使用上面的user表  
例子1  
```sql
select * from user;
```
输出:
```plain text
+-----+----------+---------------------+--------+
| uid | username | register_time       | sex    |
+-----+----------+---------------------+--------+
|   1 | 小红     | 2020-05-25 05:07:19 | female |
|   2 | 小明     | 2020-05-25 05:07:19 | male   |
|   3 | 小兵     | 2020-05-25 05:07:19 | male   |
+-----+----------+---------------------+--------+
```
例子2
```sql
select username, register_time 
from user 
where sex='male' 
limit 2 
offset 1;
```
输出:
```plain text
+----------+---------------------+
| username | register_time       |
+----------+---------------------+
| 小兵     | 2020-05-25 05:07:19 |
+----------+---------------------+
```

## where子语句
```sql
select field_1, field_2, ... field_n
from tb_name_1, tb_name_2
where conditon_1 [AND [OR]] condition_2
```
例子
```
select username, sex 
from user
where username='小明' or sex='male';
```
MySQL 的 WHERE 子句的字符串比较是不区分大小写的。 你可以使用 BINARY 关键字来设定 WHERE 子句的字符串比较是区分大小写的。

## update(更新语句)
```sql
update tb_name 
set field_1=new_data1, field_2=new_data2
where clause
```
例子1
```sql
update user
set sex='femail'
where username='小明';
```

## delete 语句
```sql
delete from tb_name where clause;
```

## like 子句
```sql
select field_1, field_2, ..., field_n
from tb_name
where field_1 LIKE condition_1 [AND [OR]] field_2='new_value'
```
例子1
```sql
select username, sex
from user
where username like '小%' and sex='male';
```

## union 
将两个表查询的结果合并出来
```sql
select exp_1, exp_2, ..., exp_n
from tb_name
where condition
union [all [distinct]]
select exp_1, exp_2, ..., exp_n
from tb_name
where condition;
```

## order by(排序)
```sql
select field_1, field_2, ..., field_n
from tb_name
order by field_1 [asc(默认) [desc]], field_2 [asc(默认) [desc]]
```
例子1
```sql
select username
from user
order by username desc;
```

## group by (分组)
```sql
select column_name, function(column_name)
from tb_name
where column_name operator value
group by column_name;
```
先插入测试用例
```sql
insert into user 
(username, register_time, sex) values ('小明', NOW(), 'male');
```
例子
```sql
select username, COUNT(*) from user group by username;
```

## join (连接)
inner join(内连接), left join(左连接)，right(右连接)
```sql
select field_1, field_2 
from table_1 join table_2 
on table_1.field_1 = table_2.field_2;
```

## NULL值处理
关于 NULL 的条件比较运算是比较特殊的。你不能使用 = NULL 或 != NULL 在列中查找 NULL 值 。

在 MySQL 中，NULL 值与任何其它值的比较（即使是 NULL）永远返回 NULL，即 NULL = NULL 返回 NULL 。

<=>: 比较操作符（不同于 = 运算符），当比较的的两个值相等或者都为 NULL 时返回 true。

## 正则表达式
```sql
select field from table where field regexp 'reg_expression' 
```

## 事务
- 在`MySQL`中只有使用了`Innodb`数据库引擎的数据库或表才支持事务。
- 事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。

 一般来说，事务是必须满足4个条件（ACID）：：原子性（Atomicity，或称不可分割性）、一致性（Consistency）、隔离性（Isolation，又称独立性）、持久性（Durability）。

    原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

    一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

    隔离性：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

    持久性：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

    在 MySQL 命令行的默认设置下，事务都是自动提交的，即执行 SQL 语句后就会马上执行 COMMIT 操作。因此要显式地开启一个事务务须使用命令 BEGIN 或 START TRANSACTION，或者执行命令 SET AUTOCOMMIT=0，用来禁止使用当前会话的自动提交。


事务控制语句：

    BEGIN 或 START TRANSACTION 显式地开启一个事务；

    COMMIT 也可以使用 COMMIT WORK，不过二者是等价的。COMMIT 会提交事务，并使已对数据库进行的所有修改成为永久性的；

    ROLLBACK 也可以使用 ROLLBACK WORK，不过二者是等价的。回滚会结束用户的事务，并撤销正在进行的所有未提交的修改；

    SAVEPOINT identifier，SAVEPOINT 允许在事务中创建一个保存点，一个事务中可以有多个 SAVEPOINT；

    RELEASE SAVEPOINT identifier 删除一个事务的保存点，当没有指定的保存点时，执行该语句会抛出一个异常；

    ROLLBACK TO identifier 把事务回滚到标记点；

    SET TRANSACTION 用来设置事务的隔离级别。InnoDB 存储引擎提供事务的隔离级别有READ UNCOMMITTED、READ COMMITTED、REPEATABLE READ 和 SERIALIZABLE。

MYSQL 事务处理主要有两种方法：

1、用 BEGIN, ROLLBACK, COMMIT来实现

    BEGIN 开始一个事务
    ROLLBACK 事务回滚
    COMMIT 事务确认

2、直接用 SET 来改变 MySQL 的自动提交模式:

    SET AUTOCOMMIT=0 禁止自动提交
    SET AUTOCOMMIT=1 开启自动提交


## alter
例子1 删除某个字段
```sql
alter table user drop register_time;
```
例子2 添加一个字段
```sql
alert table user add country varchar(64);
```

例子3 修改字段类型和名称
```sql
alter table user change country address varchar(32);
```

例子4 删除默认

例子5 修改表名
```sql
alter table user rename to usr;
```

例子6 修改存储引擎
```sql
alter table user engine=myisam;
```

## 索引
例子1 创建普通索引
```sql
create index username_idx on user(username);
```

例子2 用alter修改表结构
```sql
alter table user add index username_idx(username);
```

例子3 创建表时直接指定
```sql
create table user2(
    uid INT NOT NULL AUTO_INCREMENT,
    username varchar(64) NOT NULL,
    PRIMARY KEY(uid),
    INDEX username_index (username)
)engine=innodb default charset=utf8;
```
例子4 删除索引
```sql
drop index index_name on tb_name;
```

例子5 唯一索引

例子6 显示索引信息
```sql
show index from tb_name;
```

## 临时表
MySQL 临时表在我们需要保存一些临时数据时是非常有用的。临时表只在当前连接可见，当关闭连接时，Mysql会自动删除表并释放所有空间。
```sql
create temporary table tb_name(

);
```

## 复制表
1. show create table tb_name;
2. 更改1得到的建表语句中的表名，建立复制表
3. insert into copy_table ... select

## 元数据
例子1 获取查询语句影响的记录数
- `SELECT VERSION( )`	服务器版本信息
- `SELECT DATABASE( )`	当前数据库名 (或者返回空)
- `SELECT USER( )`	当前用户名
- `SHOW STATUS`	服务器状态
- `SHOW VARIABLES`	服务器配置变量

## mysql 序列
一张表只能有一个字段为自增主键，其他字段想实现自增可以使用`AUTO_INCREMENT`实现  

例子1 设置序列的开始值为2
```sql
alter table tb_name AUTO_INCREMENT = 2;
```

## mysql处理重复数据
使用primary key 或者 unique 

## 导出数据
- 方法1, `select ... into outfile filename`
- 方法2, 使用mysqldump

例子1 导出为csv格式
```sql
select * from tb_name
field terminated by ',' enclosed by '"'
lines terminated by '\r\n';
```



## 导入数据
- 方法1 `mysql -uuser -ppassword < data.sql;`
- 方法2 在mysql shell里执行`source data.sql;`
- 方法3 在mysql shell里使用`load data local infile filename into table tb_name;`
- 方法4 使用mysqlimport

## mysql函数
https://www.runoob.com/mysql/mysql-functions.html

## mysql运算符
https://www.runoob.com/mysql/mysql-operator.html