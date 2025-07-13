import sqlite3
conn=sqlite3.connect('example.db')
conn.execute('''
             Create table student(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nameVARCHAR(50),
                age INTEGER ,       
                
             )
             
             
             
             
             ''')
conn.close()