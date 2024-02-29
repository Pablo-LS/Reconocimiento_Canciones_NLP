# Reconocimiento de canciones con NLP

## Descripción 
Este proyecto se basa en el procesamiento del lenguaje natural (NLP) y hace uso del servicio Google Text To Speech para hacer la entrada de texto mediante el micrófono. He adaptado un modelo de comparación de similitudes de frases de Hugging Face, para poder analizar y comparar letras de canciones seleccionadas por el usuario con una frase proporcionada por voz. <br><br>
Al usar Inteligencia Artificial, la frase que el usuario introduce puede no ser exactamente la letra de la canción, o puede que alguna palabra esté cambiada. El propósito es que aun así el programa sea capaz de reconocer de que canción le estamos hablando.

## Características
-**Modelo de Procesamiento del Lenguaje Natural (NLP):** Implementé un modelo de Hugging Face que permite la comparación de similitudes entre frases, proporcionando una base sólida que después adapté para la identificación de canciones.

-**Integración con Google Text To Speech:** Facilito la entrada de frases mediante el micrófono, ofreciendo una experiencia de usuario más accesible.

-**Comparación de Letras de Canciones:** El programa selecciona y analiza letras de varias canciones, las desglosa automáticamente en frases y las compara con la frase proporcionada por el usuario. Esto se traduce en un porcentaje de similitud y la identificación precisa de la canción deseada.

## Uso
**1. Instala las librerias necesarias para ejecutar el programa:** <br>
   Estas se encuentran en el archivo principal, ya preparadas para ejecutar. <br>

**2. Introduce el nombre de las canciones que quieras comparar y la letra:** <br>
  Por defecto, el programa incluye algunas canciones de ejemplo. Simplemete cambia los nombres y pega la letra de las canciones que quieras comparar: <br>
   
        letras_canciones = {
            "Zapatillas - El Canto Del Loco": """Estoy cansado de salir de noche ...""",
        
            "Tu me dejaste de querer - C Tangana": """Tú me dejaste de querer cuando te necesitaba...""",
        
            "Tu jardin con enanitos - Melendi": """ Hoy le pido a mis sueños..."""
        }

**3. Entrada de Frase por Voz:** <br>
Utiliza el micrófono para introducir la frase que deseas comparar con las letras de canciones

**4. Resultado:** <br>
El programa comparará tu frase introducida y te dirá de que canción se trata y un porcentaje de similitud

## Reconocimiento
Este programa utiliza el modelo hiiamsid/sentence_similarity_spanish_es de Hugging Face para funcionar. El programa ha sido creado unicamente con fines educativos. <br>
Enlace al modelo: https://huggingface.co/hiiamsid/sentence_similarity_spanish_es

<br><br>

# Song Recognition with NLP

## Description
This project is based on natural language processing (NLP) and uses the Google Text To Speech service for text input via the microphone. I have adapted a sentence similarity comparison model from Hugging Face to analyze and compare lyrics of songs selected by the user with another voice-provided phrase. <br><br>
Through the use of Artificial Intelligence, this program excels in recognizing songs, even when the user's input doesn't precisely match the song's lyrics or involves some altered words. The goal is to ensure the program can still accurately identify the entered song.

## Features
- **Natural Language Processing (NLP) Model:** I implemented a Hugging Face model that enables the comparison of similarities between phrases, providing a solid foundation that I later adapted for song identification.

- **Integration with Google Text To Speech:** Facilitating phrase input through the microphone, enhancing the user experience.

- **Comparison of Song Lyrics:** The program selects and analyzes lyrics from various songs, automatically breaks them into phrases, and compares them with the phrase that the user provided. This results in a similarity percentage and accurate identification of the desired song.

## Usage
**1. Install the required libraries to run the program:** <br>
   These are located in the main file, already prepared for execution. <br>

**2. Enter the names of the songs you want to compare and their lyrics:** <br>
   By default, the program includes some example songs. Simply change the names and paste the lyrics of the songs you want to compare: <br>
   
        letras_canciones = {
            "Zapatillas - El Canto Del Loco": """Estoy cansado de salir de noche ...""",
        
            "Tu me dejaste de querer - C Tangana": """Tú me dejaste de querer cuando te necesitaba...""",
        
            "Tu jardin con enanitos - Melendi": """ Hoy le pido a mis sueños..."""
        }

**3. Voice Input of Phrase:** <br>
   Use the microphone to input the phrase you want to compare with the song lyrics.

**4. Result:** <br>
   The program will compare your entered phrase and tell you which song it is and the percentage of similarity.

## Acknowledgments
This program uses the hiiamsid/sentence_similarity_spanish_es model from Hugging Face to function. The program has been created only for educational purposes. <br>
Model link: https://huggingface.co/hiiamsid/sentence_similarity_spanish_es
