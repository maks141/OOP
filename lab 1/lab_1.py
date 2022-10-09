import sqlite3

db = sqlite3.connect('data.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS workers (
    name TEXT,
    age INT,
    salary BIGINT
)""")

db.commit()

name = input('Введите ФИО: ')
age = int(input('Введите возраст: '))
salary = int(input('Введите зарплату: '))

sql.execute(f"INSERT INTO workers VALUES (?, ?, ?)", (name, age, salary))
db.commit()

quest = input('Хотите сделать сортировку по зарплате?(да/нет): ')

if quest == 'да':
    sql.execute("SELECT * FROM workers ORDER BY salary")
    print(sql.fetchall())
    db.commit()
    
db.close()