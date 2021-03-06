#!/usr/bin/python3

import re
import csv
import sqlite3

mconn = sqlite3.connect("mason.db")
mcursor = mconn.cursor()
mcursor.execute("CREATE TABLE mason(type TEXT, catagory TEXT, str_num TEXT, prefix TEXT, str_name TEXT, city TEXT, zipcode TEXT)")
# ['', 'ALLYN', 'GRAPEVEIW', 'TAHUYA', 'ELMA', 'BREMERTON', '420', 'SHELTON', 'MCCLEARY', 'BEFAIR', 'BELFAIR', 'HOODSPORT',
#  'HOODPSORT', 'PICKERING', 'OLYMPIA', 'MATLOCK', 'ST', "STE'S", 'GRAPEVIEW', 'HOODDSPORT', 'LILLWAUP', 'UNION', 'LILLIWAUP', 'MONTESANO']

class MasonMailLists:
    def __init__(self):
        self.cities = []
        self.row_count = []
        self.regex1 = re.compile(",")

    def split_type(self, astr):
        foo = astr.split("-")
        if len(foo) != 3:
            print("this is foo {}".format(foo))
        else:
            type = foo[1]
            catagory = foo[2]
            return type, catagory

    def split_addr(self, addr):
        rpl_spc = addr.replace("  ", " ").strip()
        if re.search(self.regex1, rpl_spc) != None:

            addr_split = rpl_spc.split(",")
            ad = addr_split[0].strip()
            adr = ad.split(" ", 2)
            str_num = adr[0]
            prefix = adr[1]
            str_name = adr[2]
            # suffix = adr[3]

            cz1 = addr_split[1].strip()
            cz = cz1.split()
            if len(cz) > 1:
                city = cz[0]
                self.cities.append(cz[0])
                zipcode = cz[1]
            elif len(cz) == 1:
                city = cz[0]
                self.cities.append(cz[0])
                zipcode = "None"
            else:
                city = "None"
                zipcode = "None"
            return str_num, prefix, str_name, city, zipcode
        else:
            boo = rpl_spc.split("  ")
            print(boo[0])
            print(boo[1])
            boo1 = boo[0].split(" ", 2)
            str_num = boo1[0]
            prefix = boo1[1]
            str_name = boo1[2]

            city = boo[1]
            zipcode = "None"
            print("this is rpl_spc {}".format(rpl_spc))
            print(str_num, prefix, str_name, city, zipcode)
            return str_num, prefix, str_name, city, zipcode

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
                        print("this is row[25] {}".format(row[25]))
                    try:
                        str_num, prefix, str_name, city, zipcode = self.split_addr(row[37])
                        entries = (type, catagory, str_num, prefix, str_name, city, zipcode)
                        mcursor.execute('INSERT INTO mason(type, catagory, str_num, prefix, str_name, city, zipcode) VALUES(?, ?, ?, ?, ?, ?, ?)', entries)
                        print(mcursor.lastrowid)
                        mconn.commit()
                    except IndexError:
                        print("this is row[25] {}".format(row[25]))
                        print("this is row[37] {}".format(row[37]))
                    
                    bar = "item" + str(count) + ":" + row[25] + "  " + row[37]
                    print(str(count))
                    self.row_count.append(len(row))
                    
            except UnicodeDecodeError:
                print(row)

            print(list(set(self.cities)))
            print(list(set(self.row_count)))
        return count
