import requests
import threading
import json
from datetime import date

def get_info():
    URL='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin'
    pincode='560034'
    #today=date.today()
    #DATE=today.strftime("%d-%m-%Y")
    DATE='21-04-2021'
    HEADERS={'Accept-Language':'en_US','accept':'application/json','User-agent':'Mozilla/5.0'}
    PARAMS={'pincode':pincode,'date':DATE}
    r=requests.get(url=URL,headers=HEADERS,params=PARAMS)
    if(r):
        data=r.json()
        for key,value in data.items():
            for i in value:
                print('Centre ID',i['center_id'],i['name'],i['district_name'],i['block_name'],i['pincode'],i['from'],i['to'],i['fee_type'])
                for k in i['sessions']:
                    if(k['available_capacity']>0 and k['min_age_limit']<=45):
                        print(k['date'],'Available Capacity=>',k['available_capacity'],'Min.Age=>',k['min_age_limit'],k['vaccine'],'Timeslots=>',k['slots'])
                    else:
                        print("No Slots available")
                print()
    else:
        print("No response")
       

if __name__=='__main__':
    get_info()
    #threads=[]
    #for i in range(3):
    #    t=threading.Thread(target=get_info)
    #    t.daemon=True
    #    threads.append(t)
    #for i in range(3):
    #    threads[i].start()
    #for i in range(3):
    #    threads[i].join()

