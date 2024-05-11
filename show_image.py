import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen

root = tk.Tk()

imageUrl = "https://i.ytimg.com/vi/domt_Sx-wTY/sddefault.jpg"
u = urlopen(imageUrl)
raw_data = u.read()
u.close()

photo = ImageTk.PhotoImage(data=raw_data)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

root.mainloop()
