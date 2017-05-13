'''
CREATE TABLE `university`.`department` (
  `dept_name` VARCHAR(45) NOT NULL,
  `building` VARCHAR(45) NULL,
  `budget` INT NULL,
  PRIMARY KEY (`dept_name`));
  
CREATE TABLE `university`.`student` (
  `ID` INT(10) NOT NULL,
  `name` VARCHAR(45) NULL,
  `sex` CHAR(1) NULL,
  `age` INT(3) NULL,
  `emotion_state` VARCHAR(45) NULL,
  `dept_name` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`));
  
CREATE TABLE `university`.`exam` (
  `student_ID` INT(10) NOT NULL,
  `exam_name` VARCHAR(45) NULL,
  `grade` INT(3) UNSIGNED NULL,
  PRIMARY KEY (`student_ID`));
  
  ALTER TABLE `university`.`exam` 
CHANGE COLUMN `exam_name` `exam_name` VARCHAR(45) NOT NULL ,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`student_ID`, `exam_name`);


ALTER TABLE `university`.`student` 
ADD INDEX `fk_student_1_idx` (`dept_name` ASC);
ALTER TABLE `university`.`student` 
ADD CONSTRAINT `fk_student_1`
  FOREIGN KEY (`dept_name`)
  REFERENCES `university`.`department` (`dept_name`)
  ON DELETE SET NULL
  ON UPDATE CASCADE;

ALTER TABLE `university`.`exam` 
ADD CONSTRAINT `fk_exam_1`
  FOREIGN KEY (`student_ID`)
  REFERENCES `university`.`student` (`ID`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
'''

# coding: utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':

    # 连接数据库
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='ZKY20132042',
        charset = "utf8",
        db='university',
    )

    # 获取数据库执行游标
    cur = conn.cursor()

    f = open("~/Downloads/MySQL上课文件/作业/university/department.txt", "r")
    while True:
        line = f.readline()
        if line:
            # 处理每行\n
            line = line.strip('\n')
            line = line.split(",")
            print(line)
            dept_name = line[0]
            building = line[1]
            budget = line[2]
            cur.execute(
                "insert into department(dept_name,building,budget) values(%s,%s,%s)",
                [dept_name, building, budget])
        else:
            break
    f.close()

    z = open("~/Downloads/MySQL上课文件/作业/university/student.txt", "r")
    while True:
        line = z.readline()
        if line:
            # 处理每行\n
            line = line.strip('\n')
            line = line.split(",")
            print(line)
            ID = line[0]
            name = line[1]
            sex = line[2]
            age = line[3]
            emotion_state = line[4]
            dept_name = line[5]
            cur.execute(
                "insert into department(ID,name,sex,age,emotion_state,dept_name) values(%s,%s,%s,%s,%s,%s)",
                [ID,name,sex,age,emotion_state,dept_name])
        else:
            break
    z.close()

    l = open("~/Downloads/MySQL上课文件/作业/university/exam.txt", "r")
    while True:
        line = l.readline()
        if line:
            # 处理每行\n
            line = line.strip('\n')
            line = line.split(",")
            print(line)
            student_ID = line[0]
            exam_name = line[1]
            grade = line[2]
            cur.execute(
                "insert into department(student_ID,exam_name,grade) values(%s,%s,%s)",
                [student_ID,exam_name,grade])
        else:
            break
    l.close()

    cur.close()
    conn.commit()
    conn.close()

#3-1.把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）写出MySQL语句。
'''
select * from peoples where school != 'GDUFS' and school is NULL;
'''

#3-2.查找计算机系每次考试学生的平均成绩(最终显示学生姓名, 考试名称, 平均分)。
'''
select name,exam_name,avg(grade) from student,exam where student.ID = exam.student_ID;
'''

#3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。
'''
select name,grade from student,exam where student.sex = 'f' and exam.grade >= 80;
'''

#3-4.找出人数最少的院系以及其年度预算。
'''
select dept_name,budget from department
where count(*) from student  group by dept_name
= min( count(*) from student  group by dept_name );
'''

#3-5.计算机系改名了，改成计算机科学系（comp. sci.），写出mysql语句。
'''
update dept_name set dept_name = 'comp.sci.' where dept_name = 'computer';
'''

#3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。
'''
update budget set budget = budget + 2000;

update department.budget set budget = budget + 2000 * (count(dept_name) from student where student group by department );
'''

#3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
'''
insert into department values(avg_budget,NULL,avg(budget));
'''

#3-8. 删除计算机系中考试成绩平均分低于70的学生.
'''
delete from student 
where dept_name ='computer' 
and avg(grade) where student.ID = exam.student_ID< 70;
'''

#3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
'''
update emotion_state set emotion_state = 'single'
where emotion_state = 'loving' and avg(grade) where student.ID = exam.student_ID < 75;
'''

#3-10(选做). 对每个学生, 往exam表格中插入名为Avg_Exam的考试, 考试分数为之前学生参加过考试的平均分.
