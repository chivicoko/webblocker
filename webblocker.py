import time
from datetime import datetime as dt

hosts_temp = 'hosts'
# hosts_path = r"C:\Users\veecee\Desktop\New system\Codeo\Python\[FreeTutorials.Us] Udemy - the-python-mega-course\12 Application 3 Building a Website Blocker\120 Hosts"
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com', 'pornographic videos']
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours...')
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write('\n' + redirect + ' ' + website)
    else:
        print('fun hours...')
    time.sleep(5)
