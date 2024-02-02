from tkinter import filedialog as fd 
import heic2x
from pathlib import Path


filename = fd.askopenfile()

if not filename is None:
    filename = Path(filename.name)
else:
    quit()

heic2x.convertFile(filename, filename.parents[0], '.jpg')
