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
        if len(foo) != 3:
            pass
        else:
            print(foo)
            type = foo[1]
            catagory = foo[2]
            return type, catagory

    def split_addr(self, addr):
        addr_split = addr.split(",")
        print(addr_split)
        adr = addr_split[0].split(" ")
        print(adr)
        # try:
        str_num = adr[0]
        prefix = adr[1]
        str_name = adr[2]
        suffix = adr[3]
        # except IndexError:
        #     print("index error {}".format(addr_split))

        # try:
        cz = addr_split[1].split(" ")
        print(cz)
        city = cz[1]
        zipcode = cz[2]
            
        # except IndexError:
            # print(addr_split)
        return str_num, prefix, str_name, suffix, city, zipcode

    def parse_mason(self):

        with open('/home/2021-RP-master.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            count = 0

            try:
                for row in reader:
                    count += 1
                    try:
                        type, catagory = self.split_type(row[25])
                    except TypeError:
                        print(row[25])
                    
                    try:
                        str_num, prefix, str_name, suffix, city, zipcode = self.split_addr(row[37])
                        entries = (type, catagory, str_num, prefix, str_name, suffix, city, zipcode)
                        mcursor.execute('INSERT INTO mason(type, catagory, str_num, prefix, str_name, suffix, city, zipcode) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                        print(mcursor.lastrowid)
                        mconn.commit()
                    except IndexError:
                        print(row[37])
                    
                    bar = "item" + str(count) + ":" + row[25] + "  " + row[37]
                    print(bar)
            except UnicodeDecodeError:
                print(row)
        return count
