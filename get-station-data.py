from ftplib import FTP
from stationData import parseStationData

ftp = FTP("ftp.ncdc.noaa.gov")
ftp.login()
ftp.cwd("pub/data/ghcn/daily/all")

data = []
ftp.retrlines("RETR USW00014768.dly", lambda l: data.append(parseStationData(l)))

print(data[0].year)
print(data[0].month)
print(data[0].dataType)
print(data[0].dataValues)
print(data[0].line)