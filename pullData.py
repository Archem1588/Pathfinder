import urllib.request

url = "http://data.vancouver.ca/download/kml/bikeways.kmz"
print("why")

def downloadData():
    print("hello")
    urllib.request.urlretrieve(url, "bikeways.kmz")

downloadData()

