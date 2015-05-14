import sys
import csv
import dateutil.parser
import time
from math import fabs, radians, cos, sin, asin, sqrt

def compute_speed(lat0, lon0, tmstp0, lat1, lon1, tmstp1):
  lon0, lat0, lon1, lat1 = map(radians, [lon0, lat0, lon1, lat1])
  dlon = lon1 - lon0 
  dlat = lat1 - lat0 
  a = sin(dlat/2)**2 + cos(lat0) * cos(lat1) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a)) 
  kms = 6367. * c
  
  hours = fabs(tmstp1 - tmstp0)/3600.
  if hours == 0.:
    return 0.
  return kms/hours

new_lines = [["Ano","DiaMes","LinhaAccu","Linhapred","LatitudePonto_19","LongitudePonto_12","TimeStamp_15","LatitudePonto_18","LongitudePonto_0","LongitudePonto_1","LongitudePonto_2","LongitudePonto_3","TimeStamp_2","TimeStamp_3","TimeStamp_0","TimeStamp_1","LongitudePonto_8","LongitudePonto_9","LatitudePonto_17","Onibus","LongitudePonto_10","TimeStamp_8","TimeStamp_9","TimeStamp_18","TimeStamp_19","LongitudePonto_11","Mes","LongitudePonto_17","TimeStamp_10","TimeStamp_11","TimeStamp_12","LongitudePonto","TimeStamp_14","Linha","TimeStamp_16","TimeStamp_17","TimeStamp_6","LongitudePonto_7","TimeStamp_7","TimeStamp","LongitudePonto_19","TimeStamp_4","LatitudePonto_13","LatitudePonto_14","TimeStamp_5","LatitudePonto","LatitudePonto_15","LongitudePonto_4","ID","LongitudePonto_18","LongitudePonto_5","Hora","Velocidade","TimeStamp_13","LongitudePonto_6","LatitudePonto_10","DescricaoPonto","LatitudePonto_16","LatitudePonto_11","NomePonto","LongitudePonto_13","LatitudePonto_8","LatitudePonto_9","LongitudePonto_16","LatitudePonto_12","LongitudePonto_14","LongitudePonto_15","LatitudePonto_2","LatitudePonto_3","LatitudePonto_0","LatitudePonto_1","LatitudePonto_6","LatitudePonto_7","LatitudePonto_4","LatitudePonto_5","Speed_0","Speed_1","Speed_2","Speed_3","Speed_4","Speed_5","Speed_6","Speed_7","Speed_8","Speed_9","Speed_10","Speed_11","Speed_12","Speed_13","Speed_14","Speed_15","Speed_16","Speed_17","Speed_18","Speed_19"]]

with open(sys.argv[1], 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    speed = "0.0"
    line = []
    fields = new_lines[0]
    for f in fields:
      try:
        line.append(row[f])
      except:
        continue
    for i in range(19):
       lat0 = row['LatitudePonto_' + str(i)]
       lon0 = row['LongitudePonto_' + str(i)]
       tmstp0 = time.mktime(dateutil.parser.parse(row['TimeStamp_' + str(i)]).timetuple()) 
       lat1 = row['LatitudePonto_' + str(i + 1)]
       lon1 = row['LongitudePonto_' + str(i + 1)]
       tmstp1 = time.mktime(dateutil.parser.parse(row['TimeStamp_' + str(i + 1)]).timetuple()) 
       speed = compute_speed(float(lat0), float(lon0), float(tmstp0), float(lat1), float(lon1), float(tmstp1))
       line.append(str(speed))
    line.append(str(speed))
    new_lines.append(line)

for n in new_lines:
  print ",".join(n)
