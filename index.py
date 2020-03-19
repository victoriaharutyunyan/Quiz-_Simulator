from threading import Timer

print ("Question1: What is the longest river in South America")
correct = "Uruguay"
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

hello()

options = input ({'option1': "Uruguay",
  'option2': "Orinoco",
  'option3': "Amazon",
  'option4':"Cauca",
})

while options == correct:
 print ("True")
 inProgress = False
 score = score + 1
 questions_asked = questions_asked + 1
 thisCount = str(count)
 print("you have spent " + thisCount + " seconds on this task")
 break
else:
  print ("False")
  inProgress = False
  thisCount = str(count)
  print("you have spent " + thisCount + " seconds on this task")
  questions_asked = questions_asked + 1

count = 0
inProgress = True
print("What is the largest lake in Africa?")
correct2 = "Victoria"
hello()
options2 = input ({'a': "Tanganika",
'b':"Karita",
'c':"Tana",
'd':"Victoria"})
while options2 == correct2:
   inProgress = False
   thisCount = str(count)
   print("you have spent " + thisCount + " seconds on this task")
   score = score + 1
   questions_asked = questions_asked + 1
   break
else:
   print("False")
   inProgress = False
   thisCount = str(count)
   print("you have spent " + thisCount + " seconds on this task")
   score = score - 1
   questions_asked = questions_asked + 1

while questions_asked == 2:
   if score >= 0:
    print ("you finished the test and this is your score", score)
    break
   else:
     print ("you cannot get any score,you lose")
     break

else:
  questions_asked = questions_asked + 1
