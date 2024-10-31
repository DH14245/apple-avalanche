#   a123_apple_1.py
import turtle as trtl
import random as random


#-----lists-----


possible_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
typeable_letters = []
falling_fruits = []
falling_letters = []


#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape (Apple)
pear_image = "pear.gif" # Store the file name of your shape (Pear)

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file
wn.addshape(apple_image) # Make the screen aware of the new file

active_apple = trtl.Turtle()
active_pear = trtl.Turtle()
active_apple2 = trtl.Turtle()
active_pear2 = trtl.Turtle()
active_apple3 = trtl.Turtle()


letter_turtle = trtl.Turtle()
current_fruit = trtl.Turtle()
falling_letter_turtle = trtl.Turtle()

wn.bgpic("background.gif") # Place the background image

timer_active = False

fruits = []

num_of_apples = 3
num_of_pears = 2


fruit_cor = []

To_Fall_Fruits = []

typed_fruits = set()

index = 0

falling_index = 0

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple():
  global typeable_letters
  global fruits
  for i in range(num_of_apples):  
    active_apple = trtl.Turtle(shape = apple_image)
    active_apple.penup()
    active_apple.goto(random.randint(-200, 200), random.randint(0, 200))
    fruits.append(active_apple)
    letter_to_be_typed = possible_letters[random.randint(0, 25)]
    typeable_letters.append(letter_to_be_typed)
    letter_turtle.hideturtle()
    letter_turtle.penup()
    letter_turtle.goto(active_apple.xcor() - 10, active_apple.ycor() - 25)
    letter_turtle.write(letter_to_be_typed, font=("Arial", 32, "bold"))
  for i in range(num_of_pears):
    active_pear = trtl.Turtle(shape = pear_image)
    active_pear.penup()
    active_pear.goto(random.randint(-200, 200), random.randint(0, 200))
    fruits.append(active_pear)
    letter_to_be_typed = possible_letters[random.randint(0, 25)]   
    typeable_letters.append(letter_to_be_typed)
    letter_turtle.hideturtle()
    letter_turtle.penup()
    letter_turtle.goto(active_pear.xcor() - 10, active_pear.ycor() - 25)
    letter_turtle.write(letter_to_be_typed, font=("Arial", 32, "bold"))
  print(fruits)
  wn.update()



def draw_appleTwo(fruits):
  global letter_to_be_typed
  global index
  for fruit, image in fruits:
    fruit.shape(image)
    fruit.penup()
    for i in range(len(fruit_cor)):
      random_x = fruit_cor[i][1]
      random_y = fruit_cor[i][2]
    fruit.goto(random_x, random_y)
    letter_turtle.hideturtle()
    letter_turtle.penup()
    letter_turtle.goto(random_x - 10, random_y - 25)
    letter_turtle.write(typeable_letters[index], font=("Arial", 32, "bold"))
    index += 1
    fruit.showturtle()



# moves the fruit so that it falls down the screen
def fruit_fall(): #defines the function
  print("Fruit Fall")
  global falling_index
  if falling_index == 0:
    print(fruits[0])
    current_fruit = fruits[0]
    current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 100)
  elif falling_index == 4:
    print(fruits[1])
    current_fruit = fruits[1]
    current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 100)
  elif falling_index == 8:
    print(fruits[2])
    current_fruit = fruits[2]
    current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 100)
  elif falling_index == 12:
    print(fruits[3])
    current_fruit = fruits[3]
    current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 100)
  elif falling_index == 16:
    print(fruits[4])
    current_fruit = fruits[4]
    current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 100)
    

  respawn_fruit()

def start_fruit_fall():
  global timer_active
  timer_active = True
  fruit_fall()


def letter_to_type():
  global typeable_letters
  for letter in typeable_letters:
    wn.onkeypress(lambda l=letter: check_keypress(l), letter)


def check_keypress(key):
  global falling_index
  global typeable_letters
  global falling_letters
  if key in typeable_letters:
    print("You pressed the correct key!")
    falling_letters.append(key)
    typeable_letters.remove(key)
    for i in range(len(fruit_cor)):
      if i % 4 == 0:
        if key == fruit_cor[i + 3]:
          falling_index = i
          print(falling_index)
          print(falling_fruits)
          print(fruit_cor)
          start_fruit_fall()
   

    

def respawn_fruit():
  for i in range (len(fruits)):
    if fruits[i][0].ycor() < -200:
      letter_turtle.clear()
      global timer_active
      timer_active = False 
      fruits[i][0].hideturtle()
      ycord = random.randint(0, 200)
      xcord = random.randint(-200, 200)
      fruits[i][0].goto(xcord, ycord)
      letter_to_type()
      fruits[i][0].showturtle()
  
  wn.ontimer(respawn_fruit, 100)


#-----function calls-----


draw_apple()
letter_to_type()
#respawn_fruit()
wn.listen()


wn.mainloop()



#When clicked one letter, all fruits fall! FIX!