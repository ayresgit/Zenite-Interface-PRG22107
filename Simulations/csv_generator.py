import csv
import pandas as pd
import numpy as np

header = ['time','Latitude','longitude','Voltage1','Voltage2','Voltage3','heading','yaw','pitch','row']

c1 = pd.Series(np.arange(start=0, stop=60*5, step=0.01, dtype=float), name = "Time")                   # 300/0.01 = 30000 
c2 = pd.Series(np.arange(start=2735, stop=2738, step=0.0001, dtype=float), name = "Latitude")          # 3/30000 = 0.0001 
c3 = pd.Series(np.arange(start=4834, stop=4837, step=0.0001, dtype=float), name = "Longitude")         # 3/30000 = 0.0001
c4 = pd.Series(np.arange(start=13.5, stop=9.5, step=-0.000133333, dtype=float), name = "Voltage1")      # 4/30000
c5 = pd.Series(np.arange(start=13.5, stop=9.5, step=-0.000133333, dtype=float), name = "Voltage2")      # 4/30000
c6 = pd.Series(np.arange(start=13.5, stop=9.5, step=-0.000133333, dtype=float), name = "Voltage3")      # 4/30000

c1 = c1.round(6)
c2 = c2.round(6)
c3 = c3.round(6)
c4 = c4.round(3)
c5 = c5.round(3)
c6 = c6.round(3)


with open('logger_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    pd.concat([c1,c2,c3,c4,c5,c6], axis=1).to_csv(f, header=False)
