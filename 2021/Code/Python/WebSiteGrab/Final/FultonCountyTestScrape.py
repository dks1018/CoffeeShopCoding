import bs4 as bs 
import urllib.request                    #--------------------------> 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             #the Offset= number below is where the 25 or 9 stepping value loop has to occur                         


def GetURL():
    # url = urllib.request.urlopen('https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&resultOffset=0&resultRecordCount=25')
    # url = 'https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&result" + Offset + "&resultRecordCount=25'
    urlSITE = "https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&result" + Offset + "&resultRecordCount=25"

    request_string = urllib.request.urlopen(urlSITE)
    soup = bs.BeautifulSoup(request_string,'lxml')
    return soup

ChrisChooseNumber = 100
OG_offsetNum = 0
new_offsetNum = str(OG_offsetNum)
Offset = "Offset=" + new_offsetNum

if(OG_offsetNum < ChrisChooseNumber):
    OG_offsetNum += 25
    func = GetURL()
    

#when looking at the source on webpage the body only displays 9 data points at a time///might need the Offset= value to step by 9
#when you print the soup it displays all 25 data points at a time 
#need to write code to select the data points below
print(soup) 
["OBJECTID", "ParcelID", "Owner", "Address", "OwnerAddr1", "OwnerAddr2", "ClassCode", "LandAcres"]

filename = "fultoncounty.csv"
f= open(filename, "w")

headers = "OBJECTID, ParcelID, Owner, Address, OwnerAddr1, OwnerAddr2, ClassCode, LandAcres\n"

f.write(headers)


#below is inside for statement
    print("OBJECTID: " + OBJECTID)
    print("ParcelID: " + ParcelID)
    print("Owner: " + Owner)
    print("Address: " + Address)
    print("OwnerAddr1: " + OwnerAddr1)
    print("OwnerAddr2: " + OwnerAddr2)
    print("ClassCode: " + ClassCodes)
    print("LandAcres: " + LandAcres)
                                              #string replace below every time you see a comma replace with a "|""
    f.write(OBJECTID + "," + ParcelID.replace(",", "|") + "," + Owner + "," + Address + "," + OwnerAddr1 + "," + OwnerAddr2 + "," + ClassCode + "," + LandAcres + "\n")

f.close()

print(soup)
