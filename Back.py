import pymongo
from datetime import datetime
import pytz
import os

IST = pytz.timezone('Asia/Kolkata')
nowdatetime = datetime.now(IST)

cluster=cluster =MongoClient(os.environ.get('GithubCounter_URL'))
db=cluster['GithubHitsCounter']['Data']

def IncrementAndgetCount(request):
    if request.args.get("Username")!=None:
        if request.args.get("RepoName")!=None:
            count=0
            UserName=request.args.get("Username")
            RepoName=request.args.get("RepoName")
            if db.find_one({"UserName":UserName,"RepoName":RepoName}):
                if request.args.get("Counter")=="True":
                    db.update_one({"UserName":UserName,"RepoName":RepoName},
                                {
                                        "$inc": {
                                            "Counts": 1
                                        },
                                        "$push": {
                                            "DateAndTime":{
                                                "date":str(nowdatetime.now().date()),
                                                "time":str(nowdatetime.now().time())}
                                        }
                                })
                    return db.find_one({"UserName":UserName,"RepoName":RepoName})['Counts']
                else:
                    return db.find_one({"UserName":UserName,"RepoName":RepoName})['Counts']
            else:
                db.insert_one({
                    "UserName":UserName,
                    "RepoName":RepoName,
                    "Counts":1,
                    "DateAndTime":[{
                        "date":str(nowdatetime.now().date()),
                        "time":str(nowdatetime.now().time())
                    }]
                })
                return 1
        else:
            UserName=request.args.get("Username")
            if db.find_one({"OnlyUserName":UserName}):
                if request.args.get("Counter")=="True":
                    db.update_one({"OnlyUserName":UserName},
                                {
                                        "$inc": {
                                            "Counts": 1
                                        },
                                        "$push": {
                                            "DateAndTime":{
                                                "date":str(nowdatetime.now().date()),
                                                "time":str(nowdatetime.now().time())}
                                        }
                                })
                    return db.find_one({"OnlyUserName":UserName})['Counts']
                else:
                    return db.find_one({"OnlyUserName":UserName})['Counts']
            else:
                db.insert_one({
                    "OnlyUserName":UserName,
                    "Counts":1,
                    "DateAndTime":[{
                        "date":str(nowdatetime.now().date()),
                        "time":str(nowdatetime.now().time())
                    }]
                    
                })
                return 1
    else:
        return None
