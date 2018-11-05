# -*- coding: utf-8 -*-

import pyodbc
import json
import lxml.html.
import time

server = 'eventmobilesrv.database.windows.net'
database = 'TDK_MOB_DEV_10'
username = 'eventmobile'
password = '@mobileapp2018'


CONN_STR = 'DRIVER={SQL Server};' \
                        f'server={server}.;DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(CONN_STR)
cursor = conn.cursor()
response = cursor.execute("select * from dbo.users")
for record in response:
    print(json.dumps(record))


cursor.close()
conn.close()