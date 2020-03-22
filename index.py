from threading import Timer
import json
with open("scratch_1.json") as f:
    data = json.load(f)

score = 0
questions_asked = 0
count = 0
inProgress = True


def hello():
  global inProgress
  global count
  count = count + 1
  if inProgress:
   Timer(1.0, hello).start()


for obj in data['Questions']:
    count = 0
    inProgress = True
    hello()
    temp = obj['correct']
    del obj['correct']
    options = input (obj)
    if options == temp:
        print ("True")
        inProgress = False
        score = score + 1
        questions_asked = questions_asked + 1
        thisCount = str(count)
        print("you have spent " + thisCount + " seconds on this task")
    else:
     print ("False")
     inProgress = False
     thisCount = str(count)
     print("you have spent " + thisCount + " seconds on this task")
     questions_asked = questions_asked + 1

if score >= 0:
 print ("you finished the test and this is your score", score)
else:
 print ("you cannot get any score,you lose")


