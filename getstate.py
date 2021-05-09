import requests
import sys
def get_state():
    URL='https://cdn-api.co-vin.in/api/v2/admin/location/states'
    HEADERS={'Accept-Language':'hi_IN','accept':'application/json','User-agent':'Mozilla/5.0'}
    r=requests.get(url=URL,headers=HEADERS)
    data=r.json()
    for key,value in data.items():
        if type(value) is not int :
            for i in value:
                #print(type(i))
                if sys.argv[1].upper().lower() in i['state_name'].upper().lower():
                    print('State ID=',i['state_id'],'for',i['state_name'])
                    #exit()
    
                
if __name__=='__main__':
    get_state()