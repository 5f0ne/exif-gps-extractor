# Description

Gets EXIF information from pictures, extracts GPS coordinates and displays them on a map.

# Usage

`main.py [-h] --path PATH [--mapfile MAPFILE] [--showAll SHOWALL]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to the directory  |
|--mapfile | -m | Str | ./map/index.html | Path to the map with the extracted GPS coords |
| --showAll | -s | Bool | False | True if all EXIF results shall be shown, False if only gps tagged results shall be displayed |


# Example

`python main.py -p "path/to/img" > result.txt`

You can find the following result [here](./example/example.txt):

```
################################################################################

EXIF GPS Extractor by 5f0
Extracts Datetime and GPS coordinates from images and displays them on a map

Current working directory: /software/exif-gps-extractor
Investigate images in: img

Total numbers of images: 1
Images with GPS coordinates: 1

Current Datetime: 01/01/1970 10:11:12

################################################################################

Investigated Image: img/example.jpg

    MD5 Hash: 92e9d12b3784f1386557c9e3fb47ae1c
 SHA256 Hash: ac759931999a215ef78469a82bdfc382ccba96eb8d039ec9e81e53a9a419d35e

     Company: Apple
       Model: iPhone 11
    Software: Adobe Photoshop CS6 (Windows)
    DateTime: 1970:12:24 00:45:41
    Latitude: 38.897675
   Longitude: -77.036530
    Location: The White House, 1600 Pennsylvania Avenue, N.W. Washington, DC 20500

################################################################################

Execution Time: 0.620638 sec
```

The created map showing the GPS coordinates will be located by default under:

`./map/index.html`

Just open it in a browser.

# LICENSE

MIT