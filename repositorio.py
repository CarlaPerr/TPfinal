#! /usr/bin/python3

import sqlite3

class Repositorio:
    def __init__(self):
        self.bd = sqlite3.connect("bd.sqlite")
        self.cursor = self.bd.cursor()


