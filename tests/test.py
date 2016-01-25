#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""

Test de `pyair` avec une configuration spéficique.
Un fichier de configuration au format JSON doit être préparer sur le modèle du fichier `config-test.json`.
La variable d'environnement `CFG_PYAIR_TEST` peut être définit pour l'utilisation d'un fichier spécifique.

"""


import os
import json
import six
import sys
import unittest
from pyair import xair
from pyair.reg import excel_synthese, print_synthese
import pandas as pd
pd.set_option('display.width', 200)


# Load configuration file
fncfg = os.environ['CFG_PYAIR_TEST'] \
    if 'CFG_PYAIR_TEST' \
    else os.path.join(os.path.dirname(__file__), 'config-test.json')
cfg = json.load(open(fncfg))
print("testing with %s configuration file..." % fncfg)


class TestXAIR(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout  # save stdout
        sys.stdout = six.StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout  # restore stdout

    def test_print_synthese(self):
        """ Test l'affichage des synthèses: vérification des informations statiques.
        """
        # Traitement
        xr = xair.XAIR(user=cfg['xair']['user'], pwd=cfg['xair']['pwd'], adr=cfg['xair']['adr'])
        for mesures in cfg['mes']:
            pol, mes = list(mesures.items())[0]
            fct = getattr(__import__('pyair.reg', fromlist=[pol.lower()]), pol.lower())  # import function
            freq = 'D' if pol in ['PM10', ] else 'H'
            df = xr.get_mesures(mes, debut=cfg['debut'], fin=cfg['fin'], freq=freq, brut=False)
            print_synthese(fct, df)
        xr.disconnect()

        # Analyse du traitement
        sys.stdout.seek(0)
        stdout = sys.stdout.read()
        self.assertTrue('XAIR: Connexion établie' in stdout)
        self.assertTrue('XAIR: Connexion fermée' in stdout)
        for pol in [k for e in cfg['mes'] for k in e.keys()]:
            self.assertTrue('Pour le polluant: %s' % pol in stdout)

    def test_synthese_excel(self):
        """ Test la création de fichier de synthèses au format Excel: vérification de la présence des fichiers
        """
        xr = xair.XAIR(user=cfg['xair']['user'], pwd=cfg['xair']['pwd'], adr=cfg['xair']['adr'])
        for mesures in cfg['mes']:
            pol, mes = list(mesures.items())[0]
            fct = getattr(__import__('pyair.reg', fromlist=[pol.lower()]), pol.lower())  # import function
            freq = 'D' if pol in ['PM10', ] else 'H'

            xls = os.path.join(cfg['excel_path'], 'stat_%s.xls' % pol)
            if os.path.isfile(xls):
                os.remove(xls)  # remove old file

            df = xr.get_mesures(mes, debut=cfg['debut'], fin=cfg['fin'], freq=freq, brut=False)
            excel_synthese(fct, df, xls)
            self.assertTrue(os.path.isfile(xls))
        xr.disconnect()


if __name__ == "__main__":
    unittest.main()
