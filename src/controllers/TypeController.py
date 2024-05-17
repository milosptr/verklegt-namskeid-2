from src.models import Type


class TypeController:
    def __init__(self):
        self.type_service = Type()

    def get_types(self):
        return self.type_service.get_all()


