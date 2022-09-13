import os
import argparse
import exifread

from src.Image import Image
from src.Controller import Controller

parser = argparse.ArgumentParser()
parser.add_argument("--path", "-p", type=str, required=True, help="Path to the directory containing the images")
parser.add_argument("--mapfile", "-m", type=str, default="./map/index.html", help="Path to the created map")
parser.add_argument("--showAll", "-s", type=bool, default=False, help="True if all results shall be shown, False if only gps tagged results shall be displayed")
args = parser.parse_args()


c = Controller()

for path, dirs, files in os.walk(args.path):
    for file in files:
        currentFile = os.path.join(path, file)
        if (".png" in currentFile or ".PNG" in currentFile or
           ".jpg" in currentFile or ".JPG" in currentFile or
           ".jpeg" in currentFile or ".JPEG" in currentFile or
           ".gif" in currentFile or ".GIF" in currentFile or
           ".tiff" in currentFile or ".TIFF" in currentFile):

            with open(currentFile, "rb") as img:
                o = Image(currentFile)
                
                try:
                    tags = exifread.process_file(img)
 
                    if(len(tags) > 0):
                        o.exifAvailable = True
                        o.parseTags(tags)

                except:
                    pass
            
                c.addImages(o)

c.createHeader(args.path)
c.createResults(args.showAll)
c.createMap(args.mapfile)
c.calculateExecutionTime()