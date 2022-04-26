def addOffsets(points, offsets):
    x, y = offsets
    return [(point[0] + x, point[1] + y) for point in points]

def reverseBoundX(points, xMax):
    return [(xMax - point[0], point[1]) for point in points]
    

def parsePrinterXY(printerData):
    xy = printerData.split('Count')[1].split('Z')[0].strip().replace('Y:', '').split(' ')[1:]
    return (float(xy[0]), float(xy[1]))
        
def isHomed(xy):
    x, y = xy
    tolerence = 0.03
    return x <= tolerence and x >= -tolerence and y <= tolerence and y >= -tolerence