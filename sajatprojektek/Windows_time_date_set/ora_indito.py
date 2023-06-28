import ntplib
from datetime import datetime, timezone, timedelta
import os
import time



def jelenlegiido_ora():
    client = ntplib.NTPClient()
    response = client.request('hu.pool.ntp.org')
    current_time = datetime.fromtimestamp(response.tx_time, tz=timezone(timedelta(hours=2)))
    formatted_time = current_time.strftime('%H:%M:%S')
    return formatted_time

def jelenlegi_datum():
    client = ntplib.NTPClient()
    response = client.request('hu.pool.ntp.org')
    current_time = datetime.fromtimestamp(response.tx_time, tz=timezone(timedelta(hours=2)))
    formatted_time = current_time.strftime('%y-%m-%d')
    return formatted_time


os.system("time " + str(jelenlegiido_ora()))
time.sleep(0.5)
os.system("date " + str(jelenlegi_datum()))

