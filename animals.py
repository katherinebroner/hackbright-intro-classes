class Animals(object):
    def __init__ (self, animal, fur_or_no_fur, meals_per_day):
        self.animal = animal
        self.fur_or_no_fur = fur_or_no_fur
        self.meals_per_day = meals_per_day
    def has_fur(self):
        if self.fur_or_no_fur == "fur":
            print True
        else: 
            print False
    def weight_of_meals_per_day(self, weight_of_one_meal_in_ounces):
        total_weight = self.meals_per_day * weight_of_one_meal_in_ounces
        print self.animal, "eats", total_weight, "ounces of food per day."

cat = Animals("cat", "fur", 3)
dog = Animals("dog", "fur", 2)
cat.weight_of_meals_per_day(2)
dog.weight_of_meals_per_day(4)
