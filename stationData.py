class Indexes:
    YEAR = 11
    MONTH = 15
    ELEMENT_NAME = 17
    START_DATA = 21

DATA_SIZE = 8
VALUE_LENGTH = 5

class StationData:
    def __init__(self, year, month, dataType, dataValues, line):
        self.year = year
        self.month = month
        self.dataType = dataType
        self.dataValues = dataValues
        self.line = line

def parseStationData(line):
    return StationData(line[Indexes.YEAR: Indexes.MONTH - 1], \
        line[Indexes.MONTH: Indexes.ELEMENT_NAME - 1], line[Indexes.ELEMENT_NAME: Indexes.START_DATA - 1], \
        [int(line[i: i + DATA_SIZE][0: VALUE_LENGTH]) for i in range(Indexes.START_DATA, len(line), DATA_SIZE)], \
        line)