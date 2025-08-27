import cv2
import numpy as np

# اختر الفيديو: video0 أو video1
cap = cv2.VideoCapture('/dev/video1')

if not cap.isOpened():
    print("❌ لم أتمكن من فتح الكاميرا")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ لم أتمكن من قراءة الفريم")
        break

    # تحويل الصورة إلى درجات حرارة ملونة
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_INFERNO)

    cv2.imshow('Thermal Camera', thermal)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
