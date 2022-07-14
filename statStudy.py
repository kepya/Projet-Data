from matplotlib.pyplot import title
import numpy as np
# JSON lib
import json


class StatStudy:

    def realise(self, value, fileName):
        try:
            # Moyenne de la serie
            moyenne = np.mean(value)
            # Minimum
            minimum = min(value)
            # Maximum
            maximum = max(value)
            # Médiane
            mediane = np.median(value)
            # 1er quartile
            quartile_1 = np.percentile(value, 25)
            # 2ème quartile
            quartile_2 = np.percentile(value, 50)
            # 3eme quartile
            quartile_3 = np.percentile(value, 75)
            # Variance
            variance = np.var(value)
            # Ecart-type
            ecart_type = np.std(value)

            # Affichage des résultats en console
            print('\n')
            print('*********************************Stat of ' +
                  fileName + "******************************")
            print("La moyenne de la serie est :", moyenne)
            print("Le minimum de la serie est :", minimum)
            print("Le maximum de la serie est :", maximum)
            print("La médiane de la serie est :", mediane)
            print("Le 1er quartile de la serie est :", quartile_1)
            print("Le 2ème quartile de la serie est :", quartile_2)
            print("Le 3è quartile de la serie est :", quartile_3)
            print("La variance de la serie est :", variance)
            print("L\'écart type de de la serie est :", ecart_type)
            print('\n')

            self.report('*********************************Stat of ' +
                        fileName + "******************************", "reportStat")
            self.report("La moyenne de la serie est : " +
                        str(moyenne), "reportStat")
            self.report("Le minimum de la serie est : " +
                        str(minimum), "reportStat")
            self.report("Le maximum de la serie est : " +
                        str(maximum), "reportStat")
            self.report("La médiane de la serie est : " +
                        str(mediane), "reportStat")
            self.report("Le 1er quartile de la serie est : " +
                        str(quartile_1), "reportStat")
            self.report("Le 2ème quartile de la serie est : " +
                        str(quartile_2), "reportStat")
            self.report("Le 3è quartile de la serie est : " +
                        str(quartile_3), "reportStat")
            self.report("La variance de la serie est : " +
                        str(variance), "reportStat")
            self.report("L\'écart type de de la serie est :" +
                        str(ecart_type), "reportStat")
            self.report("\n", "reportStat")
            self.report("\n", "reportStat")

            data = {
                str('La moyenne de la serie'): moyenne,
                str('Le minimum de la serie'): minimum,
                str('Le maximum de la serie'): maximum,
                str('La médiane de la serie'): mediane,
                str('Le 1er quartile de la serie'): quartile_1,
                str('Le 2ème quartile de la serie'): quartile_2,
                str('Le 3è quartile de la serie'): quartile_3,
                str('La variance de la serie'): variance,
                str('L\'écart type de de la serie'): ecart_type,
            }

            with open("./dataset/stats/json/ " + str(fileName) + ".json", 'w') as outfile:
                json.dump(data, outfile)

        except(OSError, IOError) as e:
            print("Error: " + str(e) + '!')

    def report(self, report, filename):
        try:
            report_file = open("./dataset/stats/textes/" +
                               str(filename) + ".txt", "a")
            report_file.write(report + "\n")
        except(OSError, IOError) as e:
            print("Error: " + str(e) + '!')
