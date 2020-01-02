import billboard
import time
import csv

previousDate='2018-10-20'
ll=[]

def extract_billboard_top_100(previousDate):
    for k in range(10000):
        chart = billboard.ChartData('hot-100',previousDate)
        try:
            while chart.previousDate[:4]>='1990':
                ll1=[]
                time.sleep(2)
                chart = billboard.ChartData('hot-100', chart.previousDate)
                print("Correct",chart.date)
                for i in chart:
                    ll1.append(tuple((i.title,i.artist,chart.date)))
                ll.append(ll1)
        except:
            print(chart.date)
            previousDate=chart.date

date,bill_list=extract_billboard_top_100(previousDate)
with open("billboard.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(ll)
