import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math
import time

# --- CONFIGURACIÓN SENIOR ---
pyautogui.PAUSE = 0
W_CAM, H_CAM = 640, 480
W_SCR, H_SCR = pyautogui.size()
MARGEN = 110
SUAVIZADO = 6  # Ligeramente más alto para que el vídeo se vea fluido

# Colores Profesionales (BGR)
C_VERDE = (0, 255, 127)  # Click
C_CIAN = (255, 255, 0)  # Scroll
C_ROSA = (255, 0, 255)  # Puntero
C_AMARILLO = (0, 255, 255)  # Rescate
C_BLANCO = (255, 255, 255)
C_ROJO = (0, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, W_CAM)
cap.set(4, H_CAM)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8)

p_loc_x, p_loc_y = 0, 0
clic_hecho = False
modo_mini = False  # Empezamos en modo GRANDE para el vídeo

print(">>> SISTEMA HMI PARA VÍDEO DE PORTFOLIO")
print(">>> Pulsa 'M' para cambiar entre modo GRANDE/MINI.")
print(">>> Pulsa 'ESC' para salir.")

while cap.isOpened():
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)

    # --- SUPERPOSICIÓN GRÁFICA PROFESIONAL (HUD) ---
    # Dibujamos un panel de estado en la parte superior
    h_panel = 110
    overlay = img.copy()
    cv2.rectangle(overlay, (0, 0), (W_CAM, h_panel), (30, 30, 30), -1)
    img = cv2.addWeighted(overlay, 0.6, img, 0.4, 0)  # Semitransparente

    # Textos de los 4 gestos (Estáticos)
    font_hud = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, "HMI VISIONARY CONTROL", (10, 25), font_hud, 0.8, C_BLANCO, 1)

    # Los 4 estados para resaltar
    gestos_info = [
        ("IDLE", (10, 55), (100, 100, 100)),
        ("1. PUNTERO", (10, 85), C_ROSA),
        ("2. CLICK", (180, 55), C_VERDE),
        ("3. SCROLL", (180, 85), C_CIAN),
        ("4. RESCATE", (350, 70), C_AMARILLO)
    ]

    # Dibujamos los textos por defecto (apagados)
    for txt, pos, color in gestos_info:
        cv2.putText(img, txt, pos, font_hud, 0.6, (150, 150, 150), 1)

    # --- PROCESAMIENTO IA ---
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_lms = results.multi_hand_landmarks[0]


        # Puntos clave
        def pt(id):
            lm = hand_lms.landmark[id]
            return int(lm.x * W_CAM), int(lm.y * H_CAM)


        idx_tip, idx_mid = pt(8), pt(6)
        cor_tip, cor_mid, cor_pha = pt(12), pt(10), pt(11)
        pul_tip = pt(4)

        # Estados de los dedos (Mejorado para estabilidad)
        indice_up = hand_lms.landmark[8].y < hand_lms.landmark[6].y
        corazon_up = hand_lms.landmark[12].y < hand_lms.landmark[10].y

        # Gesto Rescate (Contar dedos)
        dedos_arriba = []
        if hand_lms.landmark[4].x > hand_lms.landmark[3].x: dedos_arriba.append(1)  # Pulgar
        for i in [6, 10, 14, 18]:  # Nudillos medios
            if hand_lms.landmark[i + 2].y < hand_lms.landmark[i].y: dedos_arriba.append(1)

        total_dedos = sum(dedos_arriba)

        # --- LÓGICA DE GESTOS Y RESALTADO ---

        # Gesto Activo
        gesto_activo_txt = "IDLE"
        color_activo = (100, 100, 100)
        pos_activo = (10, 55)

        # 4. RESCATE (Prioridad)
        if total_dedos == 5:
            gesto_activo_txt, pos_activo, color_activo = "4. RESCATE", (350, 70), C_AMARILLO
            p_loc_x, p_loc_y = pyautogui.position()
            cv2.putText(img, "RESET", (W_CAM // 2 - 30, H_CAM // 2), font_hud, 1, C_AMARILLO, 2)
            cv2.rectangle(img, (0, 0), (W_CAM, H_CAM), C_AMARILLO, 5)  # Marco de rescate

        # Control normal
        else:
            dist_click = math.hypot(pul_tip[0] - cor_pha[0], pul_tip[1] - cor_pha[1])

            # 2. CLICK
            if dist_click < 35:
                if not clic_hecho:
                    pyautogui.click()
                    clic_hecho = True
                gesto_activo_txt, pos_activo, color_activo = "2. CLICK", (180, 55), C_VERDE
                cv2.circle(img, cor_pha, 15, C_VERDE, cv2.FILLED)

            # 3. SCROLL
            elif indice_up and corazon_up:
                y_p = np.interp(idx_tip[1], (MARGEN, H_CAM - MARGEN), (0, H_SCR))
                if abs(y_p - p_loc_y) > 15:
                    pyautogui.scroll(int(-(y_p - p_loc_y) * 4))
                    p_loc_y = y_p
                gesto_activo_txt, pos_activo, color_activo = "3. SCROLL", (180, 85), C_CIAN
                cv2.circle(img, idx_tip, 10, C_CIAN, cv2.FILLED)
                cv2.circle(img, cor_tip, 10, C_CIAN, cv2.FILLED)
                clic_hecho = False

            # 1. PUNTERO
            elif indice_up and not corazon_up:
                x_p = np.interp(idx_mid[0], (MARGEN, W_CAM - MARGEN), (0, W_SCR))
                y_p = np.interp(idx_mid[1], (MARGEN, H_CAM - MARGEN), (0, H_SCR))
                curr_x = p_loc_x + (x_p - p_loc_x) / SUAVIZADO
                curr_y = p_loc_y + (y_p - p_loc_y) / SUAVIZADO
                pyautogui.moveTo(curr_x, curr_y)
                p_loc_x, p_loc_y = curr_x, curr_y
                gesto_activo_txt, pos_activo, color_activo = "1. PUNTERO", (10, 85), C_ROSA
                cv2.drawMarker(img, idx_mid, C_ROSA, cv2.MARKER_CROSS, 20, 2)
                clic_hecho = False

            else:
                clic_hecho = False

        # Resaltamos el gesto activo sobre el panel gris
        cv2.putText(img, gesto_activo_txt, pos_activo, font_hud, 0.6, color_activo, 2)
        mp.solutions.drawing_utils.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)

    # --- MANEJO DE VENTANAS (GRANDE / MINI) ---
    key = cv2.waitKey(1) & 0xFF

    if key == ord('m'):  # Tecla 'M' para cambiar modo
        modo_mini = not modo_mini
        if modo_mini:
            # Forzamos que la ventana principal se cierre para re-abrirla pequeña
            cv2.destroyWindow("Vision Control - Presentation")
        else:
            cv2.destroyWindow("Vision Control - Widget")

    if modo_mini:
        final_img = cv2.resize(img, (240, 180))
        win_name = "Vision Control - Widget"
    else:
        final_img = img
        win_name = "Vision Control - Presentation"

    cv2.imshow(win_name, final_img)
    if key == 27: break  # ESC

cap.release()
cv2.destroyAllWindows()