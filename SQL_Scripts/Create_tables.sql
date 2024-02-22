-- Table: Students
-- Поле id: Основний ключ задається автоматично
-- Поле student_fullname: Текстове поле ім'я студента
-- Поле subject_id: Зовнішій Ключ посилається на Таблицю Groups Поле id
DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_fullname VARCHAR(60) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES Groups (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
--Table: Groups
--Поле id: Основний ключ задається автоматично
--Поле group_name: Назва групи A,B,C...
DROP TABLE IF EXISTS Groups;
CREATE TABLE Groups(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(3)
);
--Table Grades
--Поле id: Основний ключ Задається автоматично
--Поле grade: Оцінка
--Поле student_id: Зовнішній ключ посилається на таблицю Stundets поле id
--Поле subject_id: Зовнішній ключ посилається на таблицю Subjects поле id
DROP TABLE IF EXISTS Grades;
CREATE TABLE Grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade VARCHAR(3),
    date_grading DATETIME,
    student_id INTEGER,
    subject_id INTEGER,

    FOREIGN KEY (student_id) REFERENCES Students(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    FOREIGN KEY (subject_id) REFERENCES Subjects(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
--Table: Subjects
--Поле id:
--Поле subject_name:
--professor_id:

DROP TABLE IF EXISTS Subjects;
CREATE TABLE Subjects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(100),
    professor_id INTEGER,
    FOREIGN KEY (professor_id) REFERENCES Professors(id)
);

--Table: Professors
--Поле id:
--Поле professor_name:
--Поле subject_id:
DROP TABLE IF EXISTS Professors;
CREATE TABLE Professors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    professor_name VARCHAR(60)
);