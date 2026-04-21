# 🚀 AI Gesture Control - HMI Visionary System

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-v0.10-0078D4?style=for-the-badge&logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-v4.0-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

This project is an advanced **Human-Machine Interface (HMI)** that utilizes **Artificial Intelligence and Computer Vision** to control the operating system through hand gestures. Designed with a focus on stability, ergonomics, and real-time performance.

---

## 🌟 Key Features

* **High-Precision Detection:** 21-point hand landmark tracking powered by neural networks.
* **Differentiated Gestures:** Robust logic that separates mouse movement, clicking, and scrolling to prevent accidental actions.
* **Adaptive UX:** Includes a **Widget Mode (PiP)** to monitor the system in a small floating window while performing other tasks.
* **Rescue Gesture:** "Open Palm" safety system to pause the execution and recalibrate coordinates instantly.
* **Smoothing Filter:** Linear interpolation algorithm for professional, fluid cursor movement.

---

## 🖐️ Gesture Map

| Gesture | Action | Technical Description |
| :--- | :--- | :--- |
| ☝️ **Index Up** | **Mouse Move** | The index knuckle acts as an anchor for stable cursor positioning. |
| ✌️ **Index + Middle Up** | **Scroll Mode** | Dynamic vertical scrolling (ideal for web browsing). |
| 🤏 **Thumb to Phalanx** | **Left Click** | Precision pinch between thumb and middle finger's middle phalanx. |
| 🖐️ **Open Palm** | **Rescue/Reset** | Stops all actions and resets smoothing filters to eliminate lag. |

---

## 🛠️ Installation & Requirements

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/amolinapi/AIGestureControl.git](https://github.com/amolinapi/AIGestureControl.git)
    cd AIGestureControl
    ```

2.  **Install dependencies via requirements.txt:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 How to Use

1.  **Run the script:**
    ```bash
    python main.py
    ```
2.  **Display Modes:**
    * **Presentation Mode:** Full window with visual telemetry (perfect for demos).
    * **'M' Key:** Toggles to **Widget Mode**, a minimized floating window.
3.  **Exit:** Press the `ESC` key to safely terminate the program.

---

## 🧠 Technical Architecture

The system processes each frame through an optimized pipeline:
1.  **Preprocessing:** BGR to RGB color space conversion and mirror effect application.
2.  **Inference:** MediaPipe extracts 3D hand landmarks in real-time.
3.  **Business Logic:** A Finite State Machine (FSM) determines the action based on spatial geometry and Euclidean distances.
4.  **Execution:** PyAutoGUI injects hardware events directly into the OS input bus.

---

## 👨‍💻 Author

**amolinapi**
* **Profile:** IT Manager / Senior Developer
* **Focus:** Applied Artificial Intelligence & UX.
