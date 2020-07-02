## 题目来源
(1) 题目1来源[链接](https://zhuanlan.zhihu.com/p/95578670)
(2) 题目2来源[]()

## 题目1
```sql
CREATE table Student(
    SId varchar(10),
    Sname varchar(10),
    Sage datetime,
    Ssex varchar(10)
);

insert into Student values('01' , '赵雷' , '1990-01-01' , '男');
insert into Student values('02' , '钱电' , '1990-12-21' , '男');
insert into Student values('03' , '孙风' , '1990-12-20' , '男');
insert into Student values('04' , '李云' , '1990-12-06' , '男');
insert into Student values('05' , '周梅' , '1991-12-01' , '女');
insert into Student values('06' , '吴兰' , '1992-01-01' , '女');
insert into Student values('07' , '郑竹' , '1989-01-01' , '女');
insert into Student values('09' , '张三' , '2017-12-20' , '女');
insert into Student values('10' , '李四' , '2017-12-25' , '女');
insert into Student values('11' , '李四' , '2012-06-06' , '女');
insert into Student values('12' , '赵六' , '2013-06-13' , '女');
insert into Student values('13' , '孙七' , '2014-06-01' , '女');


create table Course(
    CId varchar(10),
    Cname nvarchar(10),
    TId varchar(10)
);

insert into Course values('01' , '语文' , '02');
insert into Course values('02' , '数学' , '01');
insert into Course values('03' , '英语' , '03');



create table Teacher(
    TId varchar(10),
    Tname varchar(10)
);

insert into Teacher values('01' , '张三');
insert into Teacher values('02' , '李四');
insert into Teacher values('03' , '王五');


create table SC(
    SId varchar(10),
    CId varchar(10),
    score decimal(18,1)
);

insert into SC values('01' , '01' , 80);
insert into SC values('01' , '02' , 90);
insert into SC values('01' , '03' , 99);
insert into SC values('02' , '01' , 70);
insert into SC values('02' , '02' , 60);
insert into SC values('02' , '03' , 80);
insert into SC values('03' , '01' , 80);
insert into SC values('03' , '02' , 80);
insert into SC values('03' , '03' , 80);
insert into SC values('04' , '01' , 50);
insert into SC values('04' , '02' , 30);
insert into SC values('04' , '03' , 20);
insert into SC values('05' , '01' , 76);
insert into SC values('05' , '02' , 87);
insert into SC values('06' , '01' , 31);
insert into SC values('06' , '03' , 34);
insert into SC values('07' , '02' , 89);
insert into SC values('07' , '03' , 98);

数据库数据如下：
Student表:
+------+--------+---------------------+------+
| SId  | Sname  | Sage                | Ssex |
+------+--------+---------------------+------+
| 01   | 赵雷   | 1990-01-01 00:00:00 | 男   |
| 02   | 钱电   | 1990-12-21 00:00:00 | 男   |
| 03   | 孙风   | 1990-12-20 00:00:00 | 男   |
| 04   | 李云   | 1990-12-06 00:00:00 | 男   |
| 05   | 周梅   | 1991-12-01 00:00:00 | 女   |
| 06   | 吴兰   | 1992-01-01 00:00:00 | 女   |
| 07   | 郑竹   | 1989-01-01 00:00:00 | 女   |
| 09   | 张三   | 2017-12-20 00:00:00 | 女   |
| 10   | 李四   | 2017-12-25 00:00:00 | 女   |
| 11   | 李四   | 2012-06-06 00:00:00 | 女   |
| 12   | 赵六   | 2013-06-13 00:00:00 | 女   |
| 13   | 孙七   | 2014-06-01 00:00:00 | 女   |
+------+--------+---------------------+------+

Course表：
+------+--------+------+
| CId  | Cname  | TId  |
+------+--------+------+
| 01   | 语文   | 02   |
| 02   | 数学   | 01   |
| 03   | 英语   | 03   |
+------+--------+------+

Teacher表:
+------+--------+
| TId  | Tname  |
+------+--------+
| 01   | 张三   |
| 02   | 李四   |
| 03   | 王五   |
+------+--------+

SC表:
+------+------+-------+
| SId  | CId  | score |
+------+------+-------+
| 01   | 01   |  80.0 |
| 01   | 02   |  90.0 |
| 01   | 03   |  99.0 |
| 02   | 01   |  70.0 |
| 02   | 02   |  60.0 |
| 02   | 03   |  80.0 |
| 03   | 01   |  80.0 |
| 03   | 02   |  80.0 |
| 03   | 03   |  80.0 |
| 04   | 01   |  50.0 |
| 04   | 02   |  30.0 |
| 04   | 03   |  20.0 |
| 05   | 01   |  76.0 |
| 05   | 02   |  87.0 |
| 06   | 01   |  31.0 |
| 06   | 03   |  34.0 |
| 07   | 02   |  89.0 |
| 07   | 03   |  98.0 |
+------+------+-------+
```
(1.1)查询"01"课程比"02"课程成绩高的学生的信息及课程分数
```sql

select Sname, Sage, Ssex, t.score1, t.score2 
    from 
        (select t1.SId as SId, t1.score as score1, t2.score as score2
            from 
                (select SId, score from SC where CId='01') as t1, 
                (select SId, score from SC where CId='02') as t2
            where 
                t1.SId=t2.SId and t1.score > t2.score
        ) as t, Student
    where t.SId = Student.SId;

```

(1.2)查询同时存在"01"课程和"02"课程的情况
```sql
select Sname, Sage, Ssex 
    from Student 
    where SId in (
        select t1.SId from 
        (select SId from SC where CId='01') as t1,
        (select SId from SC where CId='02') as t2
        where t1.SId = t2.SId
    );
```

(1.3)查询存在"01"课程但可能不存在"02"课程的情况(不存在时显示为 null )
```sql
select t1.SId, t1.CId, t2.CId 
    from 
        (select SId, CId from SC where CId='01') as t1
        left join
        (select SId, CId from SC where CId='02') as t2
    on 
        t1.SId = t2.SId;
```


(1.4)查询不存在"01"课程但存在"02"课程的情况
```sql
select t2.SId, t1.CId, t2.CId
    from 
        (select SId, CId from SC where CId='01') as t1
        right join
        (select SId, CId from SC where CId='02') as t2
    on 
        t1.SId = t2.SId;
```

(1.5)查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
```sql
select t.SId, Student.Sname, t.average 
    from
        (select SId, avg(score) as average from SC group by SId) as t
        join
        Student
    on
        t.SId=Student.SId and t.average>=60;
```

(1.6)查询在SC表存在成绩的学生信息
```sql
select * 
    from Student
    where
        Student.SId in (select distinct SId from SC); 
```

(1.7)查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩(没成绩的显示为 null )
```sql
select Student.SId, Student.Sname, t.tot, t.cnt 
    from 
        Student
        left join
        (select SId, sum(score) as cnt, count(*) as tot from SC group by SId) as t
    on
        Student.SId=t.SId;
```

(1.8)查有成绩的学生信息
```sql
select * 
    from
        Student
    where 
        Student.SId in  (select distinct SId from SC);
```

(1.9)查询「李」姓老师的数量
```sql
select count(*) from Teacher where Tname like '李%';
```

(1.10)查询学过「张三」老师授课的同学的信息
```sql
select * 
    from Student
    where Student.SId in (
        select SId 
            from SC 
            where SC.CId in(
                select CId 
                    from Course
                    where Course.TId in (select TId from Teacher where Tname='张三')
            ) 
    );
```

(1.11)查询没有学全所有课程的同学的信息

(1.12)查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息

(1.13)查询没学过"张三"老师讲授的任一门课程的学生姓名

(1.14)查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩

(1.15)按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩(avg聚合函数想要多行输出，子查询)

(1.16)查询各科成绩最高分、最低分和平均分:

以如下形式显示:课程 ID，课程 name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率

及格为>=60，中等为:70-80，优良为:80-90，优秀为:>=90

要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列

(1.17) 按各科成绩进行排序，并显示排名， Score 重复时保留名次空缺

(1.18) 按各科成绩进行排序，并显示排名， Score 重复时合并名次

(1.19) 查询学生的总成绩，并进行排名，总分重复时保留名次空缺

(1.20)  查询学生的总成绩，并进行排名，总分重复时不保留名次空缺

(1.21) 