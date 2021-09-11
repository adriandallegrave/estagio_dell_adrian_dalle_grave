import csv
import datetime


def convert_date(str):
    # Helper function. Converts 2018-05-02 to 02/05/2018
    str = str.strip()
    result = str[8:] + "/" + str[5:7] + "/" + str[:4]
    return result


def time_delta(a, b):
    # Calculates difference between 2 dates
    c = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
    d = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S.%f')
    e = d - c

    return str(e.days)


class Saude:
    def __init__(self, menu='', input=''):
        # When args are filled tests can be made
        self.info = []
        self.menu = menu
        self.input = input
        self.teste = False
        self.print_start()
        self.get_data()

    def get_data(self):
        # Opens and store csv data into self.info
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
        if self.menu == '':
            i = input("Escolha uma das opções e aperte enter: ")
        else:
            i = self.menu
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

        if self.input == '':
            i = input("Digite o nome do município: ")
        else:
            i = self.input

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
            if self.menu != '':
                self.six()
            else:
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

        self.teste = True

        if self.menu != '':
            self.six()
        else:
            self.print_menu()
            self.ask_input()

    def two(self):
        a = b = c = d = 0

        if self.input == '':
            i = input("Digite o nome do município: ")
        else:
            i = self.input

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

            if self.menu != '':
                self.six()
            else:
                self.print_menu()
                self.ask_input()

        txt = "\n" + "Pacientes internados: " + "\n"
        txt += "2018: {0}" + "\n"
        txt += "2019: {1}" + "\n"
        txt += "2020: {2}" + "\n"
        txt += "2021: {3}" + "\n"
        txt = txt.format(a, b, c, d)
        print(txt)

        if self.menu != '':
            self.six()
        else:
            self.print_menu()
            self.ask_input()

    def three(self):
        result = []

        if self.input == '':
            i = input("Digite o nome do executante: ")
        else:
            i = self.input

        i = i.upper()

        for x in self.info:
            if x['executante'] == i:
                idade = x['idade']
                res = x['municipio_residencia']
                sol = x['solicitante']
                aut = x['data_autorizacao'][:10]
                aut = convert_date(aut)
                intern = x['data_internacao'][:10]
                intern = convert_date(intern)
                alta = x['data_alta'][:10]
                alta = convert_date(alta)
                execut = x['executante']

                txt = "===========================================" + "\n"
                txt += "idade: {0}" + "\n"
                txt += "residência: {1}" + "\n"
                txt += "solicitante: {2}" + "\n"
                txt += "data de autorização: {3}" + "\n"
                txt += "data de internação: {4}" + "\n"
                txt += "data de alta: {5}" + "\n"
                txt += "executante: {6}" + "\n"
                txt = txt.format(idade, res, sol, aut, intern, alta, execut)
                result.append(txt)

        if len(result) == 0:
            txt = "Executante não existe ou não há nenhum paciente cadastrado"
            txt = "\n" + txt + "\n"

            print(txt)

            if self.menu != '':
                self.six()
            else:
                self.print_menu()
                self.ask_input()
        else:
            for x in result:
                print(x)

            if self.menu != '':
                self.six()
            else:
                self.print_menu()
                self.ask_input()

    def four(self):
        executantes = {None}
        new_list = []
        txt = ""

        if self.input == '':
            i = input("Digite o nome do solicitante: ")
        else:
            i = self.input

        i = i.upper()

        for x in self.info:
            if x['solicitante'] == i:
                executantes.add(x['executante'])
                new_list.append(x)

        for x in executantes:
            i = 1
            txt += "===========================================" + "\n"
            txt += "Hospital executante: {}" + "\n"
            txt = txt.format(x)
            for y in new_list:
                if y['executante'] == x:
                    z = time_delta(y['data_internacao'], y['data_alta'])
                    txt += "paciente " + str(i)
                    txt += " ficou internado por " + str(z) + " dias." + "\n"
                    i += 1

        if len(executantes) == 0:
            err = "Solicitante não existe ou não há nenhum paciente cadastrado"
            err = "\n" + txt + "\n"

            print(err)

            if self.menu != '':
                self.six()
            else:
                self.print_menu()
                self.ask_input()
        else:
            print(txt)

            if self.menu != '':
                self.six()
            else:
                self.print_menu()
                self.ask_input()

    def five(self):
        result = []

        for i in range(5):
            result.append(self.info[i])

        result = sorted(result, key=lambda k: int(k['horas_na_fila']))
        for x in self.info:
            if int(x['horas_na_fila']) > int(result[0]['horas_na_fila']):
                result.pop(0)
                i = 0
                for v in range(4):
                    b = int(result[v]['horas_na_fila'])
                    if int(x['horas_na_fila']) > b:
                        i += 1
                result.insert(i, x)

        txt = "\n" + (79 * "=") + "\n"
        for i in result:
            txt += "Dia de extração: " + convert_date(i['data_extracao'][:10])
            txt += "\n"
            txt += "ID do usuario: " + i['id_usuario'] + "\n"
            txt += "Situação: " + i['situacao'] + "\n"
            txt += "Central regulação origem: " + i['central_regulacao_origem']
            txt += "\n"
            txt += "Data de solicitação: "
            txt += convert_date(i['data_solicitacao']) + "\n"
            txt += "Sexo: " + i['sexo'] + "\n"
            txt += "Idade: " + i['idade'] + "\n"
            txt += "Município de residência: " + i['municipio_residencia']
            txt += "\n"
            txt += "Solicitante: " + i['solicitante'] + "\n"
            txt += "Município solicitante: " + i['municipio_solicitante']
            txt += "\n"
            txt += "Código CID: " + i['codigo_cid'] + "\n"
            txt += "Caráter: " + i['carater'] + "\n"
            txt += "Tipo de internação: " + i['tipo_internacao'] + "\n"
            txt += "Tipo de leito: " + i['tipo_leito'] + "\n"
            txt += "Data de autorização: "
            txt += convert_date(i['data_autorizacao'][:10]) + "\n"
            txt += "Data de internação: "
            txt += convert_date(i['data_internacao'][:10]) + "\n"
            txt += "Data de alta: " + convert_date(i['data_alta'][:10]) + "\n"
            txt += "Executante: " + i['executante'] + "\n"
            txt += "Horas na fila: " + i['horas_na_fila'] + "\n"
            txt += (79 * "=") + "\n"

        print(txt)

        if self.menu != '':
            self.six()
        else:
            self.print_menu()
            self.ask_input()

    def six(self):
        pass
