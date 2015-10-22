from classes import DesStudent
import json

print("\t\tWhat up!")

new = DesStudent()

new.name = input("\nYour name: ")
new.mail = input("\nYour mail: ")
new.skills = input("\nYour skills (comma separated): ").strip(' ').split(',')

correct_answers = 0

print("Now we\'re going to ask you 3 questions: ")


fst_question = input('''\nWhat\'s the best hacker community:
                        a) Platzi
                        b) Codigofacilito
                        c) Devf\n
                        ''')

if fst_question.lower() == 'c':
    correct_answers += 1
else:
    correct_answers += 0

sec_question = input('''\nIf your friends invite you to a party you say:
                        a) Damn nigga yes!!
                        b) Nuh bruh I\'m tired
                        c) Yes, but I\'ll leave early\n
                        ''')
 
if sec_question == 'a':
    correct_answers += 1
else:
    correct_answers += 0

thr_question = input('''\nDo you play ping-pong?
                        a) Yes
                        b) Nope
                        c) Dafuq is dat?\n
                        ''')

if thr_question == 'b':
    correct_answers += 1
else:
    correct_answers += 0

if correct_answers <= 1:
    print("You're a white belt!")
    new.belt = 'white'
elif correct_answers == 2:
    print("Wow! You're a red belt")
    new.belt = 'red'
else:
    print("You're a total pro! a.k.a Black Belt")
    new.belt = 'black'


data = new.__dict__

print(new.to_JSON())
with open('{}.json'.format(new.name), 'w') as f:
    json.dump(data, f)


