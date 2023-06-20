import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="clinica"
)

mycursor = mydb.cursor()

print(mydb)

clinica = []


def cadastrar_especialidade():
    print("cadastrando")
    dados = {"nome": input('Digite o nome')}
    valores = (dados["nome"], )
    sql = "insert into especialidades(nome) values (%s)"
    mycursor.execute(sql, valores) 
    mydb.commit()

def listar_especialidade():
    print("listar")
    mycursor.execute("SELECT * FROM especialidades")

    myresult = mycursor.fetchall()
    print('id, nome')
    for id, nome in myresult:
        print(f'{id} {nome}')

def deletar_especialidade():
    id = input("Digite o id")
    valores = (id, )
    sql = "DELETE FROM especialidades WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def atualizar_especialidade():
    id = input("Digite o id")
    nome = input("Digite o nome")
    valores = (id, nome, )

    sql = "UPDATE especialidades SET nome = %s WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

def cadastrar_medico():
    print('cadastrando')
    nome = input('Digite o nome')
    crm = input('Digite o crm')
    especialidades = input('Digite a especialidade')
    valores = (nome, crm, especialidades, )
    sql = "insert into medicos(nome, crm, id_especialidade) values (%s, %s, %s)"
    mycursor.execute(sql, valores) 
    mydb.commit()

def listar_medico():
    print("listar")
    mycursor.execute("SELECT * FROM medicos")

    myresult = mycursor.fetchall()
    print("id,nome, crm, id_especialidade ")
    for id, nome, crm, id_especialidade in myresult:
        print(f'{id}, {nome}, {crm} {id_especialidade}')


def deletar_medico():
    id = input("numero do id")
    valores = (id, )
    sql = "DELETE FROM medicos WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")


def atualizar_medico():
    id = input("Digite o id")
    nome = input("Digite o nome")
    valores = (id, nome, )

    sql = "UPDATE medicos SET nome = %s WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

def juntar_tabelas():
    sql= "SELECT \
        medicos.nome AS medico, \
        especialidades.nome AS especialidade \
        FROM medicos \
        INNER JOIN especialidades ON medicos.id_especialidade = especialidades.nome"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for id, nome in myresult:
        print(f"{id} {nome}")



def juntar_tabelas():
    sql= "SELECT \
        medicos.nome AS medico, \
        especialidades.nome AS especialidade \
        FROM medicos \
        INNER JOIN especialidades ON medicos.id_especialidade = especialidades.nome"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for id, nome in myresult:
        print(f"{id} {nome}")




while True:
    print('1.cadastrar medico')
    print('2.cadastrar especialidade')
    print('3.listar especialidade')
    print('4.listar medico')
    print('5.deletar medico')
    print('6.deletar especialidade')
    print('7.atualizar medico')
    print('8.atualizar especialidade')
    print('9.juntar tabelas')
    opcao = int(input('Qual das opções desejada?'))
    if opcao == 1:
        cadastrar_medico()
    elif opcao == 2:
        cadastrar_especialidade()
    elif opcao == 3:
        listar_especialidade()
    elif opcao == 4:
        listar_medico()
    elif opcao == 5:
        deletar_medico()
    elif opcao == 6:
        deletar_especialidade()
    elif opcao == 7:
        atualizar_medico()
    elif opcao == 8:
        atualizar_especialidade()
    elif opcao == 9:
        juntar_tabelas()
    else: 
        print('exit')
        break 