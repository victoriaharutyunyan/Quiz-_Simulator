from threading import Timer
import json


def get_data():
    questions = {}
    with open("edited.json") as file_data:
     questions = json.load(file_data)

     return questions

count = -1
inProgress = True

def timer():
    global inProgress
    global count
    if (inProgress == True):
        count = count + 1
        Timer(1.0, timer).start()
    # elif (inProgress == False):




def pretty_print(current, step=0):

    if (type(current) == list):
        for item in current:
            pretty_print (item, step + 1)
            print(", ", end="")
        print("\n", end="")

    elif (type(current) == dict):
        for key in current:
            print("\n", "\t" * step, key, ": ", end="")
            pretty_print(current[key], step+1)

    else:
        print(current, "", end="")



def history_quiz(data_2):
 global inProgress
 global count
 score = 0
 while True:
  start = input("Do you want to start a quiz? (yes or no)...").lower()
  if (start == "yes"):
      quest = data_2["History"]
      for obj in quest:
          count = -1
          inProgress = True
          timer()
          temp = obj['correct'].lower()
          del obj['correct']
          pretty_print(obj)
          options = input("Your answer...")
          if options.lower() == temp:
              print("True")
              inProgress = False
              score = score + 1

              thisCount = str(count)
              print("you have spent " + thisCount + " seconds on this task")
          else:
              print("False")
              inProgress = False
              thisCount = str(count)
              print("you have spent " + thisCount + " seconds on this task")


      print("you finished the test and this is your score", score)
      if (score == 0):
         print("Here you can improve your knowledge of American history https://www.usa.gov/history")
         break

  elif (start == "no"):
      print("Try again next time")
      break
  else:
      print("wrong input try again")

def geography_quiz(data_1):
    global inProgress
    global count
    score = 0
    while True:
     start = input("Do you want to start a quiz? (yes or no)...").lower()
     if (start == "yes"):
          quest = data_1["Geography"]
          for obj in quest:
              count = -1
              inProgress = True
              timer()
              temp = obj['correct'].lower()
              del obj['correct']
              pretty_print(obj)
              options = input("Your answer...")
              if options.lower() == temp:
                  print("True")
                  inProgress = False
                  score = score + 1
                  thisCount = str(count)
                  print("you have spent " + thisCount + " seconds on this task")
              else:
                  print("False")
                  inProgress = False
                  thisCount = str(count)
                  print("you have spent " + thisCount + " seconds on this task")

          print("you finished the test and this is your score", score)
          if (score == 0):
              print("Here you can improve your knowledge of Geography https://www.nationalgeographic.org/encyclopedia/geography/")
              break


     elif(start == "no"):
         print("Try again next time")
         break
     else:
         print("wrong input try again")

def asking_questions(data):

    while True:
     quiz_subject = input("Which quiz do you want to take"
                             "\n""1)Geography"
                             "\n""2)History"
                             "\n""Your answer...").lower()

     if (quiz_subject == "geography"):
         geography_quiz(data)
         break
     elif (quiz_subject == "history"):
        history_quiz(data)
        break
     else:
         print("wrong answer, try again")




def main():
    my_data = get_data()
    asking_questions(my_data)
# main()