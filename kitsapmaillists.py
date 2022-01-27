#!/usr/bin/python3

# import os
# import re
# import csv
# import pandas as pd
# import pymongo
import sqlite3
# from io import BytesIO

BAINBRIDGEISLAND_conn = sqlite3.connect("BAINBRIDGEISLAND.db")
BAINBRIDGEISLAND_cursor = BAINBRIDGEISLAND_conn.cursor()
BAINBRIDGEISLAND_cursor.execute("CREATE TABLE bainbridgeisland(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

BELFAIR_conn = sqlite3.connect("BELFAIR.db")
BELFAIR_cursor = BELFAIR_conn.cursor()
BELFAIR_cursor.execute("CREATE TABLE belfair(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

BREMERTON_conn = sqlite3.connect("BREMERTON.db")
BREMERTON_cursor = BREMERTON_conn.cursor()
BREMERTON_cursor.execute("CREATE TABLE bremerton(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")


GIGHARBOR_conn = sqlite3.connect("GIGHARBOR.db")
GIGHARBOR_cursor = GIGHARBOR_conn.cursor()
GIGHARBOR_cursor.execute("CREATE TABLE gigharbor(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

HANSVILLE_conn = sqlite3.connect("HANSVILLE.db")
HANSVILLE_cursor = HANSVILLE_conn.cursor()
HANSVILLE_cursor.execute("CREATE TABLE hansville(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

INDIANOLA_conn = sqlite3.connect("INDIANOLA.db")
INDIANOLA_cursor = INDIANOLA_conn.cursor()
INDIANOLA_cursor.execute("CREATE TABLE indianola(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

KINGSTON_conn = sqlite3.connect("KINGSTON.db")
KINGSTON_cursor = KINGSTON_conn.cursor()
KINGSTON_cursor.execute("CREATE TABLE kingston(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

KEYPORT_conn = sqlite3.connect("KEYPORT.db")
KEYPORT_cursor = KEYPORT_conn.cursor()
KEYPORT_cursor.execute("CREATE TABLE keyport(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

OLALLA_conn = sqlite3.connect("OLALLA.db")
OLALLA_cursor = OLALLA_conn.cursor()
OLALLA_cursor.execute("CREATE TABLE olalla(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

PORTGAMBLE_conn = sqlite3.connect("PORTGAMBLE.db")
PORTGAMBLE_cursor = PORTGAMBLE_conn.cursor()
PORTGAMBLE_cursor.execute("CREATE TABLE portgamble(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

PORTORCHARD_conn = sqlite3.connect("PORTORCHARD.db")
PORTORCHARD_cursor = PORTORCHARD_conn.cursor()
PORTORCHARD_cursor.execute("CREATE TABLE portorchard(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

POULSBO_conn = sqlite3.connect("POULSBO.db")
POULSBO_cursor = POULSBO_conn.cursor()
POULSBO_cursor.execute("CREATE TABLE poulsbo(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

SEABECK_conn = sqlite3.connect("SEABECK.db")
SEABECK_cursor = SEABECK_conn.cursor()
SEABECK_cursor.execute("CREATE TABLE seabeck(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

SILVERDALE_conn = sqlite3.connect("SILVERDALE.db")
SILVERDALE_cursor = SILVERDALE_conn.cursor()
SILVERDALE_cursor.execute("CREATE TABLE silverdale(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

SUQUAMISH_conn = sqlite3.connect("SUQUAMISH.db")
SUQUAMISH_cursor = SUQUAMISH_conn.cursor()
SUQUAMISH_cursor.execute("CREATE TABLE suquamish(st_no TEXT, prefix TEXT, str_name TEXT, identifier TEXT, city TEXT, state TEXT, zip TEXT, street_addr TEXT)")

class KitsapMailLists:
    def __init__(self):
        pass

    def parse_kitsap(self):
        count = 0
        with open('/home/Property_addresses.txt', 'r') as file1:
            while True:
                count += 1
                line = file1.readline()
                if not line:
                    break
                line_array = line.strip().split("\t")
                print(line_array)
                entries = (line_array[2], line_array[3], line_array[4], line_array[5], line_array[8], line_array[9], line_array[10], line_array[11])
                if line_array[8] == 'BAINBRIDGE ISLAND':
                    BAINBRIDGEISLAND_cursor.execute('INSERT INTO bainbridgeisland(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(BAINBRIDGEISLAND_cursor.lastrowid)
                    BAINBRIDGEISLAND_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'BELFAIR':
                    BELFAIR_cursor.execute('INSERT INTO belfair(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(BELFAIR_cursor.lastrowid)
                    BELFAIR_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'BREMERTON':
                    BREMERTON_cursor.execute('INSERT INTO bremerton(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(BREMERTON_cursor.lastrowid)
                    BREMERTON_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'GIG HARBOR':
                    GIGHARBOR_cursor.execute('INSERT INTO gigharbor(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(GIGHARBOR_cursor.lastrowid)
                    GIGHARBOR_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'HANSVILLE':
                    HANSVILLE_cursor.execute('INSERT INTO hansville(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(HANSVILLE_cursor.lastrowid)
                    HANSVILLE_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'INDIANOLA':
                    INDIANOLA_cursor.execute('INSERT INTO indianola(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(INDIANOLA_cursor.lastrowid)
                    INDIANOLA_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'KEYPORT':
                    KEYPORT_cursor.execute('INSERT INTO keyport(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(KEYPORT_cursor.lastrowid)
                    KEYPORT_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'KINGSTON':
                    KINGSTON_cursor.execute('INSERT INTO kingston(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(KINGSTON_cursor.lastrowid)
                    KINGSTON_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'OLALLA':
                    OLALLA_cursor.execute('INSERT INTO olalla(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(OLALLA_cursor.lastrowid)
                    OLALLA_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'PORT GAMBLE':
                    PORTGAMBLE_cursor.execute('INSERT INTO portgamble(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(PORTGAMBLE_cursor.lastrowid)
                    PORTGAMBLE_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'PORT ORCHARD':
                    PORTORCHARD_cursor.execute('INSERT INTO portorchard(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(PORTORCHARD_cursor.lastrowid)
                    PORTORCHARD_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'POULSBO':
                    POULSBO_cursor.execute('INSERT INTO poulsbo(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(POULSBO_cursor.lastrowid)
                    POULSBO_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'SEABECK':
                    SEABECK_cursor.execute('INSERT INTO seabeck(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(SEABECK_cursor.lastrowid)
                    SEABECK_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'SILVERDALE':
                    SILVERDALE_cursor.execute('INSERT INTO silverdale(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(SILVERDALE_cursor.lastrowid)
                    SILVERDALE_conn.commit()
                    print("Line: {}".format(count))
                elif line_array[8] == 'SUQUAMISH':
                    SUQUAMISH_cursor.execute('INSERT INTO suquamish(st_no, prefix, str_name, identifier, city, state, zip, street_addr) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entries)
                    print(SUQUAMISH_cursor.lastrowid)
                    SUQUAMISH_conn.commit()
                    print("Line: {}".format(count))
        return count
        
# ['KEYPORT', 'BREMERTON', 'KINGSTON', 'INDIANOLA', 'GIG HARBOR', 'SEABECK', 'BELFAIR', 'BAINBRIDGE ISLAND', 'SUQUAMISH',
#     'SILVERDALE', 'HANSVILLE', 'PORT ORCHARD', 'OLALLA', 'PORT GAMBLE', 'POULSBO']