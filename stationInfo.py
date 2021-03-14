from math import radians
from math import cos
from math import sin
from math import acos

class StationInfo:
    def __init__(self, id, latitude, longitude, elevation, state, name, line):
        self.line = line
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.state = state
        self.name = name

    def getDistance(self, latitude, longitude):
        return calculateLatitudeLongitudeDistance(self.latitude, self.longitude, latitude, longitude)

def calculateLatitudeLongitudeDistance(latitudeA, longitudeA, latitudeB, longitudeB):
    EARTH_RADIUS_KM = 6378.8

    latitudeARad = radians(latitudeA)
    longitudeARad = radians(longitudeA)

    latitudeBRad = radians(latitudeB)
    longitudeBRad = radians(longitudeB)

    return EARTH_RADIUS_KM * acos(sin(latitudeARad) * sin(latitudeBRad) + cos(latitudeARad) * cos(latitudeBRad) * cos(longitudeBRad - longitudeARad))