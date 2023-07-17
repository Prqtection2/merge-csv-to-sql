# merge-csv-to-sql
This program will merge multiple CSV files into one .db file, which can be exported back to CSV, and read and searched in an SQLite Browser.

# Requirements
Python 3.10 with PIP
Recommended: DB Browser for SQLite so you can filter and read the data if your files are massive.
DB Browser for SQLite: https://sqlitebrowser.org/
# Instructions
You should only currently have init.py and MAIN.py in your directory. Now, run init.py by opening your terminal and running:
`python init.py`
This will create the files directory for you, and will also install all of the requirements using PIP.

Place all of your CSV files that you want to merge in the files directory. Now you can run MAIN.py using:
`python MAIN.py`
This will create the database file with all of your merged data.
Keep in mind this may take time, depending on the size of your CSV files. 

# Reading and Searching

To read this database file, use the DB Browser for SQLite, and click Open Database. Navigate to your project directory, and click on main.db. This will open up a merged version of all your CSV files. Here you can view, filter, and edit the database.

If you found this repository useful, please give it a star :). Thanks!
