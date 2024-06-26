from src.models import Category


class CategoryController:
    def __init__(self):
        self.categoryService = Category()

    def get_categories(self):
        return self.categoryService.get_all()

    def create_category(self, name: str):
        return self.categoryService.create(name)


