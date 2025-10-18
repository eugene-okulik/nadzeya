import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True)

insert_query1 = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(insert_query1, ('Jack', 'London'))
student_id = cursor.lastrowid
print(student_id)

insert_query2 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(insert_query2, [('Martin Eden', student_id), ('White Fang', student_id)])

insert_query3 = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_query3, ('liberal arts', 'Sep 2025', 'Jan 2026'))
group_id = cursor.lastrowid
print(group_id)

update_query1 = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_query1, (group_id, student_id))

insert_query4 = "INSERT INTO subjects (title) VALUES (%s)"
cursor.execute(insert_query4, ('literature_a', ))
subject_a_id = cursor.lastrowid
print(subject_a_id)

cursor.execute(insert_query4, ('literature_b', ))
subject_b_id = cursor.lastrowid
print(subject_b_id)

insert_query5 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.execute(insert_query5, ('lesson1_literature_a', subject_a_id))
lesson1_a_id = cursor.lastrowid
print(lesson1_a_id)

cursor.execute(insert_query5, ('lesson2_literature_a', subject_a_id))
lesson2_a_id = cursor.lastrowid
print(lesson2_a_id)

cursor.execute(insert_query5, ('lesson1_literature_b', subject_b_id))
lesson1_b_id = cursor.lastrowid
print(lesson1_b_id)

cursor.execute(insert_query5, ('lesson2_literature_b', subject_b_id))
lesson2_b_id = cursor.lastrowid
print(lesson2_b_id)

insert_query6 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.execute(insert_query6, (5, lesson1_a_id, student_id))
cursor.execute(insert_query6, (7, lesson2_a_id, student_id))
cursor.execute(insert_query6, (8, lesson1_b_id, student_id))
cursor.execute(insert_query6, (10, lesson2_b_id, student_id))

select_query1 = "SELECT value FROM marks WHERE student_id = %s"
cursor.execute(select_query1, (student_id, ))
print(cursor.fetchall())

select_query2 = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(select_query2, (student_id, ))
print(cursor.fetchall())

select_query3 = '''
SELECT
s.name AS student_name, s.second_name AS student_second_name, g.title AS group_title,
b.title AS book_title, sub.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = %s
'''
cursor.execute(select_query3, (student_id, ))
print(cursor.fetchall())

db.commit()

db.close()
