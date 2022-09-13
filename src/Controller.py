import os
import time
import folium

from datetime import datetime
import folium

class Controller():
    def __init__(self) -> None:
        self.images = []

        self.map = folium.Map()
        self.start = time.time()

        if(not os.path.isdir("./map")):
            os.mkdir("./map")

    def getTotalNoOfImages(self):
        return len(self.images)

    def getNumberOfGPSImages(self):
        result = 0
        for i in self.images:
            if(i.gpsAvailable):
                result += 1
        return result

    def addImages(self, image):
        self.images.append(image)


    def createHeader(self, path):
        print("################################################################################")
        print("")
        print("EXIF GPS Extractor by 5f0")
        print("Extracts Datetime and GPS coordinates from images and displays them on a map")
        print("")
        print("Current working directory: " + os.getcwd())
        print("Investigated images in: " + path)
        print("")
        print("Total numbers of images: " + str(self.getTotalNoOfImages()))
        print("Images with GPS coordinates: " + str(self.getNumberOfGPSImages()))
        print("")
        print("Examination Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("################################################################################")


    def createResults(self, showAll):
        for image in self.images:
            if(showAll):
                image.print()
            else:
                if(image.exifAvailable):
                    if(image.gpsAvailable):
                        image.print()
                        folium.Marker(location=[image.latitude, image.longitude],
                              popup= "<b>MD5: </b>" + image.md5 + "\n<b>CreationDate: </b>" + image.datetime + " \n<b>Model: </b>" + image.cameraModel,
                              icon=folium.Icon(color="red", icon="info-sign")).add_to(self.map)
   

    def createMap(self, path):
        self.map.save(path)

    def calculateExecutionTime(self):
        end = time.time()
        print("")
        print("Execution Time: " + str(end-self.start)[0:8] + " sec")
        print("")

  