### 登陆
```shell
mysql -u root -p
```

### 查看有什么数据库
```shell
show databases;
```

### 删除数据库
```shell
drop database database_name;
```

### 选中数据库
```
use database_name;
```

### 查看数据库里的表
```
show tables;
```

### 修改mysql8的密码
```shell
shell>mysql -u root -p
mysql>use mysql;
mysql>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_database_password';
```