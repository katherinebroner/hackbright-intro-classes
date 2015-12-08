class Food(object):
    def __init__ (self, recipe_name, step_1, step_2, cook_time_for_one_in_minutes):
        self.recipe_name = recipe_name
        self.step_1 = step_1
        self.step_2 = step_2
        self.cook_time_for_one_in_minutes = cook_time_for_one_in_minutes
    def print_recipe(self):
        print self.recipe_name
        print "======"
        print self.step_1
        print self.step_2
    def total_cook_time(self, how_many_want_to_cook):
        return self.cook_time_for_one_in_minutes * how_many_want_to_cook


cheese_quesedilla = Food("Cheese Quesedilla Recipe", "Place cheese in tortilla.", "Close tortilla and grill on frying pan. Cut and put on plate.", 5)
cheese_quesedilla.print_recipe()
print cheese_quesedilla.total_cook_time(4)

