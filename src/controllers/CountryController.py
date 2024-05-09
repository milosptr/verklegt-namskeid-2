from src.models import Country


class CountryController:
    def __init__(self):
        self.countryService = Country()

    def get_countries(self):
        return self.countryService.get_all()
