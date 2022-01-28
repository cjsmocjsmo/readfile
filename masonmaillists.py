#!/usr/bin/python3

import csv
import sqlite3

mconn = sqlite3.connect("mason.db")
mcursor = mconn.cursor()
mcursor.execute("CREATE TABLE mason(type TEXT, catagory TEXT, str_num TEXT, prefix TEXT, str_name TEXT, suffix TEXT, city TEXT, zipcode TEXT)")


class MasonMailLists:
    def __init__(self):
        pass

    def split_type(self, astr):
        foo = astr.split("-")
        type = foo[1]
        catagory = foo[2]
        return type, catagory

    def split_addr(self, addr):
        addr_split = addr.split(",")
        adr = addr_split[0].split(" ")
        str_num = adr[0]
        prefix = adr[1]
        str_name = adr[2]
        suffix = adr[3]
        cz = addr_split[1].split(" ")
        city = cz[0]
        zipcode = cz[1]
        return str_num, prefix, str_name, suffix, city, zipcode


    def parse_mason(self):

        with open('/home/2021-RP-master.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            count = 0

            try:
                for row in reader:
                    count += 1
                    type, catagory = self.split_type(row[25])
                    str_num, prefix, str_name, suffix, city, zipcode = self.split_addr(row[37])
                    entries = (type, catagory, str_num, prefix, str_name, suffix, city, zipcode)
                    mcursor.execute('INSERT INTO mason(type, catagory, str_num, prefix, str_name, suffix, city, zipcode) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(mcursor.lastrowid)
                    mconn.commit()
                    bar = "item" + str(count) + ":" + row[25] + "  " + row[37]
                    print(bar)
            except UnicodeDecodeError:
                print(row)
        return count
