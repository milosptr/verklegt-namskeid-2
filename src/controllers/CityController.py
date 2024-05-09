from src.models import City


class CityController:
    def __init__(self):
        self.city_service = City()

    def get_all(self):
        return self.city_service.get_all()
