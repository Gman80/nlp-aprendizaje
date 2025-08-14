# 📚 NLP Aprendizaje en Español con Hugging Face Transformers

## 🎯 Objetivo
Este repositorio es un plan de **8 semanas** para aprender Procesamiento de Lenguaje Natural (NLP) **en español** usando la librería [🤗 Hugging Face Transformers](https://github.com/huggingface/transformers) y datasets en español.  
El aprendizaje está optimizado para un horario de estudio **de 6:00 AM a 10:00 AM**.

---

## 📂 Estructura del repositorio

nlp-aprendizaje/
│
├── notebooks/
│ └── Hugging Face Transformers/
│ ├── 1_pipeline_basico.ipynb
│ ├── 2_tokenizacion.ipynb
│ ├── 3_datasets_tass2020.ipynb
│ ├── 4_trainer_beto.ipynb
│ ├── 5_traduccion_marianmt.ipynb
│ ├── 6_whisper_transcripcion.ipynb
│ ├── 7_blip_captioning.ipynb
│ └── 8_proyecto_final.ipynb
│
├── utils/
│ └── text_cleaning.py
│
├── app_streamlit/
│ ├── app.py
│ └── requirements.txt
│
└── README.md


---

## 📅 Plan de estudio – 8 semanas

| Semana | Notebook | Objetivo |
|--------|----------|----------|
| 1 | `1_pipeline_basico.ipynb` | Uso de modelos pre-entrenados con `pipeline`. |
| 2 | `2_tokenizacion.ipynb` | Tokenización y tensores. |
| 3 | `3_datasets_tass2020.ipynb` | Cargar y explorar datasets en español. |
| 4 | `4_trainer_beto.ipynb` | Entrenar BETO para sentimientos. |
| 5 | `5_traduccion_marianmt.ipynb` | Traducir ES↔EN con MarianMT. |
| 6 | `6_whisper_transcripcion.ipynb` | Transcribir audio en español con Whisper. |
| 7 | `7_blip_captioning.ipynb` | Captioning de imágenes. |
| 8 | `8_proyecto_final.ipynb` | Audio → resumen → traducción. |

---

## 🗂 Datasets usados

| Tarea | Dataset | Link HF Datasets |
|-------|---------|------------------|
| Sentimientos | TASS 2020 | `PlanTL-GOB-ES/tass2020` |
| Pregunta-Respuesta | SQuAD-es | `mrm8488/spanbert-finetuned-squades-spanish` |
| Traducción | MarianMT ES↔EN | `Helsinki-NLP/opus-mt-es-en` / `Helsinki-NLP/opus-mt-en-es` |
| Audio | WHISPER | `openai/whisper-small` |
| Multimodal | BLIP | `Salesforce/blip-image-captioning-base` |

---

## ⏰ Horario diario recomendado (6:00 AM – 10:00 AM)

**Bloque 1 – 6:00 AM a 7:30 AM (90 min)**  
📖 Teoría + ejecución guiada de la semana.  

**Descanso – 7:30 AM a 7:45 AM (15 min)**  

**Bloque 2 – 7:45 AM a 9:15 AM (90 min)**  
💻 Práctica aplicada: modificar parámetros y datasets.  

**Descanso – 9:15 AM a 9:30 AM (15 min)**  

**Bloque 3 – 9:30 AM a 10:00 AM (30 min)**  
📝 Documentar lo aprendido.

---

## 🚀 Ejecutar notebooks
1. Clonar el repo:  

git clone https://github.com/Gman80/nlp-aprendizaje.git
cd nlp-aprendizaje

2. Abrir el notebook de la semana en **Google Colab** o **Jupyter Notebook**.
3. Seguir las instrucciones de cada notebook.

---

## 💡 Consejos
- Prepara el entorno la noche anterior.
- Desayuna ligero antes de iniciar.
- Guarda tus modificaciones y haz `git push` semanalmente.

✍ **Autor:** Gman80  
📆 **Plan optimizado:** Agosto 2025  

