from fastapi import FastAPI

app = FastAPI() 

@app.get('/health')
def get_health_status():
    return {
        "statuscode": 200
    }

@app.get('/{userId}')
def get_userId(userId: int):
    return {
        "userId": userId
    }

