NO_DATA = -9999

class MonthData:
    def __init__(self, year, month, data, line):
        self.year = year
        self.month = month
        self.data = data
        self.line = line

class Station:
    def __init__(self, stationId):
        self.id = stationId
        self._data = {}

    def addData(self, element, monthData):
        if (element in self._data):
            self._data[element].append(monthData)
        else:
            self._data[element] = [monthData]

def convertFromTenthsOfCelciusToFarenheit(temp):
    if (temp == NO_DATA):
        return NO_DATA

    return (temp / 10) * (9/5) + 32