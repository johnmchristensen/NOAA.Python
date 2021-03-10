from ftplib import FTP
from stationInfo import parseStationInfo
from stationInfo import StationInfoKeys

# Create a connection to the NOAA site and download the stations file.
ftp = FTP("ftp.ncdc.noaa.gov")
ftp.login()
ftp.cwd("pub/data/ghcn/daily")
stationInfos = []

ftp.retrlines("RETR ghcnd-stations.txt", lambda l: stationInfos.append(parseStationInfo(l)))

rochesterStations = [x for x in stationInfos \
    if x[StationInfoKeys.State] == "NY" and "rochester gtr intl ap" in x[StationInfoKeys.Name].lower()][0]

print(rochesterStations[StationInfoKeys.FULL_LINE])
for i in rochesterStations:
    print(i, rochesterStations[i])
# SW0001476