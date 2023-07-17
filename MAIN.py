import sqlite3 as sql
from sqlite3 import Error
import csv 
import time
import os
import sys




os.mkdir("usercache")
tableName = input("What do you want to name the table? : ")
with open('usercache/usercache.txt', 'w') as f:
    f.write(f'{tableName}')
    

with open('usercache/searchcache.txt', 'w') as c:
    c.write('F')
# ! end user cache

connection = sql.connect('main.db') 

db = connection.cursor()


files = os.listdir('./files')
print(files)

db.execute(f'CREATE TABLE IF NOT EXISTS {tableName}(fakeColumn TEXT)')

startTime = time.time()

with open(f'./files/{files[0]}', 'r') as sample_file1:
    sample_file = csv.reader(sample_file1)
    firstRun = True
    column_names = next(sample_file)
    print (column_names)
    next(sample_file)
    for column in column_names:
        db.execute(f'ALTER TABLE {tableName} ADD COLUMN {column} TEXT')
        
new_table_columns = ', '.join(column_names)

db.execute(f'CREATE TABLE IF NOT EXISTS {tableName}_new ({new_table_columns})')

db.execute(f'INSERT INTO {tableName}_new SELECT {new_table_columns} FROM {tableName}')

db.execute(f'DROP TABLE {tableName}')

db.execute(f'ALTER TABLE {tableName}_new RENAME TO {tableName}')

for data in files:
    data = './files/' + data
    with open(data, 'r') as file:
        csv_data = csv.reader(file)
        
        next(csv_data)

    # ! only use at the first run of the program
    # ! ONLY RUN ONCE
        for row in csv_data:
            if len(row) == len(column_names):
                placeholders = ', '.join(['?'] * len(column_names))
                query = f'INSERT INTO {tableName}({", ".join(column_names)}) VALUES ({placeholders})'
                db.execute(query, row)
            else:
                print(f"Ignoring row with incorrect number of values: {row}")

    # ! only use at the first run of the program

endTime = time.time()
print (f'Finished in {endTime - startTime}')

print ('This is for making quicker searches in the database.')
# ! user cache

with open('usercache/usercache.txt', 'r') as f:
    tableName = f.read()

# ! end user cache

#! file2
with open('usercache/searchcache.txt', 'r') as c:
    searchCacheText = c.read()

    
if searchCacheText == 'T':
    print ('You have already created an index for this table. You can still search for other columns, but it will be slower.')
    sys.exit()

if searchCacheText == 'F':
    with open('usercache/searchcache.txt', 'w') as d:
        print("You have not created an index for this table. Please create an index before searching.")
        commonQuery = input("What column do you usually search by? (MAKE SURE THE COLUMN NAME MATCHES THE INPUT CSV) : ")
        indexName = f'idx_{commonQuery}'
        indexColumnName = f'{commonQuery}'
        db.execute(f"CREATE INDEX {indexName} ON {tableName}({indexColumnName})")
        d.write('T')


print ('Completed successfully! To view the database, use a program like DB Browser for SQLite to view and filter through your data.')
connection.commit()
connection.close()