# pyinstaller -F yourprogram.py

import csv


class Saude:
    def __init__(self):
        self.info = []
        self.print_start()
        self.get_data()

    def get_data(self):
        csvfile = open('gerint_solicitacoes_mod.csv', 'r')
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            self.info.append(row)
        csvfile.close()
        self.print_menu()
        self.ask_input()

    def print_start(self):
        txt = "Carregando dados: aguarde..."
        print(txt)

    def print_menu(self):
        txt = "*****************  MENU  *****************" + "\n"
        txt += "1 - Consultar média de idade dos pacientes" + "\n"
        txt += "2 - Consultar internações por ano" + "\n"
        txt += "3 - Consultar hospitais" + "\n"
        txt += "4 - Calcular tempo de internação" + "\n"
        txt += "5 - Determinar tempos de espera na fila" + "\n"
        txt += "6 - Terminar o programa" + "\n"
        print(txt)

    def ask_input(self):
        i = input("Escolha uma das opções e aperte enter: ")
        if i == '1':
            self.one()
        elif i == '2':
            self.two()
        elif i == '3':
            self.three()
        elif i == '4':
            self.four()
        elif i == '5':
            self.five()
        elif i == '6':
            self.six()
        else:
            print("Escolha uma opção de 1 a 6: ")
            self.ask_input()

    def one(self):
        print("1")

    def two(self):
        print("2")

    def three(self):
        print("3")

    def four(self):
        print("4")

    def five(self):
        print("5")

    def six(self):
        print("6")


x = Saude()

y = "end of file"
print(y)
