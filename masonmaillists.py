#!/usr/bin/python3

import csv
import sqlite3

mconn = sqlite3.connect("mason.db")
mcursor = mconn.cursor()
mcursor.execute("CREATE TABLE mason(type TEXT, str_address TEXT)")


class MasonMailLists:
    def __init__(self):
        pass


    def parse_mason(self):

        with open('/home/2021-RP-master.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            count = 0

            try:
                for row in reader:
                    count += 1
                    entries = (row[25], row[37])
                    mcursor.execute('INSERT INTO mason(type, str_address) VALUES(?, ?)', entries)
                    print(mcursor.lastrowid)
                    mconn.commit()
                    bar = "item" + str(count) + ":" + row[25] + "  " + row[37]
                    print(bar)
            except UnicodeDecodeError:
                print(row)
        return count
