import sqlite3

class University:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject TEXT,
                grade REAL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        ''')
        self.conn.commit()

    def add_student(self, name, age):
        self.cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()

    def add_grade(self, student_id, subject, grade):
        self.cursor.execute('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', (student_id, subject, grade))
        self.conn.commit()

    def get_students(self, subject=None):
        if subject:
            self.cursor.execute('SELECT s.name, s.age, g.subject, g.grade FROM students s, grades g WHERE s.id = g.student_id AND g.subject = ?', (subject,))
        else:
            self.cursor.execute('SELECT s.name, s.age, g.subject, g.grade FROM students s, grades g WHERE s.id = g.student_id')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

u1 = University('Urban')

u1.add_student('Ivan', 26)
u1.add_student('Ilya', 24)
u1.add_student('Olga', 25)
u1.add_student('Elena', 23)

u1.add_grade(1, 'Python', 4.8)
u1.add_grade(1, 'Java', 4.5)
u1.add_grade(2, 'Python', 4.3)
u1.add_grade(2, 'Java', 4.7)
u1.add_grade(3, 'Python', 4.9)
u1.add_grade(3, 'Java', 4.6)
u1.add_grade(4, 'Python', 4.7)
u1.add_grade(4, 'Java', 4.8)

print(u1.get_students())

