# 🚀 AI Gesture Control - HMI Visionary System

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-v0.10-0078D4?style=for-the-badge&logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-v4.0-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

Este proyecto es una **Interfaz Hombre-Máquina (HMI)** avanzada que utiliza **Inteligencia Artificial y Visión Artificial** para controlar el sistema operativo mediante gestos manuales. Diseñado con un enfoque en la estabilidad, la ergonomía y el rendimiento en tiempo real.

---

## 🌟 Características Principales

* **Detección de Alta Precisión:** Tracking de 21 puntos clave de la mano mediante redes neuronales.
* **Gestos Diferenciados:** Lógica robusta que separa el movimiento del ratón, el click y el scroll para evitar acciones accidentales.
* **UX Adaptativa:** Incluye un **Modo Widget (PiP)** para monitorizar el sistema en una ventana pequeña mientras realizas otras tareas.
* **Gesto de Rescate:** Sistema de seguridad de "Palma Abierta" para pausar el sistema y re-calibrar coordenadas.
* **Filtro de Suavizado:** Algoritmo de interpolación para un movimiento del cursor fluido y profesional.

---

## 🖐️ Mapa de Gestos

| Gesto | Acción | Descripción técnica |
| :--- | :--- | :--- |
| ☝️ **Índice arriba** | **Mover Ratón** | El nudillo del índice actúa como ancla para mover el cursor. |
| ✌️ **Índice + Corazón** | **Modo Scroll** | Desplazamiento vertical dinámico (ideal para lectura de webs). |
| 🤏 **Pulgar a Falange** | **Click Izquierdo** | Pinza entre pulgar y falange media del corazón (Gesto estable). |
| 🖐️ **Palma Abierta** | **Rescate/Reset** | Detiene cualquier acción y resetea los filtros de suavizado. |

---

## 🛠️ Instalación y Requisitos

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/amolinapi/AIGestureControl.git](https://github.com/amolinapi/AIGestureControl.git)
    cd AIGestureControl
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Cómo usarlo

1.  **Ejecutar el script:**
    ```bash
    python main.py
    ```
2.  **Modos de visualización:**
    * **Modo Presentación:** Ventana completa con telemetría de gestos (ideal para demos).
    * **Tecla 'M':** Alterna al **Modo Widget**, una ventana flotante minimizada.
3.  **Cerrar:** Presiona la tecla `ESC` para finalizar la ejecución.

---

## 🧠 Arquitectura Técnica

El sistema procesa cada frame a través de un pipeline optimizado:
1.  **Pre-procesamiento:** Conversión de espacio de color BGR a RGB y efecto espejo.
2.  **Inferencia:** MediaPipe extrae los puntos clave (Landmarks) en 3D.
3.  **Lógica de Negocio:** Una máquina de estados decide la acción basada en geometría espacial y distancias euclidianas.
4.  **Ejecución:** PyAutoGUI inyecta los eventos de hardware directamente en el SO.

---

## 👨‍💻 Autor

**amolinapi**
* **Perfil:** IT Manager / Senior Developer
* **Enfoque:** Inteligencia Artificial Aplicada y UX.
