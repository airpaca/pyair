#!/usr/bin/python
# -*- coding: UTF-8 -*-


import date
import geo
import plot
import utils
import xair
import reg


__version__ = "2.2"
__author__ = "Lionel Roubeyrie"
__email__ = "lroubeyrie@limair.asso.fr"
__all__ = ['xair', 'date', 'plot', 'utils', 'geo', 'reg', 'meteo_france']
__license__ = "GPL"

__changes__ = {
    '2.2': """ - Ajout de utils.pivotCSV2 permettant de pivoter des données en gardant certaines lignes et/ou colonnes;
     - xair.XAIR.liste_campagnes : tri des campagnes par date début par défaut;
     - ajouts de sites_from_df et sites_from_csv au module geo"""}