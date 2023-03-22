import json

class User:
    FILTER_ATTRS = ["id", "first_name", "last_name", "sex", "rating_gte", "rating_lte", "birth_date", "primary_skills", "secondary_skill", "company", "active", "country", "language"]
    
    def __init__(self, data=None):
        self.id = data.get("id")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.sex = data.get("sex")
        self.rating = data.get("rating")
        self.birth_date = data.get("birth_date")
        self.primary_skills = json.dumps(data.get("primary_skills"))
        self.secondary_skills = json.dumps(data.get("secondary_skills"))
        self.company = data.get("company")
        self.active = data.get("active")
        self.country = data.get("country")
        self.language = data.get("language")
        self.times_searched = 0
