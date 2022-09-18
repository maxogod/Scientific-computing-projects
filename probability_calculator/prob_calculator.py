import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, val in kwargs.items():
            for _ in range(val):
                self.contents.append(key)
    
    
    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        selected_balls = []
        for _ in range(number_of_balls):
            selected_balls.append(self.contents.pop(random.randrange(len(self.contents))))
        return selected_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        aux_hat = copy.deepcopy(hat)
        drawn_balls = aux_hat.draw(num_balls_drawn)
        current_case = False
        continuation = False
        
        for key, val in expected_balls.items():
            if drawn_balls.count(key) >= val:
                current_case = True
            else:
                continuation = True
                break
        
        if continuation: continue
        
        if current_case: count += 1
    return count/num_experiments
