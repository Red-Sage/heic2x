from PIL import Image
from pillow_heif import register_heif_opener
import argparse
from pathlib import Path

register_heif_opener()

def convertFile(fname, outputFolder):
    image = Image.open(fname)
    image.save(outputFolder / fname.with_suffix(".jpg").name)

def loadFiles(folder, outputFolder):
    folder = Path(folder)
    files = folder.match('*.heic')
    for file in files:
        convertFile(file, outputFolder)
        
if __name__=='__main__':
    parser = argparse.ArgumentParser(
                                     prog='heic2jpg',
                                     description='Converts .heic image files to .jpg.',
                                    )
    
    parser.add_argument('--filename', type=Path)
    parser.add_argument('--folder', type=Path)
    parser.add_argument('--outputFolder', default=Path.cwd(), type=Path)

    args = parser.parse_args()

    if args.filename is not None:
        convertFile(args.filename, args.outputFolder)

    if args.folder is not None:
        loadFiles(args.folder, args.outputFolder)
