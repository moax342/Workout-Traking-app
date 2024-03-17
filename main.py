import requests
import datetime as dt
APP_ID ="your id"
API_KEY="your key"
ACESS_KEY="Your key"
end_point ="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT= f"https://api.sheety.co/{ACESS_KEY}/myWorkouts/sheet1"
TOKEN= "Bearer your token"
header ={
    'x-app-id':APP_ID,
    "x-app-key":API_KEY
}

head ={
    "Authorization":TOKEN
}
time = dt.datetime.now()
exercise_prams={
    "query":input("Enter what you did today?")
}
response = requests.post(url=end_point,json=exercise_prams, headers=header)

workout_data ={
    "sheet1":{
        "date":time.strftime("%G/%m/%d"),
        "time":time.strftime("%I:%M:%S"),
        "exercise":response.json()["exercises"][0]["name"],
        "duration":response.json()["exercises"][0]["duration_min"],
        "calories":response.json()["exercises"][0]["nf_calories"]
    }
}

workout=requests.post(SHEET_ENDPOINT, json=workout_data, headers=head)
