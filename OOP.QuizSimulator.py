from threading import Timer

class QuizQuestion:
   count = -1
   inProgress = True
   def __init__(self,question, choice1, choice2, choice3, choice4, correct):
      self.question = question
      self.choice1 = choice1
      self.choice2 = choice2
      self.choice3 = choice3
      self.choice4 = choice4
      self.correct = correct

   def displayProperties(self):
       print(self.question, self.choice1, self.choice2, self.choice3, self.choice4)

   def displayCorrect(self):
       return(self.correct)


class Quiz:
    count = -1
    inProgress = True
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.questions = []

    def addQuestion (self, question):
        self.questions.append(question)

    def printAllQuestions(self):
        for q in self.questions:
            q.displayProperties()

    def startQuiz(self):
       Quiz.count = -1
       Quiz.inProgress = True

       def timer():
           if (Quiz.inProgress == True):
               Quiz.count = Quiz.count + 1
               Timer(1.0, timer).start()
           elif (Quiz.inProgress == False):
               return Quiz.count

       for quest in self.questions:
        print(quest.question, quest.choice1, quest.choice2, quest.choice3, quest.choice4)
        Quiz.inProgress = True
        timer()
        answer = input("Your answer...")
        if answer == quest.correct:
         print("True")
         Quiz.inProgress = False
         thisCount = str(Quiz.count)
         print("you have spent " + thisCount + " seconds on this task")
         Quiz.count = -1
        else:
         print("False")
         Quiz.inProgress = False
         thisCount = str(Quiz.count)
         print("you have spent " + thisCount + " seconds on this task")
         Quiz.count = -1




def studentMain():
    qq1 = QuizQuestion("1) How many starts does the American Flag have?", "forty", "fifty", "fiftyfive","fortyfive", "fifty")
    qq2 = QuizQuestion("2) What sport’s hall of fame enshrined Abraham Lincoln for having a stellar record of just one loss?", "Wrestling", "Soccer", "Swimming", "Tennis", "Wrestling")
    quiz1 = Quiz("History", "Sept 15")

    q1 = QuizQuestion("1) What is the capital of Armenia?", "yerevan", "gyumri", "dilijan", "artashat", "yerevan")
    q2 = QuizQuestion("2) What is the capital of Spain", "barcelona", "valencia", "madrid", "benidorm","madrid")
    quiz2 = Quiz("Geography", "Oct 24")


    while True:
     quiz_subject = input("Which quiz do you want to take"
                             "\n""1)Geography"
                             "\n""2)History"
                             "\n""Your answer...").lower()

     if (quiz_subject == "geography"):
         quiz2.addQuestion(q1)
         quiz2.addQuestion(q2)
         quiz2.startQuiz()
         # q1.displayProperties()
         # quiz1.startQuiz()
         # q2.displayProperties()
         # quiz1.startQuiz()
         break
     elif (quiz_subject == "history"):
         quiz1.addQuestion(qq1)
         quiz1.addQuestion(qq2)
         quiz1.startQuiz()
         break
     else:
         print("wrong answer, try again")


def instructorMain():

 quest = input("Question:")
 choice1 = input("choice 1")
 choice2 = input("choice2")
 choice3 = input("choice3")
 choice4 = input("choice4")
 correct = input("correct")

 qq1 = QuizQuestion(quest, choice1,choice2, choice3, choice4, correct)

 quest = input("Question:")
 choice1 = input("choice 1")
 choice2 = input("choice2")
 choice3 = input("choice3")
 choice4 = input("choice4")
 correct = input("correct")
 qq2 = QuizQuestion(quest, choice1,choice2, choice3, choice4, correct)

 quiz1 = Quiz("History", "OCt 12")
 quiz1.addQuestion(qq1)
 quiz1.addQuestion(qq2)

 quiz1.printAllQuestions()

def main():
     print("Welcome to Quiz Simulator App")
     while True:
         user_type = input("Are you an instructor or a student?")
         if (user_type.lower() == "instructor"):
             instructorMain()
             break
         elif (user_type.lower() == "student"):
             studentMain()
             break

main()