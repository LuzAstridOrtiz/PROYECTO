# Vamos a importar NLTK (Natural Language Toolkit) que nos va a ayudar a trabajar con lenguaje natural
import nltk
nltk.download('punkt_tab')

# Definir la ruta donde se almacenarán los datos descargados de NLTK
nltk.data.path.append(r'C:/Users/Astrid_Ortiz/AppData/Roaming/nltk_data')

# Descargamos la lista de palabras vacías stopwords que son palabras comunes como el, la, los, etc.
nltk.download('stopwords')

# Importar la función que divide un texto en palabras
from nltk.tokenize import word_tokenize

# Importar la lista de palabras vacías stopwords en español
from nltk.corpus import stopwords

# Imporar la herramienta para calcular la frecuencia de palabras en un texto
from nltk.probability import FreqDist

# Definimos un texto en español que queramos analizar

texto = """
Luz Astrid Ortiz Castaño, vive en la ciudad de Manizales. Le gusta ver series de epoca y leer. 
En el tiempo libre se dedica a su hijo Rafael. Como profesional es diseñadora visual y le gusta aprender
el uso de la tecnología y la inteligencia artificial.

José Ramírez, ING de sistemas del Quindío 
Especialista en gerencia de sistemas informáticos 
Teniene una hermosa familia una hija de 6 años.

Tatiana Carrillo, estudiante de marketing digital, es de Bogotá y actualmente vive en Villamaría 
con su esposo y su bebé de 2 años.


Juan Pablo Espinosa, es de Pereira y es Ingeniero de Sistemas de profesión. 
Actualmente trabaja en Claro, donde he tenido el privilegio de desempeñarse durante 18 años, 
creciendo tanto profesional como personalmente.

Es padre orgulloso de una hermosa hija llamada Gabriela, y comparte su hogar con ella, su madre,
 tres gatos y un perro. Aunque mi familia es pequeña, es su mayor tesoro, y cada día da gracias a Dios por tenerlos a su lado.
En los tiempos libres disfruta de actividades que le permitan desconectarse y recargar energías:
 ver series y anime, jugar videojuegos, ir al cine y escuchar música. 
 Es un apasionado por su carrera y disfruta aprender cosas nuevas constantemente,
  lo que me motiva a seguir creciendo y enfrentando nuevos retos.

"""

# Tokenización: Convertimos el texto en una lista de palabras individuales
palabras = word_tokenize(texto, language= 'spanish')

# Mostramos la lista de palabras obtenidas
print(palabras)

# Obtenemos la lista de palabras vacías en español, es decir, cargamos las stopwords en español. Aquí obtenemos una lista de palabras comunes en español que normalmente no necesistamos para el análisis. 
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras: eliminamos las stopwords y los signos de puntuación
# Recorremos cada palabra en una lista llamada palabras. Si la palabra no está en las stopwords y es una palabra real (sin números ni símbolos), la guardamos.

palabras_filtradas = [palabras for palabras in palabras if palabras.lower() not in stop_words and palabras.isalpha()]

# Mostramos la lista de palabras después del filtrado.
# Resultado: Nos quedamos solo con las palabras importantes.
print(palabras_filtradas)

# Calculamos la frecuencia de cada palabra en la lista filtrada
frecuencia_de_las_palabras = FreqDist(palabras_filtradas)

# Mostramos las 10 palabras más comunes y la cantidad de veces que aparecen
print(frecuencia_de_las_palabras.most_common(10))