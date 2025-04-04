from tkinter import filedialog as fd 
import heic2x
from pathlib import Path


filename = fd.askopenfile()



heic2x.convertFile(filename, filename.parents[0], '.jpg')
