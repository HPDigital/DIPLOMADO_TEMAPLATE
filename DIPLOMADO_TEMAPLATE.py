"""
DIPLOMADO_TEMAPLATE
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from openai import OpenAI
from docx import Document
import os, sys
from docxtpl import DocxTemplate as DocTemp
from docxtpl import InlineImage
from docx.shared import Cm, Inches, Mm, Emu


# In[2]:


client = OpenAI(api_key="YOUR_API_KEY_HERE")


# In[3]:


# Función para interactuar con ChatGPT y obtener el análisis del documento
def resumen(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales, manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.""".format(nombre_de_materia, nombre_de_materia)},

            {"role": "user", "content": """Podrías proporcionar un resumen detallado y académico para el curso titulado 
            {}, que será parte de un programa de maestría o diplomado? 
            Incluye el nombre del curso y un resumen general que explique el enfoque princial de la materia. 
            El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.La respuesta no debe exceder 50 tokens""".format(nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def temas(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales, manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.""".format(nombre_de_materia, nombre_de_materia)},

            {"role": "user", "content": """En el contexto de la elaboración de materias para maestrías y diplomados, 
            necesito un resumen exhaustivo y académico de los temas específicos que se cubrirán en el curso titulado 
            {}. Este curso está dirigido a profesionales y futuros líderes empresariales interesados en
            mejorara sus conociminetos academicos y profesionales. 
            Por favor, proporciona un listado detallado de los temas clave que se incluirán en el plan de estudios,
            asegurando que el contenido refleje la profundidad y seriedad adecuadas para un entorno académico avanzado. 
            El listado debe ser de cinco descripciones de temas clave para entender la materia. 
            Cada descripción debe ser concisa, no superar los 50 tokens y estar precedida por un punto.
            El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificia.La descripcion de cada tema no debe esceder los 30 tokens""".format(nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def competencia(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales,manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial""".format(nombre_de_materia, nombre_de_materia)},

            {"role": "user", "content": """Dentro del desarrollo de materias para maestrías y diplomados, 
            necesito conocer la competencia principal del curso {}. 
            Por favor, describe con un tono serio y académico la competencia clave que los estudiantes deben desarrollar 
            a través de este curso, resaltando su importancia para gerentes, empresarios y trabajadores en genral interezados
             en de mejorara sus destrezas academicas y profesionales.El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.La respuesta no debe exceder 50 tokens. 
            La respuesta debe empezar con verbo en infitivo""".format(nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def objetivo(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales,manteniendo un tono serio y académico que sea coherente con los estándares u
            niversitarios de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial""".format(nombre_de_materia, nombre_de_materia)},

            {"role": "user", "content": """En el contexto de la creación de cursos para maestrías y diplomados, 
            necesito una explicación detallada y con un enfoque académico sobre el objetivo principal del curso 
            titulado {}. Por favor, describe con profundidad 
            y seriedad académica el propósito central de esta materia, enfocándote en cómo pretende dotar 
            a los estudiantes de los fundamentos metodológicos necesarios para el desarrollo 
            y avance de la materia {}.El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.La respuesta no debe exceder 50 tokens""".format(nombre_de_materia,nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def saber(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales, manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            Tu respuesta debe ser directa y sin introducciones . 
            Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial""".format(nombre_de_materia, nombre_de_materia)},

            {"role": "user", "content": """En el contexto de desarrollo de cursos para maestrías y diplomados, 
            necesito una descripción detallada y académica de los elementos del saber que los estudiantes aprenderán 
            en el curso {}. 
            Por favor, proporciona una lista de cinco puntos que sea clara y precisa de los conocimientos fundamentales que se impartirán, 
            enfocándote en los aprendisages propios de materias como la de {} manteniendo un tono serio 
            y adecuado para un entorno académico.El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.La respuesta no debe exceder 50 tokens""".format(nombre_de_materia,nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def hacer(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales, 
            manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial""".format(nombre_de_materia, nombre_de_materia)},

            {"role": "user", "content": """En el marco de la creación de contenidos para maestrías y diplomados, 
            requiero una lista de cinco puntos que sea lista clara y precisa y en un tono académico sobre los elementos 
            del 'saber hacer', es decir lo que aprenderan a hacer concretamente que se enseñarán en el curso {}. 
            Por favor, incluye una explicación clara de las habilidades prácticas que los estudiantes adquirirán,
            al curasra la materia de {}. Todo en un contexto que refleje la seriedad y profundidad requeridas 
            en un entorno universitario avanzado.El tono debe ser formal y adecuado para un contexto universitario serio.
            En tu respuesta no debes utilizar formulas de cortecia.Tu respuesta debe ser directa y sin introducciones . 
            Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta generada por 
            Inteligencia Artificial. La descripcion de cada punto en la lista no debe exceder los 30 tokens""".format(nombre_de_materia, nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content
def ser(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales, manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial""".format(nombre_de_materia, nombre_de_materia)},

            {"role": "user", "content": """En el contexto de desarrollo de cursos para maestrías y diplomados, 
            necesito una descripción detallada y académica de los elementos del "saber ser" es decir esas competencias blandas 
            que los estudiantes aprenderán gracias a este curso {}. 
            Por favor, proporciona una lista de cinco puntos que sea clara y precisa de las capacidades blandas que se adquiriran, 
            enfocándote en los aprendisages propios de materias similares a la de {} manteniendo un tono serio 
            y adecuado para un entorno académico.El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial. La descripcion de cada punto en la lista no debe exceder los 30 tokens""".format(nombre_de_materia,nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def estrategias(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales, 
            manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial""".format(nombre_de_materia, nombre_de_materia)},
            {"role": "user", "content": """En el contexto de la planificación de cursos para maestrías y diplomados, 
            necesito recomendaciones sobre las estrategias de enseñanza más efectivas para el curso 
            titulado {}. Por favor, proporciona una lista de cinco puntos que sea clara y concreta de métodos 
            pedagógicos que faciliten la comprensión y aplicación de los conceptos relacionados con la materia de {}, 
            incluyendo tanto actividades presenciales como en línea. Busco estrategias que promuevan tanto 
            el aprendizaje individual como el colaborativo, y que sean adecuadas para un entorno académico serio 
            y profesional.El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.La descripcion de cada punto en la lista no debe exceder los 30 tokens""".format(nombre_de_materia,nombre_de_materia)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def recursos(nombre_de_materia):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """En el marco de la elaboración de un programa académico para maestrías
            y diplomados ofrecidos por una universidad, se está desarrollando un curso dedicado a {}, 
            Este curso tiene como objetivo proporcionar una base sólida en temas relacionado a {}, 
            Esta materia está dirigida a profesionales y futuros líderes que buscan adquirir competencias clave,
            con la finalidad impulsar y gestionar las empresa y el entorno empresarial. 
            La descripción del curso debe reflejar su relevancia y aplicación en contextos empresariales 
            y tecnológicos actuales, 
            manteniendo un tono serio y académico que sea coherente con los estándares universitarios 
            de enseñanza de posgrado. En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial""".format(nombre_de_materia, nombre_de_materia)},
            {"role": "user", "content": """En el contexto de la planificación de cursos para maestrías y diplomados, 
            necesito recomendaciones sobre las estrategias de enseñanza más efectivas para el curso 
            titulado {}. Por favor, proporciona una lista de cinco recomendaciones concretas de libros o articulos cientificos o publicacion y simialres, 
            que sirvan de respaldo pedagógicos para facilitar la comprensión y aplicación de los conceptos 
            relacionados con la materia de {}, Busco referencias en FORMATO APA la redaccion de ber ser formal adecuadas para un entorno académico serio 
            y profesional.El tono debe ser formal y adecuado para un contexto universitario serio.En tu respuesta no debes utilizar formulas de cortecia.
            tu respuesta debe ser directa y sin introducciones . Tu respuesta debe ser similar a la de un humano y que no se note que es una respuesta
            generada por Inteligencia Artificial.La descripcion de cada punto de recomendacion en la lista no debe exceder los 30 tokens""".format(nombre_de_materia,nombre_de_materia )},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def Desarrollo_materias(nombre_de_materia):
#     texto =""
    resumen_materia_1 = resumen(nombre_de_materia),
    detalle_temas_materia_1 = temas(nombre_de_materia),
    competencia_materia_1 = competencia(nombre_de_materia),
    objetivo_materia_1 = objetivo(nombre_de_materia),
    competencias_saber_materia_1 = saber(nombre_de_materia),
    competencias_hacer_materia_1 = hacer(nombre_de_materia),
    competencias_ser_materia_1 = ser(nombre_de_materia),
    competencias_ser_materia_1 = estrategias(nombre_de_materia),
    recursos_didacticos_materia_1 = recursos(nombre_de_materia),


    return (
    resumen_materia_1 ,
    detalle_temas_materia_1,
    competencia_materia_1,
    objetivo_materia_1,
    competencias_saber_materia_1,
    competencias_hacer_materia_1,
    competencias_ser_materia_1 ,
    competencias_ser_materia_1,
    recursos_didacticos_materia_1)


nombre_de_materia = "Fundamentos de Marketing"
A,B,C,D,E,F,G,H,I = Desarrollo_materias(nombre_de_materia)


path_in = r"C:\Users\HP\Desktop\PROPUESTAS DE DIPLOMADO\Propuesta DIPLOMADO A RAFEAL\PROPUESTAS DE DIPLOMADOS\Temp_prpouesta_diplomado.docx"
path_out= r"C:\Users\HP\Desktop\PROPUESTAS DE DIPLOMADO\Propuesta DIPLOMADO A RAFEAL\PROPUESTAS DE DIPLOMADOS\pruebas\{}.docx".format(nombre_de_materia)

img_in = r"C:\Users\HP\Pictures\Saved Pictures\VALUE_MAP.png"
doc = DocTemp(path_in)

context = {'nombre_materia_1':nombre_de_materia,
    'resumen_materia_1':A ,
    'detalle_temas_materia_1': B,
    'competencia_materia_1':C,
    'objetivo_materia_1':D,
    'competencias_saber_materia_1': E,
    'competencias_hacer_materia_1':F,
    'competencias_ser_materia_1': G,
    'competencias_ser_materia_1':H,
    'recursos_didacticos_materia_1': I}
doc.render(context)
doc.save(path_out)




# In[ ]:






if __name__ == "__main__":
    pass
