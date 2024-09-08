import cv2

def detect_face_features(image_path):
    """
    Function to detect face features in an image using OpenCV.

    Parameters:
    - image_path: str
        The path to the image file.

    Returns:
    - list of tuples:
        A list of tuples containing the coordinates of the detected face features.
        Each tuple represents a feature and contains the (x, y) coordinates.

    Raises:
    - FileNotFoundError:
        If the image file is not found at the specified path.
    """

    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # List to store the coordinates of detected face features
    face_features = []

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Add the coordinates of the face bounding box to the list
        face_features.append((x, y))

        # Draw a rectangle around the face
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with detected face features
    cv2.imshow("Detected Face Features", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return face_features

# Example usage of the detect_face_features function:

# Specify the path to the image file
image_path = "path/to/image.jpg"

try:
    # Detect face features in the image
    features = detect_face_features(image_path)

    # Print the coordinates of the detected face features
    for feature in features:
        print(f"Detected face feature at coordinates: {feature}")
except FileNotFoundError:
    print(f"Image file not found at path: {image_path}")