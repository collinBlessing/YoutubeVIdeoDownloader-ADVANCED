from tkinter.filedialog import askdirectory


path = askdirectory(title='Save Download Video', mustexist=True)
path = r'{}'.format(path)
print(path)