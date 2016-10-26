import requests
import json

class datiRisorse:
    def __init__(self):
        self._token = None
        self._apiUrl = "https://api.scaleway.com/"
        self._listaRisorse = ["servers", "volumes", "ips"]

    def impostaToken(self, token):
        self._token = token

    def richiestaDati(self, risorsaRichiesta):
        jsonRichiesta = {}

        oggetoRichiestaApi = requests.get(self._apiUrl + risorsaRichiesta, headers = {"Content-Type" : "application/json", "X-Auth-Token" : self._token})

        jsonRichiesta["code"] = int(oggetoRichiestaApi.status_code)
        jsonRichiesta["headers"] = dict(oggetoRichiestaApi.headers)

        listaRisorsa = json.loads(oggetoRichiestaApi.text)
        jsonRichiesta[risorsaRichiesta] = listaRisorsa[risorsaRichiesta]

        return json.dumps(jsonRichiesta, indent=4)

    def richiestaTotale(self):
        jsonRichiesta = {}
        jsonRichiesta["code"] = 200
        for risorsa in self._listaRisorse:
            listaRichiesta = json.loads(self.richiestaDati(risorsa))
            if int(float(listaRichiesta["code"])) != 200:
                jsonRichiesta["code"] = None
            else:
                jsonRichiesta[risorsa] = listaRichiesta[risorsa]

        return json.dumps(jsonRichiesta, indent=4)
