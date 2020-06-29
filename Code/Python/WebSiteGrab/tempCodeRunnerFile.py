import urllib.request

uf = urllib.request.urlopen("https://qpublic.schneidercorp.com/Application.aspx?AppID=936&LayerID=18251&PageTypeID=4&PageID=8156&Q=2124870374&KeyValue=09F101000520172")
html = uf.read()

print(html)
