import pickle
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app=FastAPI()
model=joblib.load("modelN.pkl")
templates=Jinja2Templates(directory="templates")

with open("sdicti.json","r") as f:
  features=json.load(f)
features=dict(features)
#print(type(model.predict([[1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0.51, 0.107, 0, 0, 0, 0, 1, 0, 0]])))
print(features.keys())

@app.get("/" ,response_class=HTMLResponse)
async def home(request:Request):
  return templates.TemplateResponse("index.html",{"request": request,"features":features})

@app.post("/predict/",response_class=HTMLResponse)
async def predict(request:Request):
    form = await request.form()
    features1 = dict(form)
    
##    try:
##        featuresN=[int(float(x)) for x in features.split()]
##    except ValueError:
##        return templates.TemplateResponse(
##            "index2.html",{"request":request,"prediction":featuresNN})
##    if len(featuresN)!=23:
##        return templates.TemplateResponse("index2.html",{"request":request,"prediction":message})


    
    fet=[int(float(x)) for x in list(features1.values())]
    message = list(model.predict([fet]))
    if message==[1]:
          message="User will Churn"
    else:
       message="User will Not churn"
    return templates.TemplateResponse("index.html",{"request":request,"prediction":message,"features":features})                              
















