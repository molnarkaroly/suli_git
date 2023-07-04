import cv2
import numpy as np

# Kamera inicializálása
cap = cv2.VideoCapture(0)

# Kép betöltése, amit meg szeretnénk jeleníteni
image = cv2.imread(r'C:\Users\molna\Downloads\pg.jpg')



while True:
    # Kamera képének beolvasása
    ret, frame = cap.read()
    if not ret:
        break

    # Kép átméretezése, hogy illeszkedjen a kamera képéhez
    h, w = frame.shape[:2]
    image_resized = cv2.resize(image, (w, h))

    if image_resized.shape[2] == 4:
        alpha = image_resized[:, :, 3] / 255.0
        mask = np.dstack((alpha, alpha, alpha))
        frame = frame * (1 - mask) + image_resized[:, :, :3] * mask
    else:
        frame = frame + image_resized

    # Maszk létrehozása az átlátszó pixelekhez
    alpha = image_resized[:, :, 3] / 255.0
    mask = np.dstack((alpha, alpha, alpha))

    # Kép hozzáadása a kamera képéhez
    frame = frame * (1 - mask) + image_resized[:, :, :3] * mask

    # Kép megjelenítése
    cv2.imshow('AR', frame)

    # Kilépés az ESC billentyűvel
    key = cv2.waitKey(1)
    if key == 27:
        break

# Eredőforrások felszabadítása
cap.release()
cv2.destroyAllWindows()
