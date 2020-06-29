                  #--------------------------> 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             #the Offset= number below is where the 25 or 9 stepping value loop has to occur                      
# def GetURL():
#     # url = urllib.request.urlopen('https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&resultOffset=0&resultRecordCount=25')
#     # url = 'https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&result" + Offset + "&resultRecordCount=25'
#    
# frontend = "https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&result" + Offset + "&resultRecordCount=25"

#     request_string = urllib.request.urlopen
# frontend)
#     soup = bs.BeautifulSoup(request_string,'lxml')
#     return soup

# ChrisChooseNumber = 100


# if(OG_offsetNum < ChrisChooseNumber):
#     OG_offsetNum += 25
#     func = GetURL()
    
# test = GetURL()

# print(test)

#frontend = "https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&result" + Offset + "&resultRecordCount=25"

front = "https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&result"

OG_offsetNum = 0
while(OG_offsetNum <= 100):
    
    new_offsetNum = str(OG_offsetNum)
    Offset = "Offset=" + new_offsetNum
    backend = "&resultRecordCount=25"
    entire_URL = front + Offset + backend
    backend = backend + Offset
    p_soup = entire_URL
    OG_offsetNum += 25

    print(p_soup + "\n")



def input_URL():
    pass

def create_URLString():
    front_URL = "https://gismaps.fultoncountyga.gov/arcgispub/rest/services/PropertyMapViewer/PropertyMapViewer/MapServer/12/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A2041238.60861709%2C%22ymin%22%3A1366476.939475579%2C%22xmax%22%3A2318842.7752837567%2C%22ymax%22%3A1507622.7728089124%2C%22spatialReference%22%3A%7B%22wkid%22%3A102667%2C%22latestWkid%22%3A2240%7D%7D&geometryType=esriGeometryEnvelope&inSR=102667&outFields=*&orderByFields=OBJECTID%20ASC&outSR=102667&result"
    back_URL = "&resultRecordCount=25"
    Offset = "Offset=" + Get_Offset_val()
    entire_URL = front_URL + Offset + back_URL
    return entire_URL

def add_Offset_val(val_to_add):
    offset_value = Get_Offset_val + val_to_add
    return offset_value

def Get_Offset_val():
    Offset_val = 0
    return Offset_val

def incremenet_offest_val(value):
    return value

def main():
    Offset_val = 0
    inc_value = int(input("How much would you like to increment by?\t:"))
    top_value = int(input("What is the last offset value you want to go to?\t:"))

    if(Get_Offset_val() <= top_value):
        add_Offset_val(inc_value)

if __name__ == "__main__":
    main()