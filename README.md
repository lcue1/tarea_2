# Luis Ubillus  
**3ro TSDS**

Open app_guess folder

This program is developed in **Android Studio** (Kotlin).  

Exercice
Juego adivinar número
Objetivo:
Crear una aplicación móvil en Android que permita al usuario adivinar un número aleatorio generado por la aplicación. El usuario tendrá un número limitado de intentos para adivinar correctamente el número, y la aplicación proporcionará retroalimentación en cada intento (si el número es mayor o menor que el número a adivinar).

Diseño del Problema:
1. Pantalla Principal:
La aplicación tendrá una interfaz simple con los siguientes elementos:
    • Input del Usuario: Un campo de texto (EditText) donde el jugador ingresa su intento (un número).
    • Botón de Adivinar: Un botón (Button) que, cuando el usuario lo presiona, valida el intento.
    • Retroalimentación del Juego: Un TextView donde se muestra un mensaje de retroalimentación, como:
        ◦ "¡Correcto! Has adivinado el número."
        ◦ "Demasiado alto. Intenta con un número más bajo."
        ◦ "Demasiado bajo. Intenta con un número más alto."
    • Número de Intentos: Un contador que muestra la cantidad de intentos restantes.
    • Botón de Reiniciar: Un botón para reiniciar el juego y generar un nuevo número aleatorio.
2. Lógica del Juego:
    • Generación de Número Aleatorio: La aplicación generará un número aleatorio dentro de un rango predefinido, por ejemplo, entre 1 y 100.
    • Número de Intentos: El jugador tendrá un número limitado de intentos (por ejemplo, 10 intentos). Si el jugador no adivina correctamente en esos intentos, se le muestra un mensaje de "Has perdido" y el número correcto.
    • Validación de la Entrada: Verificar que el número ingresado sea válido (un número dentro del rango y que no esté vacío).
    • Finalización del Juego: El juego termina si el jugador adivina correctamente el número o si se quedan sin intentos.
3. Componentes de la Aplicación:
    • Actividades (Activities):
        ◦ MainActivity: La actividad principal donde se mostrará la interfaz de usuario y gestionará la interacción con el usuario.
        ◦ GameLogic: La lógica del juego (generación de números aleatorios, validación de intentos, etc.).
    • Elementos del UI (Interfaz de Usuario):
        ◦ EditText: Para que el jugador ingrese su intento de número.
        ◦ Button: Para hacer el intento de adivinación y reiniciar el juego.
        ◦ TextView: Para mostrar los mensajes de retroalimentación (como "Correcto", "Demasiado alto", etc.) y el número de intentos restantes.
        ◦ TextView: Para mostrar el número de intentos restantes.
