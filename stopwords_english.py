# importar la libreria nltk
import nltk
# desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords_english = stopwords.words('english')
#imprimir las stopwords
print(lista_stopwords_english)