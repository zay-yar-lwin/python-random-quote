import random


def setup():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = 17
  rnd1 = random.randint (0, last)
  rnd2 = random.randint (0, last)
  print(quotes[rnd1], end = " ")
  print(quotes[rnd2], end = " ")

if __name__== "__main__":
  setup()
