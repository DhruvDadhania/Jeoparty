from Tkinter import *
import csv
import sys
import random

try:
    questions = []
    with open('JEOPARDY_CSV.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        firstLine = True
        for row in csv_reader:
            if firstLine:
                firstLine = False
                continue
            questions.append([row[3], row[5], row[6]])  # Category, question and answer
except:
    print('Error: Could not load questions from JEOPARDY_CSV.csv')
    sys.exit(1)

bgColor = 'black'
fgColor = 'white'

root = Tk()
root.geometry("500x300")
root.title('Jeoparty')
root.configure(background=bgColor)

questLbl = Label(root, fg=fgColor, bg=bgColor, height=10, width=60, wraplength=500)
questLbl.grid(row=0, column=0, padx=10, pady=10)

q = False
quest = None


def callback():
    global q
    global quest
    if q:
        questLbl.configure(text=quest[2])
    else:
        quest = random.choice(questions)
        temp = quest[0] + ": " + quest[1]
        questLbl.configure(text=temp)
    q = not q


callback()

Button(root, highlightbackground=bgColor, text='Next', command=callback, width=10).grid(row=1, column=0, padx=10, pady=10)

root.mainloop()