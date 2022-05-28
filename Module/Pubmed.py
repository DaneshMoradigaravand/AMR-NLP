#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:31:38 2022

@author: moradigd
"""
from Bio import Entrez
class PubMedArticle:
    def __init__(self,email):
        self.email=None
            
    def search(self,  keyword, count):
        """
        search the pubmed database with a keyword 
        :param keyword: string
        :param count: int
        :return: list
        """
        
        Entrez.email = self.email
        
        if not isinstance(keyword, str): raise ValueError('search keyword is not a string')
        if not isinstance(count, int): raise ValueError('search keyword is not an integer')

        search_results = Entrez.esearch(db='pubmed', sort='time', retmax=str(count), retmode='xml', term=keyword)
        search_results_imported = Entrez.read(search_results)
        return search_results_imported
    
    def fetch_details(self,id_list):
        """
        returns details of papers given an list of PubMed id list
        :param id_list
        :return: list
        """
        from Bio import Entrez
        ids = ','.join(id_list)
        Entrez.email = self.email
        handle = Entrez.efetch(db='pubmed',retmode='xml',id=ids)
        results = Entrez.read(handle)
        return results