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
        f_sum = m_sum = m_count = f_count = 0

        i = input("Digite o nome do município: ")
        i = i.upper()

        for x in self.info:
            if x['municipio_residencia'] == i:
                if x['sexo'] == 'MASCULINO':
                    m_sum += float(x['idade'])
                    m_count += 1
                elif x['sexo'] == 'FEMININO':
                    f_sum += float(x['idade'])
                    f_count += 1

        if (m_count + f_count) == 0:
            txt = "Município não existe ou não há nenhum paciente cadastrado"
            txt = "\n" + txt + "\n"

            print(txt)
            self.print_menu()
            self.ask_input()

        if m_count == 0:
            masc = 'nenhum paciente'
        else:
            masc = float(m_sum / m_count)

        if f_count == 0:
            fem = 'nenhum paciente'
        else:
            fem = float(f_sum / f_count)

        total = m_count + f_count
        geral = float((m_sum + f_sum)/(m_count + f_count))

        txt = "\n" + "Total de pacientes: {0}" + "\n"
        txt += "Médias de idade:" + "\n"
        txt += "    femininos:  {1:.2f}" + "\n"
        txt += "    masculinos: {2:.2f}" + "\n"
        txt += "    geral:      {3:.2f}" + "\n"
        txt = txt.format(total, fem, masc, geral)
        print(txt)

        self.print_menu()
        self.ask_input()

    def two(self):
        a = b = c = d = 0

        i = input("Digite o nome do município: ")
        i = i.upper()

        for x in self.info:
            if x['municipio_residencia'] == i:
                year = x['data_internacao'][:4]
                if year == '2018':
                    a += 1
                if year == '2019':
                    b += 1
                if year == '2020':
                    c += 1
                if year == '2021':
                    d += 1

        if (a + b + c + d) == 0:
            txt = "Município não existe ou não há nenhum paciente cadastrado"
            txt = "\n" + txt + "\n"

            print(txt)
            self.print_menu()
            self.ask_input()

        txt = "\n" + "Pacientes internados: " + "\n"
        txt += "2018: {0}" + "\n"
        txt += "2019: {1}" + "\n"
        txt += "2020: {2}" + "\n"
        txt += "2021: {3}" + "\n"
        txt = txt.format(a, b, c, d)
        print(txt)

        self.print_menu()
        self.ask_input()

    def three(self):     # todo
        print("3")

    def four(self):     # todo
        print("4")

    def five(self):     # todo
        print("5")

    def six(self):
        exit()


x = Saude()

y = "end of file"
print(y)
