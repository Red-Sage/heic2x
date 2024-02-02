from PIL import Image
from pillow_heif import register_heif_opener
import argparse
from pathlib import Path

register_heif_opener()

def convertFile(fname, outputFolder, extension):
    image = Image.open(fname)
    image.save(outputFolder / fname.with_suffix(extension).name)

def loadFiles(folder, outputFolder, extension):
    folder = Path(folder)
    files = folder.match('*.heic')
    for file in files:
        convertFile(file, outputFolder, extension)
        

if __name__=="__main__":
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
        convertFile(args.filename, args.outputFolder, extension=args.extension)
    
    
    if args.folder is not None:
        loadFiles(args.folder, args.outputFolder, extension=args.extension)