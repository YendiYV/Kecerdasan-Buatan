import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

kalimat = "Yendi kerap melakukan transaksi rutin secara daring atau online. Menurut Yendi belanja online lebih praktis & murah."
hasil = stemmer.stem(kalimat)
print(hasil)