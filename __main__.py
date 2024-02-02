import argparse
from pathlib import Path
import heic2x.convertFile
import heic2x.loadFiles


parser = argparse.ArgumentParser(
                                 prog='heic2jpg',
                                 description='Converts .heic image files to .jpg.',
                                )

parser.add_argument('--filename', type=Path)
parser.add_argument('--folder', type=Path)
parser.add_argument('--outputFolder', default=Path.cwd(), type=Path)
parser.add_argument('--extension', default='.jpg')
args = parser.parse_args()

print(args.filename)
print(args.folder)

if args.filename is not None:
    convertFile(args.filename, args.outputFolder, extension=args.extension)


if args.folder is not None:
    loadFiles(args.folder, args.outputFolder, extension=args.extension)