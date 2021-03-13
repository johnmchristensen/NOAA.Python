from ftplib import FTP
from stationData import Station
from stationData import convertFromTenthsOfCelciusToFarenheit
from stationData import NO_DATA
from math import sqrt
from matplotlib.pyplot import pyplot

ftp = FTP("ftp.ncdc.noaa.gov")
ftp.login()
ftp.cwd("pub/data/ghcn/daily/all")

station = Station("USW00014768")
ftp.retrlines("RETR USW00014768.dly", lambda l: station.parseData(l))

def getAverage(d):
    convertedData = [round(convertFromTenthsOfCelciusToFarenheit(i)) for i in d.data if i != NO_DATA] 
    return round(sum(convertedData) / len(convertedData), 2)

maxAverage = [(i.month, getAverage(i)) for i in station._data["TMAX"] if i.year == "2020"]
print(maxAverage)


# for d in [i for i in station._data["TMAX"] if i.year == "2020"]:
#     convertedData = [round(convertFromTenthsOfCelciusToFarenheit(i)) for i in d.data if i != NO_DATA] 
#     avg = round(sum(convertedData) / len(convertedData), 2)
#     variance = sum([(i - avg)**2 for i in convertedData]) / len(convertedData)
#     standardDev = sqrt(variance)
#     print(d.month, d.year, max(convertedData), min(convertedData), avg, variance, standardDev)