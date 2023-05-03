#impor StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory=StemmerFactory()
stemmer= factory.create_stemmer()

sentence = "Pemrosesan bahasa alami (NLP) adalah sebuah teknologi machine learning yang memberi komputer kemampuan untuk meninterprestasikan , memanipulasi, dan memahami bahasa manusia."
output  = stemmer.stem(sentence)
print(output)

print(stemmer.stem("Teknologi AI dapat meniru-nirukan perilaku dan memudahkan aktivitas manusia."))