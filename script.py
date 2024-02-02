from tkinter import filedialog as fd 
import heic2jpg


filename = fd.askopenfile()

heic2jpg.convertFile(filename.name)
