import time
import spacy
from rank_bm25 import BM25Okapi
from tqdm import tqdm
import pandas as pd

df = pd.read_csv('data.csv')

nlp = spacy.load("es_core_news_sm")
text_list = df.text.str.lower().values
tok_text=[] # for our tokenised corpus

#Tokenising using SpaCy:
for doc in tqdm(nlp.pipe(text_list, disable=["tagger", "parser","ner"])):
   tok = [t.text for t in doc if t.is_alpha]
   tok_text.append(tok)

bm25 = BM25Okapi(tok_text)

query = "Flood Defence"
tokenized_query = query.lower().split(" ")

t0 = time.time()
results = bm25.get_top_n(tokenized_query, df.text.values, n=3)
t1 = time.time()

print(f'Searched 50,000 records in {round(t1-t0,3) } seconds \n')

for i in results:
   print(i)