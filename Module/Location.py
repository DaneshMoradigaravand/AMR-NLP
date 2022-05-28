#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:39:53 2022

@author: moradigd
"""
import numpy as np
from geotext import GeoText
import pycountry_convert as pc

class Location:
    def __init__(self):
        self=None
   
    def geography(self, sentence):
        """
        search the pubmed database with a keyword 
        :param keyword: string
        :return: list of citties and countries
        """
        
        places = GeoText(sentence)
        output=[]
        output.append(np.unique(np.squeeze(places.cities)).tolist())
        output.append(np.unique(np.squeeze(places.countries)).tolist())
        return(output)

    def country_to_continent(list_of_countries):
        """
        search the pubmed database with a keyword 
        :param keyword: list of countries
        :return: list of matched continents
        """
        
        continents=[]
        for i in list_of_countries:
            try:
                country_code = pc.country_name_to_country_alpha2(i, cn_name_format="default")
                continents.append(pc.country_alpha2_to_continent_code(country_code))
            except:
                continents.append('Not found')
        return(continents)
    
    def extract_cities_countries(self, sentence):
        """
        :param tokenized sentence data frame
        :return: extract city names
        """
        places = GeoText(sentence)
        output=[]
        output.append(np.unique(np.squeeze(places.cities)).tolist())
        output.append(np.unique(np.squeeze(places.countries)).tolist())
        return(output)