 #!/usr/bin/python3

import os
# import re
# import csv
import pandas as pd
# import pymongo
import sqlite3
from io import BytesIO

import kitsapmaillists
import masonmaillists
import piercemaillists




# mconn = sqlite3.connect("mason.db")
# mcursor = mconn.cursor()
# mcursor.execute("CREATE TABLE mason(type TEXT, str_address TEXT)")
# class MasonMailLists:
#     def __init__(self):
#         pass


# pconn = sqlite3.connect("pierce.db")
# pcursor = pconn.cursor()
# pcursor.execute("CREATE TABLE pierce(catagory TEXT, str_name TEXT, str_num TEXT, type TEXT)")

# ['KEYPORT', 'BREMERTON', 'KINGSTON', 'INDIANOLA', 'GIG HARBOR', 'SEABECK', 'BELFAIR', 'BAINBRIDGE ISLAND', 'SUQUAMISH',
#     'SILVERDALE', 'HANSVILLE', 'PORT ORCHARD', 'OLALLA', 'PORT GAMBLE', 'POULSBO']




class CreateMailLists:

    def __init__(self):
        self.basedir = "/home/charliepi/readfile/"

    def convert_xlsx(self):
        read_file = pd.read_excel("/home/2021-RP-master.xlsx")
        read_file.to_csv("/home/2021-RP-master.csv", index = None, header=False)

    def main(self):
        # if not os.path.exists("/home/Property_addresses.txt"):
        #     os.system("sh /home/kitsap.sh")
        # KML = kitsapmaillists.KitsapMailLists()
        # KML.parse_kitsap()

        if not os.path.exists("/home/2021-RP-master.xlsx"):
            os.system("sh /home/mason.sh")
            self.convert_xlsx()
        MML = masonmaillists.MasonMailLists()
        MML.parse_mason()

        # if not os.path.exists("/home/tax_account.zip"):
        #     os.system("sh /home/pierce.sh")
        
        

        
        
       

if __name__ == "__main__":
    foo = CreateMailLists()
    foo.main()