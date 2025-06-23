** start of main.py **

import copy
import random

class Hat:
    
    def __init__(self, **color):
        self.contents = []   
        if len(color) >= 1:   
            for key, value in color.items():
                if value == 0:
                    raise ValueError('Hat must contain at least one ball')
                for i in range(value):
                    self.contents.append(key)
        else:
            raise ValueError('Hat must contain at least one ball')
        

    def draw(self, no_balls):
        
        
        output_list = []
        if no_balls > len(self.contents):
            output_list = copy.copy(self.contents)
            self.contents = []
            return output_list

        for i in range(no_balls):
            output_list.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
            
        
        
        return output_list
        #return random.sample(self.contents, no_balls)
        
        
       

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0
    expected_content = []
    
    for key, value in expected_balls.items():
            for i in range(value):
                expected_content.append(key)
    
    for i in range(N):
        all_there = []
        #print(len(hat.contents))
        content_copy = copy.copy(hat.contents)
        drawn_content = hat.draw(num_balls_drawn)
        #drawn_content_copy = copy.copy(drawn_content)
        print(len(drawn_content))
        
        #print(len(drawn_content_copy), '\n')
        for content in expected_content:
            print(expected_content)
            if content in drawn_content:
                all_there.append(True)
                drawn_content.remove(content)
            else:
                print('WHAT THE FUCK!!!!')
                all_there.append(False)
                
        hat.contents = content_copy     
        if all(all_there):
             
            M += 1   
            
    return M/N


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=14,
                  num_experiments=10)
print(probability)

** end of main.py **

