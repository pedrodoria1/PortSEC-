from random import choice
import sqlite3

conn = sqlite3.connect('portas.db')
cursor = conn.cursor()
nome_tabela = 'Protocolos'

score = 0

def question():
    global score
    protocols = ['ftp','ssh','telnet','snmp','rdp','https','http','smtp']
    ports = [21,22,23,161,3389,443,8080,25]
    ftp = [protocols[0]] + [str(ports[0])]
    ssh = [protocols[1]] + [str(ports[1])]
    telnet = [protocols[2]] + [str(ports[2])]
    snmp = [protocols[3]] + [str(ports[3])]
    rdp = [protocols[4]] + [str(ports[4])]
    https = [protocols[5]] + [str(ports[5])]
    http = [protocols[6]] + [str(ports[6])]
    smtp = [protocols[7]] + [str(ports[7])]
    consolidated = [ftp,ssh,telnet,snmp,rdp,https,http,smtp]
    randomPort = choice(consolidated)
    print('Qual o número da porta equivalente ao protocolo: {}'.format(randomPort[0]))
    answer = int(input('Digite: '))
    if str(answer) == randomPort[1]:
        print('RIGHT!')
        score = score + 1
    else:
        print('WRONG!')
        score = score - 1
    print('Resposta: Protocolo {} | Porta {}'.format(randomPort[0],randomPort[1]))
    print('Pontuação: {}'.format(score))
    question()

question()
conn.close