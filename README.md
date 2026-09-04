# 🎓 PrediScore — Predicción de Aprobación de Examen

**Proyecto Final · Sistemas Embebidos y Redes Neuronales**  
**4to Semestre · Tecnología Superior en Desarrollo de Software · 2026_2**  
**Autoras:** Aracely Estefanía Herrera Regalado · Melany Sangoquiza

> Una aplicación académica que utiliza una red neuronal MLP implementada desde cero con NumPy para estimar la probabilidad de aprobación a partir de horas de estudio, asistencia y nota anterior.

## ✨ ¿Qué incluye?

- 🧠 **MLP desde cero**: forward pass, backpropagation, ReLU/Sigmoid y optimizadores SGD, Momentum y Adam.
- 🖥️ **Interfaz de escritorio Tkinter renovada**: diseño oscuro moderno, tarjetas, ejemplos rápidos, resultado visual y recomendaciones sencillas.
- 🌐 **Interfaz web complementaria** en `web/predictor.html`, pensada para que el usuario entienda el resultado sin conocimientos técnicos.
- 📊 **Gráficas y análisis** de entrenamiento, accuracy, pérdida, frontera de decisión y comparación de configuraciones.
- 📄 **Informe y presentación** listos para la defensa del proyecto.
- 📦 **Modelo entrenado** y normalizador incluidos para ejecutar la aplicación sin reentrenar.

## 🎯 Problema

El sistema estima si un estudiante aprobará un examen usando tres variables tabulares:

| Variable | Rango |
|---|---:|
| Horas de estudio semanales | 0–10 h |
| Porcentaje de asistencia | 0–100 % |
| Nota anterior | 0–20 |

## 🧩 Arquitectura

```text
Entrada (3)
     ↓
Oculta 1 (8, ReLU)
     ↓
Oculta 2 (6, ReLU)
     ↓
Salida (1, Sigmoid)
```

La red tiene **93 parámetros entrenables**.

## 🚀 Ejecución

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Entrenar / regenerar resultados

```bash
python src/entrenar.py
```

### 3. Abrir la aplicación de escritorio

```bash
python src/app_gui.py
```

### 4. Usar la versión web

Abre `web/predictor.html` directamente en el navegador. No necesita servidor ni instalación adicional.

## 📁 Estructura

```text
.
├── src/
│   ├── app_gui.py
│   ├── neural_network.py
│   ├── dataset.py
│   ├── entrenar.py
│   └── diagrama_arquitectura.py
├── web/
│   └── predictor.html
├── models/
│   ├── modelo_entrenado.npz
│   ├── normalizador.npz
│   └── metricas.json
├── plots/
│   ├── 00_arquitectura_red.png
│   ├── 01_curvas_perdida.png
│   ├── 02_curvas_accuracy.png
│   ├── 03_train_vs_val.png
│   ├── 04_frontera_decision.png
│   ├── 05_comparacion_final.png
│   ├── 07_captura_gui_moderno.png
│   └── 08_captura_resultado.png
├── docs/
│   └── Informe_Proyecto_Final.docx
├── presentacion/
│   └── Presentacion_Proyecto_Final.pptx
├── requirements.txt
└── README.md
```

## 📌 Nota sobre los resultados

Los resultados reportados corresponden al modelo y dataset del proyecto original. La configuración que obtuvo el mejor accuracy de prueba fue **ReLU + Momentum (82.5 %)**. La aplicación carga ese modelo entrenado para que la predicción de la interfaz corresponda a los pesos guardados.

## 👩‍💻 Autoras

**Aracely Estefanía Herrera Regalado**  
**Melany Sangoquiza**
