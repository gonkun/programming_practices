# 🎲 Generador de Sudoku 🎲

> Una elegante aplicación web que genera un nuevo puzzle de Sudoku con diferentes niveles de dificultad.

---

## 📸 Screenshots

*Aquí puedes ver cómo luce la aplicación en acción:*

**Tablero de Sudoku con Selector de Dificultad**

![Screenshot de la aplicación de Sudoku](./screenshots/sudoku_board.png)

*Para agregar tu propia screenshot:*
1.  *Ejecuta la aplicación.*
2.  *Toma una captura de pantalla de la página en tu navegador.*
3.  *Crea una carpeta `screenshots` en el directorio del proyecto.*
4.  *Guarda la imagen como `sudoku_board.png` dentro de esa carpeta.*

---

## ✨ Características

*   **Generación Dinámica:** Crea un nuevo puzzle de Sudoku cada vez que se recarga la página.
*   **Niveles de Dificultad:** Elige entre varios niveles de dificultad (Fácil, Medio, Difícil, Experto) para ajustar el número de pistas.
*   **Interfaz Limpia:** Un diseño moderno y visualmente agradable para mostrar el tablero de Sudoku.
*   **Código Organizado:** La lógica está encapsulada en una clase `SudokuGenerator` para mayor claridad y reutilización.

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
    Visita `http://127.0.0.1:5000` en tu navegador web. Para cambiar la dificultad, simplemente haz clic en los botones correspondientes.

---

## 👨‍💻 Creador

Este proyecto fue creado por **gon**.