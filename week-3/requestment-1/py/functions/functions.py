import json
from urllib import request

def getResults():
    url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
    with request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        data = json.loads(data)
        return data['result']['results']

def parseRegionFromAddress(address: str):
    return address[5:8]

def parseFileToFiles(file: str):
    files = file.split('https')[1:]
    return list(map(lambda file: 'https' + file, files))

def checkPostDateAfterSpecificYear(postDate: str, year: int):
    return int(postDate[0:4]) >= year

def checkRegionInAcceptableRegions(region, acceptableRegions: list):
    return region in acceptableRegions

def checkImgUrl(url: str):
    extension = url[url.rfind("."):]
    extension = extension.lower()
    return (extension.find('.bmp') >= 0 or
        extension.find('.jpg') >= 0 or
        extension.find('.png') >= 0)

def convertResultToRow(result):
    title = result['stitle']
    region = parseRegionFromAddress(result['address'])
    longitude = result['longitude']
    latitude = result['latitude']
    files = parseFileToFiles(result['file'])
    imgUrls = list(filter(lambda file: checkImgUrl(file), files))
    if len(imgUrls) == 0:
        print(result)
    return [title, region, longitude, latitude, imgUrls[0]]
