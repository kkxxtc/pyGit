def toLower(str):
    someString = (str.lower())
    return someString
def toUpper(str):
    someString = (str.upper())
    return someString
allDown = ['HELLO', 'MY', 'FRIEND']
allUp = ['bye','my','friend']
down = list(map(toLower,allDown))
up = list(map(toUpper,allUp))