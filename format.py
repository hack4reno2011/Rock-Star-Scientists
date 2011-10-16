import csv
from datetime import datetime
import time
filenames = ['CAD100620111108.csv', 'CAD100620111120.csv', 'CAD100620111152.csv', 'CAD100620111207.csv', 'CAD100620111221.csv', 'CAD100620111237.csv', 'CAD100620111250.csv', 'CAD100620111307.csv', 'CAD100620111321.csv', 'CAD100620111339.csv', 'CAD100620111352.csv', 'CAD100620111407.csv', 'CAD100620111422.csv', 'CAD100620111436.csv', 'CAD100620111453.csv', 'CAD100620111507.csv', 'CAD100620111522.csv', 'CAD100620111537.csv', 'CAD100620111552.csv', 'CAD100620111606.csv', 'RMS100420110105.csv', 'RMS100420111306.csv', 'RMS100520110105.csv', 'RMS100520111305.csv', 'RMS100620110105.csv', 'RMS100620111305.csv']


filePaths = []
filename = '/Users/glennwil/Documents/Code/Hack4Reno/hackDay/Rock-Star-Scientists/GeoRelevantData/Reno-Crime-Reports/data/'

for i, file in enumerate(filenames):
  path = filename + str(filenames[i])
  filePaths.append(path)

track = 0

for j, file in enumerate(filePaths):
  with open(filePaths[j], 'U') as f:
    reader = csv.reader(f)
    for row in reader:
      time_tuple = datetime(int(row[2][4:8]), int(row[2][0:2]), int(row[2][2:4]),int(row[3][0:2]), int(row[3][2:4]), int(row[3][4:6]) )
      # year mmonth day hour min sec
      date_str = time_tuple.strftime("%Y-%m-%d %H:%M:%S")
      track += 1
      print row[1] + ' ' + date_str + ' : line-' + str(track)