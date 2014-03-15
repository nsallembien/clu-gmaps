clu-gmaps
=========

Highlights a CLU boundary with a GPolygon using Google maps

Prerequisites:

```
pip install shapefile
pip install pyproj
brew install proj
```

Usage:
======

* Edit `shape_file_projection.py` to point to a shapefile on your disk.
* Edit `index.html` to include your Google Maps API key.
* Change the projection parameters in the code to match those used by your shapefile.
* Run `python shape_file_projection.py` to generate the data in JSON format.
* Include the JSON code in index.html and load it into your browser.
