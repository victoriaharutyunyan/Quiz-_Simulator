import json
def get_data():
    questions = {}
    with open("instructor.json") as file_data:
     questions = json.load(file_data)

    return questions

def pretty_print(current, step=0):
    if (type(current) == list):
        for item in current:
            pretty_print (item, step + 1)
            print(", ", end="")
        print("\n", end="")

    elif (type(current) == dict):
        for key in current:
            print("\n", "\t" * step,  ": ", end="")
            current[key] = input(key)
            pretty_print(current[key], step+1)


def making_quiz(data):
    while True:
     start = input("do you want to make a quiz?").lower()
     if start == "yes":
       for obj in data['Questions']:
        pretty_print(obj)

       f = open("instructor.json", "w")
       json.dump(data, f, indent=2)
       f.close()
       break
     elif (start.lower() == "no"):
        print("try next time,bye :)")
        break
     else:
        print("wrong input, try again")




def main():
    current_data = get_data()
    making_quiz(current_data)
# main()

