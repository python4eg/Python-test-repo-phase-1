import psycopg2

connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres', password='postgres')


cursor = connection.cursor()
cursor.execute('SELECT * FROM person')
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchall())
cursor.execute('SELECT * FROM person')
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchall())
name = 'Zidan); Drop table players; --'
cursor.execute("INSERT INTO players(name) values(%s)", (name, ))

names = [('name1', ), ('name2', ), ('name3', )]
cursor.executemany(f"INSERT INTO players(name) values(%s)", names)
connection.commit()
try:
    cursor.execute('CREATE TABLE players (id serial primary key, name varchar(100))')
    cursor.close()
    connection.commit()
except:
    print('Ha')
    connection.rollback()



connection.close()