from fastapi import FastAPI, Request
import motor.motor_asyncio
import pydantic
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
import  datetime 
import pytz

import requests

app = FastAPI()

origins = [
    "https://jw-lab-6-api.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://IOT_CLASS:iotclass@cluster0.irzkjxq.mongodb.net/?retryWrites=true&w=majority")
db = client.lab_6
states = db["state"]

pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str


sunset_api_endpoint = f'https://ecse-sunset-api.onrender.com/api/sunset' #from lab

sunset_api_response = requests.get(sunset_api_endpoint) #send get requests
sunset_api_data = sunset_api_response.json() #put requests RESPONSE/RESULTS into sunset Api

sunset_time = datetime.datetime.strptime(sunset_api_data['sunset'], '%Y-%m-%dT%H:%M:%S.%f').time() #decodes the results into readable manner
now_time = datetime.datetime.now(pytz.timezone('Jamaica')).time()#tells the time into the jamaican time zome


datetime1 = datetime.datetime.strptime(str(sunset_time),"%H:%M:%S") #sets the time so it can be compared 
datetime2 = datetime.datetime.strptime(str(now_time),"%H:%M:%S.%f") #set the now time so it can be compared

@app.get("/")
async def home():
    return {"LAB 6": "redirect to /api/state"}


@app.put("/api/temperature")  #put requests
async def toggle(request: Request): 
  state = await request.json() #wait for request
  state["light"] = (datetime1<datetime2) #compare the now and sunst time and give a true or false results
  state["fan"] = (float(state["temperature"]) >= 28.0) #same as above but tells if temperature is greater in true and false reulsts

  obj = await states.find_one({"the":"change"})
  
  if obj:
    await states.update_one({"the":"change"}, {"$set": state})
  else:
    await states.insert_one({**state, "the": "change"})
  new_obj = await states.find_one({"the":"change"}) 
  return new_obj,204



@app.get("/api/state")
async def get_state():
  state = await states.find_one({"the": "change"})
  
  state["fan"] = (float(state["temperature"]) >= 28.0) 
  state["light"] = (datetime1<datetime2)

  if state == None:
    return {"fan": False, "light": False}
  return state