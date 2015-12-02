#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from pyair import xair
from pyair.reg import excel_synthese, print_synthese, o3, so2, no2, pm10
import pandas as pd
pd.set_option('line_width', 200)


DEBUT = '2012-01-01'
FIN = '2012-12-31'
USER = 'XXXXX'
PWD = 'XXXXX'
ADR = '192.168.1.1'
PATH = '/tmp/'  # chemin où enregistrer les fichiers excel

MES = [
    [so2, ['SO2_FO', 'SO2_GA', 'SO2_IP', 'SO2_PR'], 'H', 'reg_SO2.xls'],
    [no2, ['NO2_AINE', 'NO2_DA', 'NO2_FO', 'NO2_HU', 'NO2_IP', 'NO2_NI', 'NO2_PR', 'NO2_VI'], 'H', 'reg_NO2.xls'],
    [pm10, ['PSC_AI', 'PSC_DA', 'PSC_FO', 'PSC_GA', 'PSC_HU', 'PSC_IP', 'PSC_NI', 'PSC_PR', 'PSC_IP'], 'D', 'reg_PM10.xls'],
    [o3, ['O3_DA', 'O3_FON', 'O3_GAR', 'O3_HUG', 'O3_MER', 'O3_NI', 'O3_PRE'], 'H', 'reg_O3.xls'],
]


def run():
    xr = xair.XAIR(user=USER, pwd=PWD, adr=ADR)
    for fct, mes, freq, xls_name in MES:
        df = xr.get_mesures(mes, debut=DEBUT, fin=FIN, freq=freq, brut=False)
        excel_file = os.path.join(PATH, xls_name)
        excel_synthese(fct, df, excel_file)
        print_synthese(fct, df)
    xr.disconnect()

if __name__ == "__main__":
    run()
