# Умови створення данних 
# --1. 30-50 студентів
# --2. 3 группи
# --3. 5-8 Предметів
# --4. 3-5 Викладачів
# --5. До 20 Оцінок у кожного студента з кожного предмета
#------------------------------------------------------------------------
# Система оцінювання не вказна тому Використовуєм Шкалу Лайкерта 
# --1 Абсолютно незадовільнено
# --2 Швидше погано чим добре
# --3 Середня
# --4 Задовільнено
# --5 Абсолютно задовільнено
#------------------------------------------------------------------------

from sqlite3 import Error, Connection
from faker import Faker
import datetime
from random import randint,choice,sample
from connect import create_connection
from create_db import DATABASE
NUMBER_STUDENTS = randint(30,51)
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = randint(5,9)
NUMBER_PROFESSORS = randint(3,6)
NUMBER_GRADES = randint(10,20)

SUBJECTS = ['English','Math','Science',
            'History','Social Studies',
            'Spanish','French','German',
            'Chinese','Japanese','Algebra',
            'Geometry','Calculus','Physics',
            'Chemistry','Biology','Geography',
            'Government','Economics','Psychology',
            'Sociology','Art','Music','Theater',
            'Dance','Literature','Business',
            'Computer Science','Engineering',
            'Helth','Home economics','Physical Education'
            ]

GROUP_NAME = ['A','B','C','D','E','F']

def generate_fake_data(num_students=30,num_groups=3,num_subjects=5,num_professors=3,num_grades=NUMBER_GRADES,subjects=SUBJECTS,group_name=GROUP_NAME)  -> tuple:
    fake_data = Faker()
    fake_students = []
    fake_professors = []
    fake_subjects = []
    fake_groups = []
    
    
    
    fake_groups =  sample(group_name,num_groups)
    
    fake_subjects = sample(subjects,num_subjects)
    
    
    for _ in range(num_students):    
        fake_students.append(fake_data.name())
    

    for _ in range(num_professors):
        fake_professors.append(fake_data.name())
    
    for_groups = []
    group_id = 1
    for group in fake_groups:
        for_groups.append((group,group_id))
        group_id += 1
        
        
    
    
    for_students = []
    student_id = 1
    for student in fake_students:
        for_students.append((student,randint(1,num_groups),student_id))
        student_id += 1
    
    
    for_subjects = []
    subject_id = 1
    for subject in fake_subjects:
        for_subjects.append((subject,randint(1,num_professors),subject_id))
        subject_id += 1

    
    
    for_professors = []
    professor_id = 1
    for professor in fake_professors:
        for_professors.append((professor,professor_id))
        professor_id +=1
    
    for_grades = []
    grades_id = 1
    for subject in for_subjects:
        for student in for_students:
            for g in range(NUMBER_GRADES):
                for_grades.append((randint(1,5),datetime.datetime(2024,randint(1,12),randint(1,29)).date(),student[2],subject[2],grades_id))
                grades_id += 1
    return for_groups,for_students,for_professors,for_subjects,for_grades
     
groups,students,professors,subjects,grades = generate_fake_data()

def insert_data(groups,students,professors,subjects,grades):
    with Connection(DATABASE) as conn:
        cur = conn.cursor()

        sql_to_groups = """
        INSERT INTO Groups(group_name,id)
        VALUES(?,?)
        """
        
        sql_to_student = """
        INSERT INTO Students(student_fullname,group_id,id)
        VALUES(?,?,?)
        """
        sql_to_professors = """
        INSERT INTO Professors(professor_name,id)
        VALUES(?,?)
        """
        sql_to_subjects = """
        INSERT INTO Subjects(subject_name,professor_id,id)
        VALUES(?,?,?)
        """
        sql_to_grades = """
        INSERT INTO Grades(grade,date_grading,student_id,subject_id,id)
        VALUES(?,?,?,?,?)
        """

        cur.executemany(sql_to_groups,groups)
        cur.executemany(sql_to_student,students)
        cur.executemany(sql_to_professors,professors)
        cur.executemany(sql_to_subjects,subjects)
        cur.executemany(sql_to_grades,grades)
        conn.commit()


if __name__ == '__main__':
    insert_data(groups,students,professors,subjects,grades)
