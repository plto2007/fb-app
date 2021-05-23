from requests import get
from bs4 import BeautifulSoup
from json import dumps

def Update(file):
        req=get("https://www.worldometers.info/coronavirus/")

        p=req.content.decode()    
        soup=BeautifulSoup(p, 'html.parser')
        soup=soup.find_all("table",id="main_table_countries_today")[0]
                
        tbrows=soup.find_all("tr")

        to_zero=lambda st:st if st else "0"

        attrs=["Total cases","New cases","Total deaths","New deaths","Total recovered","Active cases","Serious cases" ,"Total cases per 1 million"]
        dic={}
        dic["infected"] = []
        for i in tbrows:
            data=[]
            for dt in i.find_all("td"):
                data.append(dt.get_text().replace("Total","Worldwide").replace(":", ""))
            try:
                dic[data[0]]={p:to_zero(a) for p,a in zip(attrs,data[1:])}
                dic["infected"].append(data[0]) 
            except:
                pass
        with open(file,"w") as fd:
            fd.write(dumps(dic))
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
        
block = BlockingScheduler()

@block.scheduled_job("interval", minutes=1)
def job():
    print("Updated!", file=sys.stdout)
    Update("main_data.json")
        
if __name__=="__main__":
        block.start()
