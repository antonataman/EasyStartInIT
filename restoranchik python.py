import random
import re
 
 
class Dish:
    def __init__(self, name):
        self.name = name
        self.time = self.calc_time()
 
    def calc_time(self):
        return random.randint(0, 50)
 
    def to_print(self):
        print('{0}{1}{2}{3}minutes'.format(self.name,
                                           (31 - self.name.__len__())*'.',
                                           self.time,
                                           ((3 - int(len(str(self.time))))*' ')))
                                     
    def is_valid_name(self):
        is_valid = []
        for word in self.name.split("'"):
            for subword in word.split('-'):
                for sub_subword in subword.split('+'):
                    is_valid.append(sub_subword.strip().isalpha())  # [True, False, True, True]
        
        result = True
        for is_word_alpha in is_valid:
            result = result and is_word_alpha
        
        return result
            
    
    
    
dishes_string = input('What would you like?(Use comma to separate) ')  
 
 
dishes_list = re.split(',+', dishes_string)
 
dishes_set = {dish.strip().title() for dish in dishes_list}
 
# creating list of class Dishes
dishes = [Dish(dish) if (dish and Dish(dish).is_valid_name()) else None
for dish in dishes_set]
 
 
 
# printing list of class Dishes
print('\nDish                     Time for cooking')
for dish in dishes:
    if dish:
        dish.to_print()