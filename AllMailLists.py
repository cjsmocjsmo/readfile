 #!/usr/bin/python3

import os
import re
import csv
import pandas as pd
# import pymongo
import sqlite3
from io import BytesIO

import kitsapmaillists


# kconn = sqlite3.connect("kitsap.db")
# kcursor = kconn.cursor()
# kcursor.execute("CREATE TABLE kitsap(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")
# class KitsapMailLists:
#     def __init__(self):
#         pass




mconn = sqlite3.connect("mason.db")
mcursor = mconn.cursor()
mcursor.execute("CREATE TABLE mason(type TEXT, str_address TEXT)")
class MasonMailLists:
    def __init__(self):
        pass


pconn = sqlite3.connect("pierce.db")
pcursor = pconn.cursor()
pcursor.execute("CREATE TABLE pierce(catagory TEXT, str_name TEXT, str_num TEXT, type TEXT)")

# ['KEYPORT', 'BREMERTON', 'KINGSTON', 'INDIANOLA', 'GIG HARBOR', 'SEABECK', 'BELFAIR', 'BAINBRIDGE ISLAND', 'SUQUAMISH',
#     'SILVERDALE', 'HANSVILLE', 'PORT ORCHARD', 'OLALLA', 'PORT GAMBLE', 'POULSBO']




class CreateMailLists:

    def __init__(self):
        self.basedir = "/home/charliepi/readfile/"

    def convert_xlsx(self):
        read_file = pd.read_excel("/home/2021-RP-master.xlsx")
        read_file.to_csv("/home/2021-RP-master.csv", index = None, header=False)

    # def parse_kitsap(self):

    #     count = 0
    #     with open('/home/Property_addresses.txt', 'r') as file1:
    #         while True:
    #             count += 1
    #             line = file1.readline()
    #             if not line:
    #                 break
    #             line_array = line.strip().split("\t")
    #             print(line_array)
    #             entries = (line_array[2], line_array[3], line_array[4], line_array[5], line_array[8], line_array[9], line_array[10], line_array[11])
    #             # kdb.main.insert_one(foo)
    #             kcursor.execute('INSERT INTO kitsap(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
    #             # kcursor.execute("INSERT INTO kitsap VALUES ")
    #             print(kcursor.lastrowid)
    #             kconn.commit()
    #             print("Line: {}".format(count))
    #     return count

    def parse_mason(self):

        s1 = re.compile("Undeveloped")
        s2 = re.compile("Resource")
        s3 = re.compile("Recreational")
        s4 = re.compile("Transportation")

        with open('/home/2021-RP-master.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            count = 0

            try:
                for row in reader:
                    count += 1
                    if re.search(s1, row[25]) != None:
                        pass
                    elif re.search(s2, row[25]) != None:
                        pass
                    elif re.search(s3, row[25]) != None:
                        pass
                    elif re.search(s4, row[25]) != None:
                        pass
                    else:
                        entries = (row[25], row[37])
                        mcursor.execute('INSERT INTO mason(type, str_address) VALUES(?, ?)', entries)
                        print(mcursor.lastrowid)
                        mconn.commit()
                        bar = "item" + str(count) + ":" + row[25] + "  " + row[37]
                        print(bar)
            except UnicodeDecodeError:
                print(row)
        return count

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

    def main(self):
        if not os.path.exists("/home/Property_addresses.txt"):
            os.system("sh /home/kitsap.sh")

        # if not os.path.exists("/home/2021-RP-master.xlsx"):
        #     os.system("sh /home/mason.sh")
        #     self.convert_xlsx()

        # if not os.path.exists("/home/tax_account.zip"):
        #     os.system("sh /home/pierce.sh")
        
        KML = kitsapmaillists().KitsapMailLists()
        KML.parse_kitsap()


        # c1 = self.parse_kitsap()
        # rows = kcursor.execute("SELECT city FROM kitsap").fetchall()
        # cityList = []
        # for row in rows:
        #     cityList.append(row)
        # citylist2 = list(set(cityList))
        # print(citylist2)

        # c2 = self.parse_mason()
        # c3 = self.parse_pierce()
        # zoo = c1 + c2 + c3
        
       

if __name__ == "__main__":
    foo = CreateMailLists()
    foo.main()