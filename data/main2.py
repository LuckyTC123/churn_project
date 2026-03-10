import pickle
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app=FastAPI()
model=joblib.load("modelL.pkl")
templates=Jinja2Templates(directory="templates")

with open("sdict.json","r") as f:
  features=json.load(f)
features=dict(features)
#print(type(model.predict([[1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0.51, 0.107, 0, 0, 0, 0, 1, 0, 0]])))
print(features.keys())

@app.get("/" ,response_class=HTMLResponse)
async def home(request:Request):
  return templates.TemplateResponse("index3.html",{"request": request,"features":features})

@app.post("/predict/",response_class=HTMLResponse)
async def predict(request:Request):
    form = await request.form()
    features = dict(form)
    
##    try:
##        featuresN=[int(float(x)) for x in features.split()]
##    except ValueError:
##        return templates.TemplateResponse(
##            "index2.html",{"request":request,"prediction":featuresNN})
##    if len(featuresN)!=23:
##        return templates.TemplateResponse("index2.html",{"request":request,"prediction":"please 23"})


    
    fet=[int(float(x)) for x in list(features.values())]
    message = list(model.predict([fet]))
    return templates.TemplateResponse("index2.html",{"request":request,"prediction":message})                              
















