import json

from pyairtable import Api
from pyairtable.formulas import match

# Opens the file in read-only mode and assigns the contents to the variable cfg to be accessed further down
with open('config.json', 'r') as cfg:
  # Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
  data = json.load(cfg)

API_KEY  = data["API_KEY"]
#  print(API_KEY)
BASE_ID  = data["BASE_ID"]
#  print(BASE_ID)
TABLE_ID = data["TABLE_ID"]
#  print(TABLE_ID)

api   = Api(API_KEY)
table = api.table(BASE_ID, TABLE_ID)

formula = match({"Field": "Value"})

print(table.all(formula = formula))