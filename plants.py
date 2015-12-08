class Plants(object):
    def __init__ (self, type_of_flower, flowering_or_not_flowering, color):
        self.type_of_flower = type_of_flower
        self.flowering_or_not_flowering = flowering_or_not_flowering
        self.color = color
    def set_is_flowering(self, bool):
        self.flowering_or_not_flowering = bool 
    def flower_color(self):
        print "a", self.type_of_flower, "is", self.color[0], "and", self.color[1]

sunflower = Plants("sunflower", True, ["yellow", "green"])
sunflower.set_is_flowering(True) 
sunflower.flower_color()
