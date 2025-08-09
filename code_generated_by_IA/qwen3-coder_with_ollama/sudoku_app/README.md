
# 🎲 Generador de Sudoku 🎲

> Una sencilla pero elegante aplicación web que genera un nuevo puzzle de Sudoku cada vez que la visitas.

---

## 📸 Screenshots

*Aquí puedes ver cómo luce la aplicación en acción:*

**Tablero de Sudoku Generado**

![Screenshot de la aplicación de Sudoku](./screenshots/sudoku_board.png)

*Para agregar tu propia screenshot:*
1.  *Ejecuta la aplicación.*
2.  *Toma una captura de pantalla de la página en tu navegador.*
3.  *Crea una carpeta `screenshots` en el directorio del proyecto.*
4.  *Guarda la imagen como `sudoku_board.png` dentro de esa carpeta.*

---

## ✨ Cómo Funciona

Esta aplicación utiliza **Flask** como framework web para servir los puzzles de Sudoku. La lógica principal para generar los puzzles reside en `sudoku_generator.py`.

1.  **Generación del Tablero:**
    *   Se resuelve un tablero completo de Sudoku 9x9 utilizando un algoritmo recursivo de backtracking. Para asegurar un puzzle único cada vez, el algoritmo baraja los números del 1 al 9 antes de intentar colocarlos.
    *   Una vez que el tablero está resuelto, la función `generate_sudoku` elimina un número predefinido de celdas (actualmente 40) al azar para crear el puzzle para el usuario.

2.  **Visualización:**
    *   La aplicación principal de Flask (`app.py`) llama a la función de generación y pasa el puzzle resultante a una plantilla HTML (`templates/index.html`).
    *   La plantilla renderiza el puzzle dentro de una tabla HTML, mostrando los números dados y dejando las otras celdas vacías para que el usuario las resuelva.

---

## 📂 Estructura del Proyecto

```
sudoku_app/
├── 🐍 app.py              # El servidor web principal de Flask
├── 🧩 sudoku_generator.py # La lógica para crear los puzzles de Sudoku
├── 🖼️ templates/
│   └── index.html      # Plantilla HTML para mostrar el Sudoku
├── 📸 screenshots/
│   └── (aquí van tus imágenes)
└── 📖 README.md           # Este archivo
```

---

## 🚀 Cómo Ejecutar la Aplicación

Para poner en marcha esta aplicación en tu máquina local, sigue estos sencillos pasos:

1.  **Clona o descarga el repositorio.**

2.  **Instala las dependencias.**
    Necesitarás tener Python y Flask instalados.
    ```bash
    pip install Flask
    ```

3.  **Ejecuta la aplicación.**
    Navega al directorio `sudoku_app` en tu terminal y ejecuta el siguiente comando:
    ```bash
    python app.py
    ```

4.  **Abre tu navegador.**
    Visita `http://127.0.0.1:5000` en tu navegador web para ver el generador de Sudoku en acción. Haz clic en el enlace "Generar otro Sudoku" para obtener un nuevo puzzle.

---

## 👨‍💻 Creador

Este proyecto fue creado por **gon**.
