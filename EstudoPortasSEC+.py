from random import choice
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_PORTAS(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM PORTAS")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"C:\sqlite\db\portlist.db"

    conn = create_connection(database)
    with conn:

        print("2. Query all tasks")
        select_all_PORTAS(conn)


if __name__ == '__main__':
    main()

protocols = ['ftp','ssh','telnet','snmp']
ports = [21,22,23,161]
ftp = [protocols[0]] + [str(ports[0])]
ssh = [protocols[1]] + [str(ports[1])]
telnet = [protocols[2]] + [str(ports[2])]
snmp = [protocols[3]] + [str(ports[3])]
consolidated = [ftp,ssh,telnet,snmp]
randomPort = choice(consolidated)
print('Qual o número da porta equivalente ao protocolo: {}'.format(randomPort[0]))
answer = int(input('Digite: '))
if str(answer) == randomPort[1]:
    print('RIGHT!')
else:
    print('WRONG!')
print('Resposta: Protocolo {} | Porta {}'.format(randomPort[0],randomPort[1]))


