import cv2

def count_fingers(image):
    # Kép előfeldolgozása (pl. szürkeárnyalattá alakítás, elmosás, éldetektálás stb.)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    finger_count = 0

    for contour in contours:
        # Kéz kontúrjainak megtalálása
        if cv2.contourArea(contour) > 1000:
            hull = cv2.convexHull(contour, returnPoints=False)
            defects = cv2.convexityDefects(contour, hull)

            # Gyűjtsd össze az ujjakat (küszöbölés a kisebb hibák eltávolításához)
            if defects is not None:
                for i in range(defects.shape[0]):
                    start, end, far, _ = defects[i, 0]
                    start_point = tuple(contour[start][0])
                    end_point = tuple(contour[end][0])
                    far_point = tuple(contour[far][0])

                    # Számold meg a "far" pontokat (ujjhegyek)
                    if far_point[1] < start_point[1] and far_point[1] < end_point[1]:
                        finger_count += 1

    return finger_count

# Webkamera inicializálása
video = cv2.VideoCapture(0)

while True:
    # Képkocka olvasása a webkamerából
    ret, frame = video.read()

    # Kézdeti kép betöltése
    if ret:
        cv2.imshow("Finger Count", frame)
        finger_count_value = count_fingers(frame)
        print("Finger count:", finger_count_value)

    # Kilépés a programból, ha a 'q' billentyűt lenyomod
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera leállítása és ablakok bezárása
video.release()
cv2.destroyAllWindows()
