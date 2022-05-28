#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:33:21 2022

@author: moradigd
"""
import spacy
import numpy as np
import spark

class NLP:
    def __init__(self,max_length):
        self.max_length=max_length
        self=None
    
    def extract_sentence(self, text):
        """
        :param text 
        :return: list of sentences
        """
        import spacy
        nlp = spacy.load("en")
        nlp.max_length = self.max_length
        nlp_object=nlp(text)
        return(list(map(lambda x: str(x),list(nlp_object.sents))))
    
    def tokenize_senetence_entities(self, sentence_list):
        """
        :param text 
        :return: list of sentences
        """
        nlp= spacy.load('en_core_web_sm')
        doc = nlp(sentence_list)
        return(doc.ents)
    
    def delete_stopwords(self,text, TokenizedSetenceList):
        """
        :param text 
        :return: list of sentences
        """
        tokens = [TokenizedSetenceList.text for token in text if not token.is_stop]
        return(' '.join(tokens))
        
    def index_sentence(self, sentence_list):
        """
        :param text 
        :return: indexed sentences
        """
        return list(zip(np.arange(2), sentence_list))

    def create_spark_data_frame(self, index_sentence_list):
        """
        :param indexed sentences 
        :return: spark dataframe
        """
        return spark.createDataFrame([(float(tup[0]), tup[1]) for tup in index_sentence_list], ["id", "sentence"])

    def tokenizer_spark(self, sentenceDataFrame):
        """
        :param spark dataframe 
        :return: tokenized sentence data frame 
        """
        from pyspark.ml.feature import Tokenizer
        tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
        return tokenizer.transform(sentenceDataFrame).select("words")

    def remover_stop_word_spark(self, TokenizedSentenceDataFrame):
        """
        :param tokenized sentence data frame
        :return: remove stop words
        """
        from pyspark.ml.feature import StopWordsRemover
        remover = StopWordsRemover(inputCol="words", outputCol="filtered")
        return remover.transform(TokenizedSentenceDataFrame).select("filtered")
    
    def get_word2vec_freq(self, gesim_model):
        
        w2c = dict()
        for item in gesim_model.wv.vocab:
            w2c[item]=gesim_model.wv.vocab[item].count
        return