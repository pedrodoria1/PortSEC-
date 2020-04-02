from random import choice

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


