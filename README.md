# Systematic Analysis of Global Patterns of the Epidemiology of Antimicrobial Resistance from Literature using Natural Language Processing Approaches

A library of tools to curate the embeddings and extract patterns from medical literature on AMR

## Table of contents
1. [Citation](#citation)
2. [Abstract](#content)
3. [Repository](#repository)
4. [Contact](#contact)

----

### Citation <a name="citation"></a>

The repository is part of the following working manuscript 

*Systematic Analysis of Global Patterns of the Epidemiology of Antimicrobial Resistance from Literature using Natural Language Processing Approaches.*

Citation will be added upon the final publication of the manuscript.

----

### Abstract <a name="content"></a>
Antimicrobial resistance (AMR) is a global health issue expected to become the leading cause of death worldwide in the coming years. Although AMR is an intrinsic characteristic of micro-organisms, the rise and prevalence of AMR in clinically relevant micro-organisms has accelerated due to several factors, such as the inappropriate use of antimicrobial agents.

In this study, we systematically analysed the wealth of information in the scientific literature to identify the socio-economic factors that influence the presence of a given country in the epidemiological AMR-related literature. To this end, we used natural language processing (NLP) and other machine learning methods and integrated antibiotic consumption data and socio-economic data from different sources.

Our results reveal that the country's consumption of antimicrobials and gross national income are the most explanatory factors for the amount of reports from each country. We also identified changes in the use of antibiotic classes across the years and that the rise of livestock antimicrobials consumption in a given country was significantly linked with the rise of the AMR literature of that country. This study is the first text-only driven AMR analysis and highlights the significance of public literature in inferring latent knowledge on AMR-related epidemiological factors. 

----
### Repository <a name="repository"></a>

The repository includes script to compute word embeddings for the key words extracted from scientific literature corpus. The package has following components:

#### Fetching data (Pubmed.py)
Here we use the Bio library to systematically fetch abstracts containing the term antibiotic from the PubMed repository. 

#### Preprocessing and word embedding calculation (NLP.py)
After creating a corpus of abstract texts, we cleaned the data using NLP tools implemented in ***gensim***, ***nLTK*** and ***spaCy*** libraries. The preprocessing includeds following steps:

1- removing stop words 

2- removing special characters

3- lemmatization 

We used the word2vec function in the ***gensim*** library to compute the word2vec embedding for antibiotic and location terms. 

#### Geographical annotation (Location.py)
Here we extract geographical attributes, e.g. cities and countries, in the text and annotate them with ***geotext*** library. To study country-wide patterns, we replaced the terms with their correspondind country attribute.  

#### Clustering and plotting (Unsupervised.py and Plot.py)
We employed unsupervised methods, e.g. ***t-SNE*** and ***PCA***, to reduce dimensions and visulaize word embeddings. 

----
### Contact <a name="contact"></a>
For queries, please contact [Danesh Moradigaravand](mailto:d.moradigaravand@bham.ac.uk?subject=[GitHub]), Data-Driven Microbiology lab, Center for Computational Biology, University of Birmingham. 
 


-----

