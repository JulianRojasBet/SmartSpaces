import cv2

def draw_rectangle_on_image(img, upper_corner: tuple, lower_corner: tuple, color='white'):

    # Select the color of the rectangle
    if color=='white':
        color = (255, 255, 255)
    elif color=='black':
        color = (0, 0, 0)

    img = cv2.rectangle(img, upper_corner, lower_corner, color, -1)
    return img