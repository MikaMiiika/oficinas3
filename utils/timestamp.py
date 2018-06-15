import time
import pytz, datetime

def timeToTimestamp(t = '2018-06-14 15:53:45'):
    local = pytz.timezone("America/Sao_Paulo")
    naive = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    t = str(utc_dt).split('+')[0]
    timestamp = time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S'))
    return timestamp

def timestampToTime(timestamp = 1526237625):
    t = time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
    return t

def secondsToHours(s):
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    timeString = "%d:%02d:%02d" % (h, m, s)
    return timeString

print(timeToTimestamp())