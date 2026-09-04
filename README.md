# PrediScore

## Proyecto Final — Sistemas Embebidos y Redes Neuronales

Este proyecto consiste en una aplicación para estimar la probabilidad de que un estudiante apruebe un examen. Para hacerlo usamos una red neuronal MLP y tres datos: horas de estudio, asistencia y nota anterior.

### Integrantes

- Aracely Estefanía Herrera Regalado
- Melany Sangoquiza

4to Semestre — Desarrollo de Software

## ¿Qué hace el programa?

El usuario ingresa:

- Horas de estudio por semana (0 a 10)
- Asistencia a clases (0% a 100%)
- Nota anterior (0 a 20)

Con esos datos, el programa calcula una probabilidad de aprobación y muestra el resultado junto con una recomendación.

La red tiene la siguiente estructura:

**3 entradas → 8 neuronas → 6 neuronas → 1 salida**

Las capas ocultas usan ReLU y la salida usa Sigmoid. La red tiene 93 parámetros entrenables.

## Pruebas del modelo

Durante el proyecto probamos cuatro configuraciones diferentes:

| Configuración | Accuracy de prueba |
|---|---:|
| Sigmoid + SGD | 80.0% |
| ReLU + SGD | 77.5% |
| ReLU + Momentum | **82.5%** |
| ReLU + Adam | 79.17% |

La mejor configuración fue **ReLU + Momentum**, con un accuracy de prueba del 82.5%. La aplicación utiliza el modelo entrenado con esta configuración.

## Interfaz

La aplicación principal está hecha con Tkinter. Se puede cambiar cada uno de los valores con controles deslizantes y también probar algunos ejemplos ya preparados.

Además del programa de escritorio, dejamos una versión web en `web/predictor.html` para poder probar el predictor desde un navegador.

## Cómo ejecutar

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

Después ejecuta:

```bash
python src/app_gui.py
```

Si quieres volver a entrenar la red:

```bash
python src/entrenar.py
```

La versión web se encuentra en:

```text
web/predictor.html
```

## Organización del proyecto

```text
PrediScore/
├── src/              Código de Python
├── models/           Modelo entrenado y métricas
├── plots/            Gráficas y capturas
├── web/              Versión web
├── docs/             Informe
├── presentacion/     Presentación
├── requirements.txt  Dependencias
└── README.md
```

## Tecnologías

- Python
- NumPy
- Tkinter
- HTML
- CSS
- JavaScript
- Node.js / PptxGenJS

Aquí se encuentra el código fuente, el modelo entrenado, las gráficas, el informe y la presentación del proyecto final.

**Proyecto Final — Sistemas Embebidos y Redes Neuronales**
