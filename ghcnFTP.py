from ftplib import FTP
from stationInfo import StationInfo
from stationData import Station
from stationData import MonthData

def getAllStationInfo():
    class Indexes:
        LATITUDE_INDEX = 11
        LONGITUDE_INDEX = 21
        ELEVATION_INDEX = 31
        STATE_INDEX = 38
        NAME_INDEX = 41
        GSN_FLAG_INDEX = 72
        HCN_CRN_INDEX = 76
        WMO_INDEX = 80

    # Create a connection to the NOAA site and download the stations file.
    ftp = FTP("ftp.ncdc.noaa.gov")
    ftp.login()
    ftp.cwd("pub/data/ghcn/daily")
    
    stationInfos = []

    def parseLine(line):
        id = line[0: Indexes.LATITUDE_INDEX - 1]
        latitude = float(line[Indexes.LATITUDE_INDEX: Indexes.LONGITUDE_INDEX - 1])
        longitude = float(line[Indexes.LONGITUDE_INDEX: Indexes.ELEVATION_INDEX - 1])
        elevation = float(line[Indexes.ELEVATION_INDEX: Indexes.STATE_INDEX - 1])
        state = line[Indexes.STATE_INDEX: Indexes.NAME_INDEX - 1]
        name = line[Indexes.NAME_INDEX: Indexes.GSN_FLAG_INDEX - 1]

        return StationInfo(id, latitude, longitude, elevation, state, name, line)

    ftp.retrlines("RETR ghcnd-stations.txt", lambda l: stationInfos.append(parseLine(l)))

    return stationInfos

def getStation(stationId):
    class Indexes:
        YEAR = 11
        MONTH = 15
        ELEMENT_NAME = 17
        START_DATA = 21

    DATA_SIZE = 8
    VALUE_LENGTH = 5

    ftp = FTP("ftp.ncdc.noaa.gov")
    ftp.login()
    ftp.cwd("pub/data/ghcn/daily/all")

    station = Station(stationId)

    def parseData(line):
        year = int(line[Indexes.YEAR: Indexes.MONTH])
        month = int(line[Indexes.MONTH: Indexes.ELEMENT_NAME])
        element = line[Indexes.ELEMENT_NAME: Indexes.START_DATA]
        data = [int(line[i: i + DATA_SIZE][0: VALUE_LENGTH]) for i in range(Indexes.START_DATA, len(line), DATA_SIZE)]

        station.addData(element, MonthData(year, month, data, line))

    ftp.retrlines(f"RETR {stationId}.dly", lambda l: parseData(l))
    
    return station