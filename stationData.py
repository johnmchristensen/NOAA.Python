class Indexes:
    YEAR = 11
    MONTH = 15
    ELEMENT_NAME = 17
    START_DATA = 21

DATA_SIZE = 8
VALUE_LENGTH = 5
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

    def parseData(self, line):
        year = int(line[Indexes.YEAR: Indexes.MONTH])
        month = int(line[Indexes.MONTH: Indexes.ELEMENT_NAME])
        element = line[Indexes.ELEMENT_NAME: Indexes.START_DATA]
        data = [int(line[i: i + DATA_SIZE][0: VALUE_LENGTH]) for i in range(Indexes.START_DATA, len(line), DATA_SIZE)]

        self.addData(element, MonthData(year, month, data, line))

class StationData:
    def __init__(self, year, month, dataType, dataValues, line):
        self.year = year
        self.month = month
        self.dataType = dataType
        self.dataValues = dataValues
        self.line = line

def convertFromTenthsOfCelciusToFarenheit(temp):
    if (temp == NO_DATA):
        return NO_DATA

    return (temp / 10) * (9/5) + 32