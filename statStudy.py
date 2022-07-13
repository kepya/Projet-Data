import numpy as np
# JSON lib
import json


class StatStudy:

    def realise(self, distance):
        # Moyenne de la série
        moyenne = np.mean(distance)
        # Minimum
        minimum = min(distance)
        # Maximum
        maximum = max(distance)
        # Médiane
        mediane = np.median(distance)
        # 1er quartile
        quartile_1 = np.percentile(distance, 25)
        # 2ème quartile
        quartile_2 = np.percentile(distance, 50)
        # 3eme quartile
        quartile_3 = np.percentile(distance, 75)
        # Variance
        variance = np.var(distance)
        # Ecart-type
        ecart_type = np.std(distance)

        # Affichage des résultats en console
        print('\n')
        print("La moyenne de la série est :", moyenne)
        print("Le minimum de la série est :", minimum)
        print("Le maximum de la série est :", maximum)
        print("La médiane de la série est :", mediane)
        print("Le 1er quartile de la série est :", quartile_1)
        print("Le 2ème quartile de la série est :", quartile_2)
        print("Le 3è quartile de la série est :", quartile_3)
        print("La variance de la série est :", variance)
        print("L\'écart type de de la série est :", ecart_type)
        print('\n')

        data = {
            str('La moyenne de la série'): moyenne,
            str('Le minimum de la série'): minimum,
            str('Le maximum de la série'): maximum,
            str('La médiane de la série'): mediane,
            str('Le 1er quartile de la série'): quartile_1,
            str('Le 2ème quartile de la série'): quartile_2,
            str('Le 3è quartile de la série'): quartile_3,
            str('La variance de la série'): variance,
            str('L\'écart type de de la série'): ecart_type,
        }

        with open("./dataset/stats/resultOfStatistiqueDescriptive.json", 'w') as outfile:
            json.dump(data, outfile)
