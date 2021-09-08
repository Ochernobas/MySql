import mysql.connector

con = mysql.connector.connect(host = 'localhost', database = 'testpython', user = 'testPython', password = 'senhateste')

def criarTabela():
    table_name = input("Digite o nome da tabela \n")
    col_num = input("Digite o número de colunas \n")
    cols = []

    col_command = []
    final_command = ""
    primaria = False

#   Preenche a lista com listas vazias
    for i in range(0, int(col_num)):
        cols.append([])
        col_command.append([])

#   Preenche as listas vazias com as colunas da tabela
    for i in range(0, int(col_num)):
        cols[i].append(input("Digite o nome da coluna " + str(i + 1) + "\n"))
        cols[i].append(input("Digite o tipo da coluna " + str(i + 1) + " dentre os indicados abaixo\nint\nvarchar\ndate\n"))

        if cols[i][1] == "varchar":
            cols[i].append(input("Digite a quantidade máxima de caracteres: \n"))
        else:
            cols[i].append(str(0))

        if primaria == False:
            cols[i].append(input("Ele é a Chave Primária ? (y/n)"))
        if cols[i][3] == "y":
            primaria != primaria

        cols[i].append(input("Ele é um Auto Increment ? (y/n)"))

        if cols[i][3] != "y":
            cols[i].append(input("Ele pode ser um valor nulo ? (y/n)"))

#       Criação do comando em SQL para criação da Tabela
        col_command[i] = str(str(cols[i][0]) + " " + str(cols[i][1]))
        if cols[i][2] != "0":
            col_command[i] += str("(" + str(cols[i][2]) + ")")
        if cols[i][3] == "y":
            col_command[i] += str(" PRIMARY KEY")
        if cols[i][4] == "y":
            col_command[i] += str(" AUTO_INCREMENT")
        if cols[i][5] == "n":
            col_command[i] += str(" NOT NULL")

        print(col_command)

        if i < (int(col_num) -1):
            final_command += str(str(col_command[i]) + ", ")
        else:
            final_command += str(str(col_command[i]))

#   Confirma se a tabela está certa
    print("\n Será criada a tabela " + table_name + " com as colunas:\n")
    for i in range(0, int(col_num)):
        print(cols[i])
    print("\n O comando em SQL -> " + final_command + " <- Será executado.")
    certo = input("\n Está tudo certo? (y/n) \n")

#   Cria a Tabela
    if certo == "y":
        cursor = con.cursor()
        cursor.execute("CREATE TABLE " + str(table_name) + "(" + str(final_command) + ");")
        print("A Tabela foi criada com sucesso")

#   Se a tabela não estiver certa, reinicia tudo
    else:
        print("O processo será reiniciado")
        criarTabela()


def selecionarTabela():
    mode = input("\n Você deseja selecionar todos os dados de uma tabela, ou digitar um comando SQL do zero ? (Digite o número correspondente) \n 1 - Selecionar Dados \n 2 - Digitar comando SQL")
    if mode == 1:
        #MOSTRAR LISTA DE TABELAS
        cursor = con.cursor(named_tuple=True)
        cursor.execute("SHOW TABLES;")
        for row in cursor:
            print("Tabela " + str(row[0]))
        table_name = input("\n Essas são as tabelas disponíveis, qual delas você quer selecionar ?")

        #SELECIONAR TABELA
        cursor.execute("SELECT * FROM " + table_name)
        print("QUANTIDADE DE COLUNAS: " + str(len(cursor.description)))
        for row in cursor:
            print(row)
            print("==================================================")
            for i in range(int(len(cursor.description))):
                print(str(row[i]))
            print("==================================================")

    elif mode == 2:
        cursor = con.cursor()
        command = input("Digite o comando \n")
        cursor.execute(command)
        for row in cursor:
            print("==================================================")
            for i in range(int(len(cursor.description))):
                print(str(row[i]))
            print("==================================================")

def inserirValor():
    pass

def main():
    print(" ================== \n Qual ação você quer fazer? \n Criar uma Tabela - Digite c \n Selecionar uma Tabela - Digite s \n Sair - Digite sair \n ==================")
    op = input()
    if op == "c":
        criarTabela()
    elif op == "s":
        selecionarTabela()
    else:
        pass

if __name__ == "__main__":
    main()