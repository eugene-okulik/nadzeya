import csv
import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


with (open(data_file_path, newline='') as csv_file):
    file_data = csv.DictReader(csv_file)
    missing_data = []

    for row in file_data:
        name = row['name']
        second_name = row['second_name']
        group_title = row['group_title']
        book_title = row['book_title']
        subject_title = row['subject_title']
        lesson_title = row['lesson_title']
        mark_value = row['mark_value']

        select_query = '''
        SELECT
        s.name, s.second_name, g.title, b.title, sub.title, l.title, m.value
        FROM students s
        JOIN `groups` g ON s.group_id = g.id
        JOIN books b ON b.taken_by_student_id = s.id
        JOIN marks m ON m.student_id = s.id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects sub ON l.subject_id = sub.id
        WHERE s.name = %s AND s.second_name = %s AND g.title = %s
        AND b.title = %s AND sub.title = %s AND l.title = %s AND m.value = %s'''

        cursor.execute(select_query, (name, second_name, group_title,
                                      book_title, subject_title, lesson_title, mark_value))

        result = cursor.fetchall()
        if result not in file_data:
            missing_data.append(row)


if missing_data:
    print('Absent data: ')
    for row in missing_data:
        print(row)
else:
    print('All data is present in db.')


db.close()
