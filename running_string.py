import cv2
import numpy as np

# Параметры для бегущей строки
text = "I love School 21!!!"
font_scale = 1
font_thickness = 2
font_color = (0, 0, 255)
bg_color = (255, 255, 255)
line_spacing = 10
scroll_speed = 2  # Скорость прокрутки (пикселей в секунду)

# Видео параметры
video_width = 100
video_height = 100
fps = 30
duration = 3 # Длительность видео в секундах

# Создание видео объекта
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter("running_text.mp4", fourcc, fps, (video_width, video_height))

# Создание фона видео
background = np.ones((video_height, video_width, 3), dtype=np.uint8)
background[:] = bg_color

# Подготовка текста
font = cv2.FONT_HERSHEY_SIMPLEX
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
text_width, text_height = text_size

# Генерация кадров видео
for i in range(int(fps * duration)):
    frame = background.copy()
    x = (video_width - text_size[0]) // 2 - i * scroll_speed
    y = video_height // 2 + text_height // 2
    cv2.putText(frame, text, (x, y), font, font_scale, font_color, font_thickness)
    video.write(frame)

video.release()
print("Видео успешно создано!")