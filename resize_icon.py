from PIL import Image

# Open your original JPEG icon
img = Image.open("TMTlogo.jpeg")

# Resize to 32x32 pixels
img_resized = img.resize((32, 32), Image.ANTIALIAS)

# Save resized image as PNG (favicon format)
img_resized.save("favicon_32x32.png")

print("Resized favicon saved as favicon_32x32.png")
