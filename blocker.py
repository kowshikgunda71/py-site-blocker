import time
from datetime import datetime as dt  # importing date time module as dt
host_path = "your host path "  # give your real path where your host is there
redirect = "127.0.0.1"
website_list = ["sitestoblock.com", "game.com"]  # website list to block
host_tmp = "hosts"  # dummy file of hosts
while True:
    #time check if it's time or not 
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 10):
        print("it's on and please work ")
        # for test i have given a temp hosts file in same file system but change that loop to regular host path 
        # opend with wite and read op
        with open(host_tmp, "r+") as file:

            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n") #string formating as reqired 

    else:
        with open(host_tmp, "r+") as file:
            content = file.readlines()
            # keep the pointer back to 0 with seek
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # remove extra lines using trunc
            file.truncate()

        print("chill time ")
    time.sleep(5)
