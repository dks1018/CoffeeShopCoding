import urllib.request

uf = urllib.request.urlopen("https://gis.fultoncountyga.gov/Apps/PropertyProfile/PropertyProfileSimple.html?pin=09F101000520172&mode=print&o=N")
html = uf.read()

print(html)

