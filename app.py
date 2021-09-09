# pyinstaller -F yourprogram.py

import csv
import json

info = []
csvfile = open('gerint_solicitacoes_mod.csv', 'r')

reader = csv.DictReader(csvfile, delimiter=";")

for row in reader:
    info.append(row)

csvfile.close()
