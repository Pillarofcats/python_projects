import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    ball_str = ""
    self.orig_ball_dict = {}
    self.copy_ball_dict = {}
    self.orig_balls = []
    self.copy_balls = []
    self.removed_balls = []
    self.recent_removed_balls = []

    for ball, num in kwargs.items():
      ball_str += num*(ball + " ")
      self.orig_balls = ball_str.rstrip().split(" ")
      self.copy_balls = ball_str.rstrip().split(" ")

      self.orig_ball_dict[ball] = num
      self.copy_ball_dict[ball] = num

  def __str__(self):
    balls_in_hat = ", ".join(self.copy_balls)
    balls_removed = ", ".join(self.removed_balls)
    return "Remaining balls in hat: " + balls_in_hat + "\nBalls removed from hat: " + balls_removed

  def draw(self, num_balls_to_draw):
    self.recent_removed_balls = []
    # print("DRAWING:")

    for i in range(num_balls_to_draw):
      rand_index = random.randint(0, len(self.copy_balls) - 1)
      self.removed_balls.append(self.copy_balls[rand_index])
      self.recent_removed_balls.append(self.copy_balls[rand_index])
      # print("Removed:", self.copy_balls[rand_index])
      self.copy_ball_dict[self.copy_balls[rand_index]] -= 1 
      del self.copy_balls[rand_index]

    # print("current", self.copy_ball_dict)
    # print("orginal", self.orig_ball_dict)
    # print("\nTotal balls remaining in hat:", self.copy_balls)
    # print("\nTotal balls Removed from hat:", self.removed_balls, "\n")
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  got_expected_balls = 0
  probabilty_with_num_exp = 0

  for i in range(num_experiments):
    total_balls = 0
    expected_balls_probabilites = {}
    expected_probability = 1.0

    for val in hat.copy_ball_dict.values():
      total_balls += val

    # print("total balls before draw:", total_balls)

    temp_orig_ball_dict = hat.orig_ball_dict
    temp_orig_balls = hat.orig_balls
    temp_reset_removed_balls = []
    dict_recent_removed_balls = {}
    expected_ball_chk = len(expected_balls)

    if num_balls_drawn > len(hat.copy_balls):
      # print("Cannot draw", num_balls_drawn, "balls while", len(hat.copy_balls), "balls remain in the hat. Putting all removed balls back into hat.\n")
      hat.copy_ball_dict = copy.deepcopy(temp_orig_ball_dict)
      hat.copy_balls = copy.deepcopy(temp_orig_balls)
      hat.removed_balls = copy.deepcopy(temp_reset_removed_balls)

    if total_balls - num_balls_drawn == 0:
      # print("\nAll of the balls have been drawn. Putting all removed balls back into hat.\n")
      hat.copy_ball_dict = copy.deepcopy(temp_orig_ball_dict)
      hat.copy_balls = copy.deepcopy(temp_orig_balls)
      hat.removed_balls = copy.deepcopy(temp_reset_removed_balls)

    hat.draw(num_balls_drawn)

    #initialize the known keys (ball colors)
    for key in hat.copy_ball_dict.keys():
      dict_recent_removed_balls[key] = 0

    for key in hat.recent_removed_balls:
      if key in hat.copy_ball_dict.keys():
        dict_recent_removed_balls[key] += 1

    # print("expected_balls:", expected_balls)
    # print("drawn_balls:", dict_recent_removed_balls)

    for key, val in expected_balls.items():
      # print("\nexpected balls:")
      # print(key,":",val)
      # print("\ndrawn balls:")
      # print(key, dict_recent_removed_balls[key],"\n")

      if key in dict_recent_removed_balls.keys() and dict_recent_removed_balls[key] >= val:
        expected_ball_chk -= 1
        # print("chk", expected_ball_chk)

      if expected_ball_chk == 0:
        got_expected_balls += 1
        # print(got_expected_balls)
        # print("The expected balls were drawn!")

    for key, val in expected_balls.items():
      probability = f'{val/total_balls:.4f}'
      expected_balls_probabilites[key] = float(probability)
    
    for val in expected_balls_probabilites.values():
      expected_probability *= val

    expected_probability = float(f'{expected_probability:.4f}')

    # print(expected_balls_probabilites)
    # print(expected_probability)

  probabilty_with_num_exp = got_expected_balls/num_experiments
  print("Expected balls drawn:", got_expected_balls)
  print("Number of experiments:", num_experiments)

  return f'{float(probabilty_with_num_exp*100):.2f} %'