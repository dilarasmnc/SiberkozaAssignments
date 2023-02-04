
import json

# Sample JSON
user_dsJSON ='{"first_name_ds": "Dilara", "last_name_ds": "Samancı", "age_ds": 30}'

# Parse to dict
user_ds = json.loads(user_dsJSON)

print(user_ds)
print(user_ds['first_name_ds'])

car_ds = {'make_ds': 'Ford', 'model_ds': 'Mustang', 'year_ds': 1970}

car_dsJSON = json.dumps(car_ds)

print(car_dsJSON)















