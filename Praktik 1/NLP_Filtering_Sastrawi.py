import nltk
import string

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory,StopWordRemover, ArrayDictionary
from nltk.tokenize import word_tokenize

stop_factory= StopWordRemoverFactory().get_stop_words() #load deafult stopword
more_stopword = ['daring','online']
kalimat = "Yendi kerap melakukan transaksi rutin secara daring atau online. Menurut Yendi belanja online lebih praktis & murah."
kalimat = kalimat.translate(str.maketrans('','', string.punctuation)).lower()
data=stop_factory + more_stopword

dictionary= ArrayDictionary(data)
str= StopWordRemover(dictionary)
tokens= nltk.tokenize.word_tokenize(str.remove(kalimat))

print(tokens)