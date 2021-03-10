class Indexes:
    LATITUDE_INDEX = 11
    LONGITUDE_INDEX = 21
    ELEVATION_INDEX = 31
    STATE_INDEX = 38
    NAME_INDEX = 41
    GSN_FLAG_INDEX = 72
    HCN_CRN_INDEX = 76
    WMO_INDEX = 80

class StationInfoKeys:
    ID = "id"
    Latitude = "latitude"
    Longitude = "longitude"
    Elevation = "elevation"
    State = "state"
    Name = "name"
    IsGSN = "isgsn"
    HCN_CRN = "hcn_crn"
    WMOId = "wmoid"
    FULL_LINE = "fullline"

def parseStationInfo(line):
    stationInfo = {}
    stationInfo[StationInfoKeys.FULL_LINE] = line
    stationInfo[StationInfoKeys.ID] = line[0: Indexes.LATITUDE_INDEX - 1]
    stationInfo[StationInfoKeys.Latitude] = line[Indexes.LATITUDE_INDEX: Indexes.LONGITUDE_INDEX - 1]
    stationInfo[StationInfoKeys.Longitude] = line[Indexes.LONGITUDE_INDEX: Indexes.ELEVATION_INDEX - 1]
    stationInfo[StationInfoKeys.Elevation] = line[Indexes.ELEVATION_INDEX: Indexes.STATE_INDEX - 1]
    stationInfo[StationInfoKeys.State] = line[Indexes.STATE_INDEX: Indexes.NAME_INDEX - 1]
    stationInfo[StationInfoKeys.Name] = line[Indexes.NAME_INDEX: Indexes.GSN_FLAG_INDEX - 1]

    return stationInfo

    