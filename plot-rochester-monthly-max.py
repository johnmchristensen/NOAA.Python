from stationData import convertFromTenthsOfCelciusToFarenheit
from stationData import NO_DATA
from ghcnFTP import getStation
from math import sqrt
from matplotlib import pyplot as plt

def getAverage(d):
    convertedData = [round(convertFromTenthsOfCelciusToFarenheit(i)) for i in d.data if i != NO_DATA] 
    return round(sum(convertedData) / len(convertedData), 2)

def plotYear(axes, stationData, year):
    maxAverage = [(i.month, getAverage(i)) for i in stationData._data["TMAX"] if i.year == year]
    axes.plot([i[0] for i in maxAverage], [i[1] for i in maxAverage], label=year)

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

plotMonthlyMaxTemperatureAverageForEachYear(getStation("USW00014768"))