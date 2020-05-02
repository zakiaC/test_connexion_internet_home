# -*- coding: utf-8 -*-

import speedtest

serveur = speedtest.Speedtest()
serveur.get_best_server()
serveur.download()
serveur.upload()
resultat  = serveur.results.dict()
print(resultat["download"], resultat["upload"], resultat["ping"])
