#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:24:12 2022

@author: moradigd
"""
import pandas as pd
import numpy as np
import spacy
import os

from Modules.Location import Location
from Modules.NLP import NLP
from Modules.Plot import Plot
from Modules.Unsupervised import Unsupervised
from Modules.Pubmed import Pubmed
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
CURRENT_PATH =os.path.dirname(os.path.realpath(__file__))

def main():
    results = Pubmed.search('antibiotic resistance',1000000)
    res=[results['IdList'][i:i + 1000] for i in range(0, len(results['IdList']), 1000)]
    ids=[]
    for j in range(0,len(res)):
        papers = Pubmed.fetch_details(res[j])
        print('iteration {:.2f}%'.format(100*j/len(res)))
        print('number of ids {}'.format(len(ids)))
        for k in range(len(res[j])):
            try:
                instance = papers['PubmedArticle'][k]['MedlineCitation']['Article']
                instance_text=instance['Abstract']['AbstractText']
                geo_check=Location.geography(instance_text[0])
                if any(geo_check):
                    print(geo_check)
                    ids.append(res[j][k])
            except Exception:
                print(Exception)
                pass

    #extract metadata
    inp=pd.read_csv(os.path.join(CURRENT_PATH, "ids.csv"))
    ids=inp.iloc[:,1].values.tolist()
    ids=list(map(lambda x : str(x), ids))
    res=[ids[i:i + 1000] for i in range(0, len(ids), 1000)]

    nlp = spacy.load("en")
    loc_pub=[]
    year_pub=[]
    title_pub=[]
    len_pub=[]
    text_pub=[]
    for j in range(0,len(res)):
        papers = Pubmed.fetch_details(res[j])
        print('iteration {:.2f}%'.format(100*j/len(res)))
        for k in range(len(res[j])):
        
            try:
                instance = papers['PubmedArticle'][k]['MedlineCitation']['Article']
                instance_text=instance['Abstract']['AbstractText']
                len_pub.append(len(str(instance['Abstract']['AbstractText'])))
                year_pub.append(instance['ArticleDate'][0]['Year'])
                title_pub.append(instance['ArticleTitle'])
            
                print(k)
                print(instance['ArticleTitle'])
            
                doc=str(instance_text[0])
                text = nlp(doc)
                text=NLP.delete_stopwords(text)

                geo_check=Location.geography(str(text))
            
                loc_pub.append(geo_check)
                text_pub.append(str(text))
            
                print(geo_check)
            except Exception:
                pass

    city=pd.DataFrame(list(map(lambda x: np.squeeze(loc_pub[x][0]), np.arange(len(loc_pub)))),columns=['city'])
    country=pd.DataFrame(list(map(lambda x: np.squeeze(loc_pub[x][1]), np.arange(len(loc_pub)))),columns=['country'])
    year=pd.DataFrame(year_pub,columns=['year'])
    title=pd.DataFrame(title_pub,columns=['title'])
    text=pd.DataFrame(text_pub,columns=['text'])
    output=pd.concat([city,country, year, title, text], join="inner", axis=1)


    #read curated data and plot
    import os 
    import pandas as pd
    df=pd.read_csv(os.path.join(CURRENT_PATH, "ids_NLP.csv"))


    #attach continents
    df['continents']=Location.country_to_continent(df.country.values)
    df=df[df.continents != 'Not found']
    df=df.reset_index()

    df.continents.value_counts()
    df.year.value_counts()

    #replace countries with continents
    continents_full_name={'AF':'Africa', 'AS':'Asia', 'EU':'Europe', 'NA':'NorthAmerica', 'OC':'Oceania', 'SA':'SouthAmerica'}
    for i in range(df.shape[0]):
        df.text[i]=df.text[i].replace(df.country[i], continents_full_name[df.continents[i]])

    #plot year versus continent
    input_table=pd.crosstab(df.continents,df.year)
    Plot.plot_grouped_barplot(input_table)

    aggregated_text_by_year=df.groupby('year')['text'].apply(' '.join).reset_index()
    years=list(set(aggregated_text_by_year.year))
    years.sort()
    years=[2015, 2016, 2017, 2018, 2019]
    for i in years:
        print("\n")
        print(i)
        text_holder=aggregated_text_by_year[aggregated_text_by_year.year==i].text.values[0]
        
        nlp_op=NLP(1500000)
        sentence_holder=nlp_op.extract_sentence(text_holder)

        tokenized_sentences_holder= [word_tokenize(i) for i in sentence_holder]
        print(len(tokenized_sentences_holder))
        tokenized_sentences_holder= [i for i in tokenized_sentences_holder if len(i)>5]
        print(len(tokenized_sentences_holder))

        model = Word2Vec(tokenized_sentences_holder, min_count=3)
    
        embeddings=model.wv[model.wv.vocab]
        embeddings_reduced=pd.DataFrame(list(zip([*model.wv.vocab.keys()], Unsupervised().PCA(embeddings).fit_PCA(embeddings)[:,0],Unsupervised().PCA(embeddings).fit_PCA(embeddings)[:,1])))
        embeddings_reduced['freq']=NLP.get_word2vec_freq(model)['freq']
        embeddings_reduced.to_csv(os.path.join(CURRENT_PATH+ str(i) +".csv"))

if __name__ == "__main__":
    main()