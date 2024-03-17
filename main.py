import requests
import datetime as dt
APP_ID ="65c291d3"
API_KEY="1dcddc7322f5e9ad91dc3e8b75e46ab9"
end_point ="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT= "https://api.sheety.co/992c979c61e12759d7b9b39c41edb933/myWorkouts/sheet1"
TOKEN= "Bearer knasncjkdbsvisbvoncnojbsdvosovknodsdvnnsovknonsdvn"
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
