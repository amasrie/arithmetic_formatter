import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, num_draws):
    removed = []
    if num_draws >= len(self.contents):
      removed = self.contents
      self.contents = []
      return removed
    list = self.contents
    for _ in range(num_draws):
      random_index = random.randint(0, len(list) - 1)
      element = list.pop(random_index)
      removed.append(element)
    return removed
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matches = 0
  for _ in range(num_experiments):
    match = True
    dictionary = dict()
    copy_hat = copy.deepcopy(hat)
    draws = copy_hat.draw(num_balls_drawn)
    for elem in range(len(draws)):
      dictionary[draws[elem]] = 1 if draws[elem] not in dictionary else dictionary[draws[elem]] + 1
    for key in expected_balls:
      if key not in dictionary or expected_balls[key] > dictionary[key]:
        match = False
        break
    matches = matches + 1 if match else matches
  return matches / num_experiments
