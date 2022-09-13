import hashlib

from geopy.geocoders import Nominatim

class Image():
    def __init__(self, path) -> None:
        self.path = path
        self.exifAvailable = False
        self.gpsAvailable = False
        self.latitude = "-"
        self.latitudeRef = "-"
        self.longitude = "-"
        self.longitudeRef = "-"
        self.software = "-"
        self.datetime = "-"
        self.cameraModel = "-"
        self.cameraCompany = "-"
        self.location = "-"
        self.md5 = "-"
        self.sha256 = ""
        self.geolocator = Nominatim(user_agent="exif-gps-extractor")
        self.__calculateFileHash()


    def parseTags(self, tags): 
        keys = tags.keys()
        for k in keys:
            if "Image Make" in k:
                self.cameraCompany = tags["Image Make"].values
            if "Image Model" in k:
                self.cameraModel = tags["Image Model"].values
            if "Image Software" in k:
                self.software = tags["Image Software"].values
            if "Image DateTime" in k:
                self.datetime = tags["Image DateTime"].values
            if "GPS GPSLatitude" in k:
                self.latitude = tags["GPS GPSLatitude"].values
            if "GPS GPSLatitudeRef" in k:
                self.latitudeRef = tags["GPS GPSLatitudeRef"].values
            if "GPS GPSLongitude" in k:
                self.longitude = tags["GPS GPSLongitude"].values
            if "GPS GPSLongitudeRef" in k:
                self.longitudeRef = tags["GPS GPSLongitudeRef"].values

        if(self.latitude != "-" and self.longitude != "-"):    
           self.__calculateGps()


    def print(self):
        print("")
        print("Investigated Image: " + self.path)
        print("")
        print("     MD5 Hash: " + self.md5)
        print("  SHA256 Hash: " + self.sha256)
        print("")
        print("EXIF:")
        print(f"     Company: {self.cameraCompany}")
        print(f"       Model: {self.cameraModel}")
        print(f"    Software: {self.software}")
        print(f"    DateTime: {self.datetime}")
        print(f"    Latitude: {self.latitude}")
        print(f" LatitudeRef: {self.latitudeRef}")
        print(f"   Longitude: {self.longitude}")
        print(f"LongitudeRef: {self.longitudeRef}")
        print(f"    Location: {self.location}")
        print("")
        print("################################################################################")


    def __calculateGps(self):

        lngCor = [c.decimal() for c in self.longitude]
        latCor = [c.decimal() for c in self.latitude]

        lngCor = sum([c/60**i for i, c in enumerate(lngCor)])
        if(self.longitudeRef == "W"):
            lngCor = (-1) * lngCor

        latCor = sum([c/60**i for i, c in enumerate(latCor)])
        if(self.latitudeRef == 'S'):  
            latCor = (-1) * latCor

        self.latitude = latCor
        self.longitude = lngCor

        self.gpsAvailable = True

        try:
            self.location = self.geolocator.reverse(f"{self.latitude}, {self.longitude}")
        except:
            pass


    def __calculateFileHash(self):

        sha256 = hashlib.sha256()
        md5 = hashlib.md5()

        with open(self.path, "rb") as f:
            while True:
                data = f.read(65536) 
                if not data:
                    break
                sha256.update(data)
                md5.update(data)

        self.sha256 = sha256.hexdigest()
        self.md5 = md5.hexdigest()