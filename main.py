import random

num = 0
lower_bound = 1
upper_bound = 100


def generate_random_number(lb, ub):
  rand_num = random.randint(lb, ub)
  return (rand_num)


def difference_from_answer(guess, answer):
  answer = generate_random_number(lower_bound, upper_bound)]
  if guess > answer:
    print("Too high")
  elif guess < answer:
    print("Too Low")
  elif guess == answer:
    print("Correct")
  else:
    print("ERROR")

def make_a_guess(answer):
  guess = int(input("Make a guess: "))