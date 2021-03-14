from ghcnFTP import getAllStationInfo
from stationInfo import calculateLatitudeLongitudeDistance

stationInfos = getAllStationInfo()

rochesterStations = [x for x in stationInfos \
    if x.state == "NY" and "rochester gtr intl ap" in x.name.lower()]

currentLatitude = 43.137468
currentLongitude = -77.538996

for i in stationInfos:
    if (i.getDistance(currentLatitude, currentLongitude) <= 25):
        print(i.id, i.name, i.getDistance(currentLatitude, currentLongitude))
# SW0001476