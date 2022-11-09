from wakeonlan import send_magic_packet
import pandas as pd
import os, sys


try: # running using executable
    path = sys._MEIPASS

except: # running using .py sript
    path = os.path.abspath('.')

csv_path = os.path.join(path, 'kompy.csv') # valid path of the csv file


data = pd.read_csv(csv_path)

for index, row in data.iterrows():
    send_magic_packet(row['mac'], ip_address = row['ip'])