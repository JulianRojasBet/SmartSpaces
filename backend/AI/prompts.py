from typing import List


RECOGNITION_PROMT = """\
Eres un experto en diseño de interiores y adecuacion de espacios para el alquiler de casas, habitaciones y apartamentos en plataformas como Airbnb o Booking
Tu tarea es la siguiente: dado una lista de comentarios en formato JSON sobre un espacio, indicar un listado conciso de mejoras puntuales a las imagenes en la plataforma iniciando la frase con un verbo en infinitivo.
Tambien entregar un resumen general de sugerencias segun los comentarios leidos con el fin de mejorar las imagenes en la plataforma. En un tono amigable.
Entregar maximo 10 recomendaciones.
La salida se espera en formato JSON tambien.
No incluir recomendaciones respecto a cosas ajenas al inmueble por ejemplo: la ubicacion, seguridad del sector, la actitud de los vecinos, etc.
Incluir recomendaciones respecto a los espacios interiores del inmueble: sala, comedor, baños, habitaciones, cocina, etc.
A continuacion unos ejemplos:

Ejemplo 1:
query : {"comments" : ["No me gustó que la cama ocupe tanto espacio","El baño no tenía papelera para las basuras", "un lugar muy agradable me gustó mucho", "la cama ocupa bastante espacio"]}
respuesta: {"improvements": ["reducir el tamaño de la cama", "añadir papelera al baño", "remplazar cama por camarote"], "summary": "La mayoria de clientes se quejan por el espacio de la cama, como recomendacion revisar la posibilidad de reducir el tamaño de la cama o sustituirlo por una opcion mas acorde al espacio como un camarote"}
Ejemplo 2:
query : {"comments" : ["Que tan agradable, volveria muchisimas veces más","Me encantaria volver, el host super recomendado", "excelente para parejas, muy buena ubicacion", "genial!"]}
respuesta: { "improvements": [], "summary" : "Genial! Los clientes se sienten satisfechos con tu inmueble, algunos creen que son excelentes para parejas, el pensar en adecuar este espacio a ser aun mas orientado a parejas puede ser una muy buena idea "}
A continuacion tu primera consulta:
query : {comments : %s}
respuesta: """


TRANSLATION_PROMT_SPANISH_TO_ENGLISH = """\
Traducir esto a Ingles: 
%s   
"""

TRANSLATION_PROMT_ENGLISH_TO_SPANISH = """\
Translate this into Spanish: 
%s   
"""

def create_suggestions_prompt(comments : List[str]):
    return RECOGNITION_PROMT % (str(comments),)

def create_translate_prompt_es_to_en(statement : str):
    return TRANSLATION_PROMT_SPANISH_TO_ENGLISH % (statement,)

def create_translate_prompt_en_to_es(statement : str):
    return TRANSLATION_PROMT_ENGLISH_TO_SPANISH % (statement,)