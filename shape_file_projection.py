import shapefile
import pyproj

p = pyproj.Proj(proj = 'utm', zone=14, ellps='GRS80')
r = shapefile.Reader("/Users/nico/Desktop/clu-samples/clu_public_a_ks067")

print "["
for sr in r.shapeRecords():
    shape = sr.shape
    print "\t["
    for point in shape.points:
        lon, lat = p(point[0], point[1], inverse=True)
        print "\t\t[%8.8f, %8.8f]," % (lat, lon)

    print "\t],"

print "];"
