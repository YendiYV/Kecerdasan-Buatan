import nltk
from nltk.stem import PorterStemmer 

ps = PorterStemmer()

kata = ["program", "programs", "programer","programing","programers"]

for k in kata:
	print(k, " : ", ps.stem(k))