'''
Universidad del Valle de Guatemala
Sistema de telecomunicaciones 1
Proyecto Aplicación de DNS
Luis Gómez 18291
Helder Ovalle 18349
'''

#Librerias
import socket
from dnslib import DNSRecord

opcion=0
while opcion!=2: #Mientras no sea la opcion de salir
    print("OPCIONES\n1. DNS\n2. Salir")
    opcion = input("Escoga una opcion (1-2):\n")
    while not opcion.isdigit(): #Mientras la opcion no sea digito
          opcion = input("Escoga una opcion (1-2):\n") #Vuelve a preguntar
    opcion = int(opcion) #Se vuelve entera la variable
    if opcion == 1:
        # DNS
        serverName = input("Ingrese Servidor DNS a consultar:\n") #Servidor de DNS
        serverPort = 53 #puerto DNS

        forward_addr = (serverName, serverPort)

        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #udp
            qname = str(input("Ingrese el Dominio:\n")) #Mensaje del DNS # query
            registro = str(input("Ingrese el registro:\n")) #ingresar registro
            q = DNSRecord.question(qname,registro)
            client.sendto(bytes(q.pack()), forward_addr)
            data, _ = client.recvfrom(2048)
            d = DNSRecord.parse(data)
            print(str(d.rr[0].rdata)+"\n") # imprimir la informacion
        except IndexError:
            print("No existe el registro: "+registro)

    elif opcion == 2:
            print("Gracias por utilizar el programa\n")
    else:
            print("Opcion no valida\n")
