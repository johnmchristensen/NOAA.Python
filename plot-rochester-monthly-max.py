from ftplib import FTP
from stationData import Station
from stationData import convertFromTenthsOfCelciusToFarenheit
from stationData import NO_DATA
from math import sqrt
from matplotlib import pyplot as plt

def getAverage(d):
    convertedData = [round(convertFromTenthsOfCelciusToFarenheit(i)) for i in d.data if i != NO_DATA] 
    return round(sum(convertedData) / len(convertedData), 2)

def plotYear(axes, stationData, year):
    maxAverage = [(i.month, getAverage(i)) for i in stationData._data["TMAX"] if i.year == year]
    axes.plot([i[0] for i in maxAverage], [i[1] for i in maxAverage], label=year)

def getStation():
    ftp = FTP("ftp.ncdc.noaa.gov")
    ftp.login()
    ftp.cwd("pub/data/ghcn/daily/all")

    station = Station("USW00014768")
    ftp.retrlines("RETR USW00014768.dly", lambda l: station.parseData(l))
    
    return station

def plotMonthlyMaxTemperatureAverageForEachYear(stationData):
    years = list(set([i.year for i in stationData._data["TMAX"]]))
    years.sort()

    fig, axes = plt.subplots()

    for year in years:
        plotYear(axes, stationData, year)

    axes.set_xlabel("Month")
    axes.set_ylabel("Avg Max Temperature (F)")
    axes.set_title("Rochester: Average Max Temperature Per Month Per Year")
    plt.show()

plotMonthlyMaxTemperatureAverageForEachYear(getStation())