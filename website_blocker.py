import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"   # hosts path may be diff on diff computers
redirect = "127.0.0.1"  # localhost
with open("websites.txt", 'r') as file:
    website_list = file.readlines()

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                          dt.now().day, 20):
        print("Working hours...")   # prints only in terminal
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print("Non-working hours...")   # prints only in terminal
        with open(hosts_path, 'r+') as file:
            content = file.readlines()  # coverts the file to a list of each separate line as a string
            file.seek(0)    # takes the pointer before the first character of file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
