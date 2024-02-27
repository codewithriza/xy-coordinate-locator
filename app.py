import tkinter as tk
from PIL import Image, ImageTk

# Function to get the mouse position when clicked on the image
def get_mouse_position(event):
    x, y = event.x, event.y
    print(f"Mouse clicked at: {x}, {y}")

# Replace "your_image.png" with the path to your image file
image_path = "your_image.png"

# Open the image file
image = Image.open(image_path)

# Create a Tkinter window
root = tk.Tk()

# Convert the PIL Image to a Tkinter-compatible format
tkimage = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = tk.Label(root, image=tkimage)
label.pack()

# Bind the left mouse button click event to the get_mouse_position function
label.bind("<Button-1>", get_mouse_position)

# Start the Tkinter event loop
root.mainloop()
