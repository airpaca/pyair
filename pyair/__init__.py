#!/usr/bin/python
# -*- coding: UTF-8 -*-


from . import date
from . import reg
from . import stats
from . import xair


__version__ = "3.2.3"
__author__ = "Lionel Roubeyrie"
__email__ = "lroubeyrie@limair.asso.fr"
__all__ = ['date', 'reg', 'stats', 'xair']
__license__ = "GPL"
__changes__ = {
    '3.2.3': """- Correction bug pour extraction avec des fréquences différentes de l'horaire.""",
    '3.2.2': """- Ajout de l'option verbose.""",
    '3.2.1': """- Ajout du code public des stations.""",
    '3.2.0': """- Compatibilité avec Python 3.x""",
    '3.1.0': """- Evolution de la méthode 'list_mesures' pour la prise en compte des différentes critères de sélection des mesures.""",
    '3.0.0': """- Separation des modules en packages distincts : pyair, pyair_utils
    - Nettoyage des fichiers pour etre conforme avec PEP8
    - ajout de xair.indice_et_ssi pour récupérer les sous-indices et les polluants faisant l'indice global""",
    '2.2': """ - Ajout de utils.pivotCSV2 permettant de pivoter des données en gardant certaines lignes et/ou colonnes;
     - xair.XAIR.liste_campagnes : tri des campagnes par date début par défaut;
     - ajouts de sites_from_df et sites_from_csv au module geo"""
}
