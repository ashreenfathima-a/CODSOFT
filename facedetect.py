import cv2

# Load the image
img = cv2.imread("group.jpg")

# Resize if image is too large (optional)
max_width = 800
if img.shape[1] > max_width:
    scale = max_width / img.shape[1]
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Try different values for scaleFactor and minNeighbors
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,     # more sensitive
    minNeighbors=3,       # reduce to detect more (but may add false positives)
    minSize=(30, 30)      # minimum face size
)

# Draw rectangles and count
count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    count += 1

# Show count
cv2.putText(img, f"Faces Detected: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# Save and display result
cv2.imwrite("group_faces_detected.jpg", img)
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
