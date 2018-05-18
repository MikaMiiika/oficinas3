import time

def timeToTimestamp(t = '13/05/2018 15:53:45'):
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