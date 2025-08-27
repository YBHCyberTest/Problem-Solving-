import cv2
import numpy as np

# اختر الفيديو المناسب (video0 أو video1)
cap = cv2.VideoCapture(0)  # جرب 0 أو 1 لو الشاشة سوداء

if not cap.isOpened():
    print("❌ لم أتمكن من فتح الكاميرا")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ لم أتمكن من قراءة الإطار")
        break

    # تحويل الصورة إلى grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # تطبيق colormap حراري
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_INFERNO)

    # عرض الصورة
    cv2.imshow("UTi720M Thermal View", thermal)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
