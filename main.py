import nmap

escaneo = nmap.PortScanner()

while True:
    print("[01] - Comprobar host activos en la red")
    print("[02] - Escanear red o equipos en profundidad")
    print("[00] - Salir")
    print("")
    elec = input("Elige una opcion: ")

    if elec == "0":
        print("Adiós!!")
        break

    elif elec == "1":
        target = input("Introduce la red objetivo: ")
        escaneo.scan(target, arguments="-T5 -sn")
        for ip in escaneo.all_hosts():
            print(ip)
            print("--------------")
    elif elec == "2":
        target = input("Introduce el equipo o la red a escanear: ")
        escaneo.scan(target, arguments="-sS -T5")
        for host in escaneo.all_hosts():
            for prot in escaneo[host].all_protocols():
                for port in escaneo[host][prot].keys():
                    print(
                        f"{host} | {prot} | {port} | {escaneo[host][prot][port]['state']}"
                    )
            print("--------------------")
