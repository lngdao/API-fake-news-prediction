
def transformData(data):
  return {"message": "success", "code": 1, "data": data}

def transformError(error):
  return {"message": error, "code": 0}