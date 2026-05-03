from faker import Faker

from utils.methods.ingredient import IngredientMethod


BASE_URL = 'https://stellarburgers.education-services.ru'
ACCOUNT_URL = BASE_URL + '/account/profile'
CONSTRUCTOR_URL = BASE_URL + '/'
FORGOT_PASSWORD_URL = BASE_URL + '/forgot-password'
LOGIN_URL = BASE_URL + '/login'
RESET_PASSWORD_URL = BASE_URL + '/reset-password'
FEED_URL = BASE_URL + '/feed'


class UserData:

    def __init__(self, locale='en_US'):
        self.faker = Faker(locale)
        self.extra_word = (f'{self.faker.word()}'
                           f'{self.faker.random_int(min=10, max=100)}')
        self.user = {
            'email': None,
            'password': None,
            'name': None,
        }

    @property
    def email(self):
        email_split = self.faker.email().split('@')
        email_split[0] = email_split[0] + self.extra_word + '@'
        return f'{"".join(email_split)}'

    @property
    def password(self):
        return self.faker.password()

    @property
    def name(self):
        return f'{self.faker.name()}{self.extra_word}'

    @property
    def with_all_data(self):
        self.user['email'] = self.email
        self.user['password'] = self.password
        self.user['name'] = self.name
        return self.user

    @property
    def without_email(self):
        self.user['password'] = self.password
        self.user['name'] = self.name
        return self.user

    @property
    def without_password(self):
        self.user['email'] = self.email
        self.user['name'] = self.name
        return self.user

    @property
    def without_name(self):
        self.user['email'] = self.email
        self.user['password'] = self.password
        return self.user

    @staticmethod
    def data_for_login(user_data):
        return {
            'email': user_data['email'],
            'password': user_data['password'],
        }

    @staticmethod
    def change_email(user_data, word='1'):
        user = user_data['email'].split('@')
        user[0] = user[0] + word + '@'
        user_data['email'] = "".join(user)
        return user_data

    @staticmethod
    def change_password(user_data, word='1'):
        user_data['password'] = user_data['password'] + word
        return user_data


class OrderData:

    def __init__(self):
        self.faker = Faker()
        self.ingredients = {"ingredients": []}
        self._data = IngredientMethod(
            url=IngredientMethod.INGREDIENT_URL).get_ingredients()
        (self._buns,
         self._sauce,
         self._main,
         self._unknown) = OrderData._get_data(self._data)
        if self._unknown != []:
            raise ValueError(f"Database has unknown type {self._unknown}")

    @property
    def empty_order(self):
        return self.ingredients

    @property
    def wrong_id(self):
        self.ingredients = {"ingredients": ["0"]}
        return self.ingredients

    @property
    def buns_only(self):
        self.ingredients["ingredients"] = [
            self.faker.random_element(self._buns).get('_id')
        ]
        return self.ingredients

    @property
    def buns_and_sauce(self):
        self.ingredients["ingredients"] = [
            self.faker.random_element(self._buns).get('_id'),
            self.faker.random_element(self._sauce).get('_id')
        ]

        return self.ingredients

    @staticmethod
    def _get_data(_data):
        _buns = []
        _sauce = []
        _main = []
        _ = []

        for el in _data:
            if el['type'] == 'bun':
                _buns.append(el)
            elif el['type'] == 'sauce':
                _sauce.append(el)
            elif el['type'] == 'main':
                _main.append(el)
            else:
                _.append(el)
        return _buns, _sauce, _main, _
