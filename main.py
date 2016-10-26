import leggiRisorse
import os
import json

leggiRisorse = leggiRisorse.datiRisorse()
leggiRisorse.impostaToken("Inserisci qui il tuo token")

listaOpzioni = [ "quit",
            "help",
            "all",
            "source"]

dettagliOpzioni = """
{0}\t Esci
{1}\t Questa schermata
{2}\t Tutte le risorse
{3}\t Tutte le risorse in JSON
""".format(*listaOpzioni)


def listaRisorse():

    jsonRisorse = json.loads(leggiRisorse.richiestaTotale())
    if int(float(jsonRisorse["code"])) == 200:

        print("Servers:")
        if len(jsonRisorse["servers"]) > 0:
            for server in jsonRisorse["servers"]:
                dettagliServer = server["name"]+"\t"+server["state"]
                if server["public_ip"] != None:
                    dettagliServer += "\t"+server["public_ip"]["address"]
                if server["volumes"] != None:
                    for chiave in server["volumes"]:
                        dettagliServer += "\t"+server["volumes"][chiave]["name"]
                print(dettagliServer)
        else:
            print("Vuoto")

        print("Volumes:")
        if len(jsonRisorse["volumes"]) > 0:
            for volume in jsonRisorse["volumes"]:
                dettaglioVolume = volume["name"]+"\t"+str(volume["size"]/1000000000)+" GB"
                if volume["server"] != None:
                    dettaglioVolume += "\t"+volume["server"]["name"]
                print(dettaglioVolume)
        else:
            print("Vuoto")

        print("Ips:")
        if len(jsonRisorse["ips"]) > 0:
            for ip in jsonRisorse["ips"]:
                dettagliIp = ip["address"]
                if ip["server"] != None:
                    dettagliIp += "\t"+ip["server"]["name"]
                print(dettagliIp)
        else:
            print("Vuoto")


def main():

    while True:
        inCmd = str(input("Per la lista delle opzioni \'help\': "))

        if inCmd == listaOpzioni[0]:
            break
        elif inCmd == listaOpzioni[1]:
            print(dettagliOpzioni)
        elif inCmd == listaOpzioni[2]:
            listaRisorse()
        elif inCmd == listaOpzioni[3]:
            print(leggiRisorse.richiestaTotale())


if __name__ == '__main__':
    main()
