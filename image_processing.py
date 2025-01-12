import cv2  # Import OpenCV library

# Read the image
image = cv2.imread('assignment-001-given.jpg')

if image is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Draw a green rectangle on the image
    # Rectangle coordinates: top-left (265, 190), bottom-right (985, 925)
    # Color: Green (BGR format: (0, 255, 0)), Thickness: 8 pixels
    cv2.rectangle(image, (265, 190), (985, 925), (0, 255, 0), 8)

    # Create a semi-transparent overlay for the shadow
    overlay = image.copy()
    cv2.rectangle(overlay, (795, 80), (1235, 175), (0, 0, 0), -1)  

    # Apply transparency using addWeighted
    alpha = 0.5  # Transparency factor (50%)
    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

    # Add text over the image
    # Font: Hershey Simplex, Size: 3, Color: Green (0, 255, 0), Thickness: 7
    cv2.putText(image, 'RAH972U', (800, 160), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)

    # Display the image in a new window named 'Image'
    cv2.imshow('Image', image)

    # Wait indefinitely until a key is pressed
    cv2.waitKey(0)

    # Save the resulting image to a new file
    cv2.imwrite('result.jpg', image)

    # Close all OpenCV windows to release resources
    cv2.destroyAllWindows()
