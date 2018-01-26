class Food:
    def __init__(self, name, calories):
        self.__name = name
        self.__calories = calories

    def set_name(self, name):
        self.__name = name

    def set_calories(self, calories):
        self.__calories = calories

    def get_name(self):
        return self.__name

    def get_calories(self):
        return self.__calories

def main():
    calories = {'Boiled Eggs':155, 'Fried Eggs':196, 'Whole Chicken':1070}

main()