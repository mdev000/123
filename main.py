import os
from datetime import date, time, datetime
import datetime
import random

total_day = 100 #total days back
commit_frequency = 20 #commit time per day
repo_link = "https://github.com/mdev000/123.git"

tl = total_day #time day
ctr = commit_frequency

now = datetime.datetime.now()

f = open("commit.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

pointer = 0

while tl > 0:
    ct = random.randint(1, commit_frequency)
    random_number = random.randint(1, 10)
    while ct > 0 and random_number < 6:
        f = open("commit.txt", "a+")
        l_date = now + datetime.timedelta(days=-pointer)
        formatdate = l_date.strftime("%Y-%m-%d")
        f.write(f"commit ke {ctr}: {formatdate}\n")
        f.close()
        os.system("git add .")
        os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"commit ke {ctr}\"")
        print(f"commit ke {ctr}: {formatdate}")
        ct-=1
        ctr+=1
    pointer+=1
    tl-=1

os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")