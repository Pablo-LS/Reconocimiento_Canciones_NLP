from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import speech_recognition as sr
from speech_recognition import AudioData
import time

# -------------------------------------------------------------------FUNCIONES-------------------------------------------------------------------

# Funcion para crear el diccionario separando las letras de las canciones en trozos
def generar_diccionario(letras):
    crear_diccionario = {}
    
    for nombre, letra in letras.items():
        lineas = letra.split("\n")
        for i, linea in enumerate(lineas):
            key = f"{nombre} {i+1}"
            crear_diccionario[key] = linea.strip()
    
    return crear_diccionario

# Función para buscar clave de cada valor:
def BuscaClave():
    clave_encontrada = None
    for clave, valor in nombre_y_cancion.items():
        if valor == letrasSimilitud[0]:
            clave_encontrada = clave
            break

    # Verificar si la clave se encontró o no
    if clave_encontrada is not None:
        print(f"La canción es: {clave_encontrada}")
    else:
        print(f"No se encontró ninguna clave para el valor {letrasSimilitud[0]}")

# Función detector de texto en directo
def transcribe_audio_to_text():
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()

    # Usar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Por favor, canta la letra de una canción:")

        # Ajustar el reconocedor al nivel de ruido ambiental
        recognizer.adjust_for_ambient_noise(source, duration=1)
       
        # Escuchar el audio del micrófono
        audio_data = recognizer.listen(source)
       
        try:
            # Utilizar el reconocedor de Google para convertir el audio a texto
            text = recognizer.recognize_google(audio_data, language="es-ES")
            print("Texto reconocido: " + text)
            return text
        except sr.UnknownValueError:
            # Error: el reconocedor no entendió el audio
            print("No se pudo entender el audio.")
        except sr.RequestError as e:
            # Error: no se pudieron enviar los datos a Google
            print(f"No se pudo solicitar resultados de Google Speech Recognition; {e}")


# -------------------------------------------------------------------CANCIONES-------------------------------------------------------------------

# Introduce el nombre y la letra de las canciones que quieres comprobar aquí:
letras_canciones = {
    "Zapatillas - El Canto Del Loco": """Estoy cansado de salir de noche y ver siempre la misma gente estoy flipando de que la gente se invente, cuente y luego reinvente
Apoltronado en el sofá de mi casa, vente, se está caliente amaestrados vamos al mismo sitio todos, aunque luego ni entres
Alucinando de que me miren de arriba abajo como un delincuente intoxicado de que me pongan esa puta música indiferente
Quiero entrar en tu garito con zapatillas que no me miren mal al pasar estoy cansado de siempre lo mismo la misma historia y quiero cambiar
me da pena tanta tontería quiero un poquito de normalidad pero a ver mírame y dime tronco no veo mi sitio y no puedo aparcar
Estoy muy harto de que me digan si no estás en lista, no puedes pasar solo entran cuatro tenemos zona super mega guay y nunca la verás
Abarrotado hay aforo limitado y ahora toca esperar y nos han multado y tu coche se lo ha llevado la grúa municipal
Ya has aparcado el coche y ahora busca lo del ticket de la hora y cuando vuelvas a ponerlo te habrán puesto una receta de recuerdo""",

    "Tu me dejaste de querer - C Tangana": """Tú me dejaste de querer cuando te necesitaba
Cuando más falta hacía
Tú me diste la espalda (vaya)
Tú me dejaste de querer cuando menos lo esperaba
Cuando más te quería
Se te fueron las ganas (toma que toma)
Dale, aire
Toma que toma (vaya, vaya)
Hala, ajá
Oye, El Madrileño (anda, ah)
Quieto, quieto, quieto (hey)
Ese Pucho (hala)
Venga ya, dale
Chipu, chipu
Yo me creía que era el más cabrón
Pero me estoy notando el corazón (dale, dale)
Estás apretando mucho, mami, déjalo (eso e')
Si quieres te doy la razón (hala)
Yo lo único que quiero es largarme de aquí (oh)
Me da igual dónde puedas elegir (dale)
Algún día, dentro de poco me vo' a arrepentir
De haberte confesa'o lo que me hace sufrir (toma que toma)
Tú me dejaste de querer cuando menos lo esperaba (hale)
Cuando más te quería (madrileño)
Se te fueron la' gana' (uh, ah)
Hala (hala)
¿Qué pasa? (oye)
Tú ('cucha, 'cucha)
Pucho (ese Pucho)
Chipu, chipu, chipu (pucho)
Eso e' (hala)
Hala, hale (eso e')
De punta en blanco para tu fiesta
He pasa'o tre' día' con la misma ropa puesta
Loco por ti, perdiendo apuesta'
Dime en quién piensa' cuando te acuestas
Porque yo pienso en ti (son ilusione')
Yo pienso en ti (son ilusione')
Porque yo pienso en ti (son ilusione')
Yo pienso en ti, son ilusione' (hala)
Tú me dejaste de querer cuando te necesitaba (toma, que lo tome')
Cuando más falta hacía (dímelo bonito)
Tú me diste la espalda (dímelo de verdad)
Tú me dejaste de querer cuando menos lo esperaba
Cuando más te quería
Se te fueron la' gana'
Toma que toma que toma
Hala, ajá (venga ya, dale)
Ese Pucho (toma que toma que toma)
Hey (oh, oh, oh)
Hala (dale)
Vaya, vaya (dale, dale)
Venga ya, Tangana
Toma que toma (ah-ah)
Dale, dale a los que saben, dale""",

    "Tu jardin con enanitos - Melendi": """ Hoy le pido a mis sueños, que te quiten la ropa
Que conviertan en besos
Todos mis intentos de morderte la boca
Y aunque entiendo que tú
Tú siempre tienes la última palabra en esto del amor
Y hoy le pido a tu ángel de la guarda, que comparta
Que me de valor y arrojo en la batalla pa' ganarla
Y es que yo no quiero pasar por tu vida como las modas
No se asuste señorita, nadie le ha hablado de boda
Yo tan solo quiero ser las cuatro patas de tu cama
Tu guerra todas las noches, tu tregua cada mañana
Quiero ser tu medicina, tus silencios y tus gritos
Tu ladrón, tu policía, tu jardín con enanitos
Quiero ser la escoba que en tu vida barra la tristeza
Quiero ser tu incertidumbre y sobre todo tu certeza
Hoy le pido a la luna, que me alargue esta noche
Y que alumbre con fuerza este sentimiento y bailen los corazones
Y aunque entiendo que tú
Serás siempre ese sueño que quizás nunca podre alcanzar
Y hoy le pido a tu ángel de la guarda, que comparta
Que me de valor y arrojo en la batalla pa' ganarla
Y es que yo no quiero pasar por tu vida como las modas
No se asuste señorita, nadie le ha hablado de boda
Yo tan solo quiero ser las cuatro patas de tu cama
Tu guerra todas las noches, tu tregua cada mañana
Quiero ser tu medicina, tus silencios y tus gritos
Tu ladrón, tu policía, tu jardín con enanitos
Quiero ser la escoba que en tu vida barra la tristeza
Quiero ser tu incertidumbre y sobre todo tu certeza
Y es que yo quiero ser el que nunca olvida tu cumpleaños
Quiero que seas mi rosa y mi espina aunque me hagas daño
Quiero ser tu carnaval, tus principios y tus finales
Quiero ser el mar donde puedas ahogar todos tus males
Quiero que seas mi tango de Gardel, mis octavillas
Mi media luna de miel, mi Blues, mi octava maravilla
El baile de mi salón, la cremallera y los botones
Quiero que lleves tu falda y también mis pantalones
Tu astronauta, el primer hombre que pise tu luna
Clavando una bandera de locura
Para pintar tu vida de color, de pasión
De sabor, de emoción y ternura
Sepa usted que yo ya no tengo cura
Sin tu amor """
}

# Genero un diccionario a partir de estas canciones que has introducido
nombre_y_cancion = generar_diccionario(letras_canciones)
Letras = nombre_y_cancion.values()

# -------------------------------------------------------------------PROGRAMA-------------------------------------------------------------------
porcentajesSimilitud = []
letrasSimilitud = []

transcripcion = transcribe_audio_to_text()
print()
print("Se está buscando la canción...")

MensajeFinal = True # Mensaje final por si no se encuentra canción

model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')

for i in Letras:
    sentences = [i, transcripcion]
    
    embeddings = model.encode(sentences)

    # Embeddings obtenidos
    embedding1 = embeddings[0]
    embedding2 = embeddings[1]

    # Calcular la similitud coseno
    similarity_score = cosine_similarity([embedding1], [embedding2])
    porcentajesSimilitud.append(similarity_score)
    valorMax = max(porcentajesSimilitud)
    if similarity_score == valorMax:
        letrasSimilitud = []
        letrasSimilitud.append(i)
    
if valorMax > 0.5:
    print(f"Similitud con la letra: {valorMax}")
    BuscaClave()
    MensajeFinal = False


if MensajeFinal == True:
    print("No se encuentra la canción")
