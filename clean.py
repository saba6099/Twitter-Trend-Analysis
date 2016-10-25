from nltk.corpus import stopwords 
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
def clean(doc):
	#doc1 = pos_tag(doc.split())
	#print(doc1)
	#doc2 = [word for word,pos in doc1 if (pos == 'NNP' or pos=='NN')]
    stop_free = " ".join([i for i in doc2 if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
#with open('doc1','r') as d1:
doc1="Learning from Teaching in Literacy Education: New Perspectives on Why on earth should or would Dublin want to.Policies must be designed before execution ."
doc2 = "It has been a very long since Modi has started the swachchh bharat abhyan We have a big library of books for science, history, geography etc "
doc3 = "Lot of money has been wasted in government's useless policies There is a big need of cleanliness in india"
'''dc1 = pos_tag(doc1.split())
dc2 = pos_tag(doc2.split())
dc3 = pos_tag(doc3.split())
#print(dc1+dc2+dc3)
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]

d1 = [word for word,pos in dc1 if (pos == 'NNP' or pos=='NN')]
d2 = [word for word,pos in dc2 if (pos == 'NNP'or pos =='NN')]
d3 = [word for word,pos in dc3 if (pos == 'NNP' or pos =='NN')]
print(doc1+doc2+doc3)
#doc_clean=clean(d1)'''

doc_complete = [doc1, doc2, doc3]
doc_clean = [clean(doc).split() for doc in doc_complete] 
dictionary = corpora.Dictionary(doc_clean)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)
print(ldamodel.print_topics(num_topics=3, num_words=3))
