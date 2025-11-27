from PIL import Image, ImageTk, ImageOps

with Image.open("Image/file.png") as img:
    img = img.resize((200, 200))
    img = ImageOps.Circle(img, radius=100)
    img = ImageTk.PhotoImage(img)

add = Label(image=img)
add.place(x=1200, y=140)
