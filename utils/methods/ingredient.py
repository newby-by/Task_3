from .base_method import BaseMethod


class IngredientMethod(BaseMethod):
    BASE_URL = 'https://stellarburgers.education-services.ru/api'
    INGREDIENT_URL = BASE_URL + '/ingredients'

    def get_ingredients(self, headers=None) -> list:
        response = self.get(
            headers=headers
        )
        return response.json().get('data')
