import argparse
from pathlib import Path
from heic2x import heic2x
from tkinter import filedialog as fd

parser = argparse.ArgumentParser(
                                 prog='heic2jpg',
                                 description='Converts .heic image files to .jpg.',
                                )

parser.add_argument('--filename', type=Path)
parser.add_argument('--folder', type=Path)
parser.add_argument('--outputFolder', default=Path.cwd(), type=Path)
parser.add_argument('--extension', default='.jpg')
args = parser.parse_args()

if args.filename is not None:
    heic2x.convertFile(args.filename, args.outputFolder, extension=args.extension)

if args.folder is not None:
    heic2x.loadFiles(args.folder, args.outputFolder, extension=args.extension)

if args.folder is None and args.filename is None:
    filename = fd.askopenfile()
    
    if not filename is None:
        filename = Path(filename.name)
    else:
        quit()

    print(filename)
    print(filename.parents[0])

    heic2x.convertFile(filename, filename.parents[0], '.jpg')
