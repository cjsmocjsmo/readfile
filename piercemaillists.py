#!/usr/bin/python3

import sqlite3


pconn = sqlite3.connect("pierce.db")
pcursor = pconn.cursor()
pcursor.execute("CREATE TABLE pierce(catagory TEXT, str_name TEXT, str_num TEXT, type TEXT)")



class PierceMailLists:
    def __init__(self):
        pass

    def parse_pierce(self):
        count = 0
        with open('/home/tax_account.txt', 'r') as file1:
            while True:
                count += 1
                line = file1.readline()
                if not line:
                    break
                line_array = line.strip().split("|")
                entries = (line_array[1], line_array[3], line_array[4], line_array[5])
                pcursor.execute('INSERT INTO pierce(catagory, str_name, str_num, type) VALUES(?, ?, ?, ?)', entries)
                print(pcursor.lastrowid)
                pconn.commit()
                print(entries)
        return count
