import time
from datetime import datetime as dt


# hosts file is in
# windows
hostsPathWindows = r"C:\Windows\System32\drivers\etc\hosts"
# unix
hostsPathUnix = "/etc/hosts"

hosts = hostsPathWindows
# hosts = "hosts"

redirect = "127.0.0.1"

websitesList = [
    "www.facebook.com",
    "facebook.com",
    "www.instagram.com",
    "instagram.com",
    "twitter.com"
]

fromHour = 9
toHour = 18

while True:
    t = dt.now().hour
    if fromHour <= t and t <= toHour:
        print("no distractions", t)
        with open(hosts, 'r+') as file:
            content = file.read()
            for website in websitesList:
                if website in content:
                    pass
                else:
                    file.seek(0,2)
                    file.write(redirect + "   " + website + "\n")
    else:
        print('free time: ', t)
        with open(hosts, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websitesList):
                    file.write(line)
                file.truncate()
    time.sleep(1) 
