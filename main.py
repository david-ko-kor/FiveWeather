
import requests
import os
from dotenv import load_dotenv
load_dotenv()
apikey=os.getenv("apikey")
lat=37.3514
lon=127.9453
url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}"
result=requests.get(url)
response=result.json()
print("현재시간",response['list'][0]['dt_txt'])
print("온도",response['list'][0]['main']['temp'])
print("체감온도",response['list'][0]['main']['feels_like'])
print("최고온도",response['list'][0]['main']['temp_max'])
print("습도",response['list'][0]['main']['humidity'])
print("기압",response['list'][0]['main']['pressure'])
print("풍속",response['list'][0]['wind']['speed'])
print("하늘",response['list'][0]['weather'][0]['description'])

# print("날씨:",response["weather"][0]["description"])
# print("현재온도:",response["main"]["temp"])
# print("체감온도",response["main"]["feels_like"])
# print("최저온도",response["main"]["temp_min"])
# print("최고온도",response["main"]["temp_max"])
# print("습도",response["main"]["humidity"])
# print("기압",response["main"]["pressure"])
# print("풍향",response["wind"]["deg"])
# print("풍속",response["wind"]["speed"])





# if os.path.isfile('wether.csv'):
#     os.remove('weather.csv')
# list=[]
# i=response['list'][0]
# print(i)


# for i in response['list']:
#     print(i)
    # print(i['dt_txt'],i['main']['temp'],i['main']['temp_min'],i['main']['temp_max'],i['main']['humidity'],i['weather'][0]['description'])
    # list.append(str(i['dt_txt'])+","+str(i['main']['temp'])+","+str(i['main']['temp_min'])+","+str(i['main']['temp_max'])+","+str(i['main']['humidity'])+","+str(i['weather'][0]['description']))

    # with open('weather.csv','a',encoding='utf-8') as f:
    #     f.write(str(i['dt_txt'])+","+str(i['main']['temp'])+","+str(i['main']['temp_min'])+","+str(i['main']['temp_max'])+","+str(i['main']['humidity'])+","+str(i['weather'][0]['description'])+"\n")





