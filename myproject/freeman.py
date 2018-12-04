#!/usr/bin/env python

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='LabPracticalBackup')

cur = conn.cursor()
cur.execute("SELECT * FROM Employee_Main")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()
