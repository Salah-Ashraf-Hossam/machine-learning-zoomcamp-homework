import pickle 

from model import normalize_record


with open("pipeline.bin", "rb") as model_file:
    pipeline = pickle.load(model_file)


CLIENT = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

record = normalize_record(CLIENT)

prediction = round (pipeline.predict_proba([record])[0, 1], 3)

print ({"conversion_probability": prediction, "conversion": prediction >= 0.5})