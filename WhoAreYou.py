from tkinter import *
from PIL import ImageTk, Image

# variables
root = Tk()

dream = 0
part = 1
introPart = 1
questions = [   # formatting    ['question', yes, no]
    ['Are you dreaming?', 1, -1],
    ['Are your eyes closed?', 1, -1],
    ['Do you know the people in your head?', 1, 0],
    ['Are you of wounds?', -1, 1],
    ['Do you fester?', -1, 1],
    ['Do you own crawlers under your bed?', 1, 0],
    ['Did you really fall that day?', 0, 1],
    ['Does the light in the sky scream your name?', 0, 1],
    ['Are you wrong in the answers you give?', -1, 1],
    ['Do you own purpose in the beings you cut?', 1, -1],
    ['Your wounds are festering again, scratch till they bleed?', 0, 1],
    ['Do your words know better?', 1, 0],
    ['There is something in your room that is very important to the stability of yourself, break it?', 1, -1],
    ['Whether you broke it or not, there are still shards on the ground. Pick them up?', 1, -1],
    ['Your bed is screaming at you to hop in.', 1, -1],
    ['Are you awake?', -1, 1],
    ['The Greeter is at your window, wave at him?', 1, 0],
    ['There is a deer on the road, take its flesh?', 0, 1],
    ['The road is smoother than you thought, rough it out?', 0, 1],
    ['There is a light at the end of the road, it\'s snowing. Walk in?', 1, -1],
    ['Everywhere is snowing, lie down in the snow?', 1, -1],
    ['Snow covers your being, you cannot move. Scream?', 0, 1],
    ['Your wounds are festering again, scratch till they bleed?', 0, 1],
    ['There seems to be something wrong in your imagination, you can\'t move. Scream?', 0, 1],
    ['The snow is shining brighter than it was before, ask it to shine brighter?', 1, -1]
]
images = []
for i in range(25):
    images.append(ImageTk.PhotoImage(Image.open('images/'+'%s' % i+'.png')))

introDialogue = [
    'You\'re in your bed.',
    'You\'re eyes are wading.',
    'You\'re eyes begin to close.',
    'You\'re eyes are shut.',
    'Tell me, who are you in your dreams?'
]
introImages = [
    ImageTk.PhotoImage(Image.open('images/sleep0.png')),
    ImageTk.PhotoImage(Image.open('images/sleep1.png')),
    ImageTk.PhotoImage(Image.open('images/sleep2.png')),
    ImageTk.PhotoImage(Image.open('images/sleep3.png')),
    ImageTk.PhotoImage(Image.open('images/sleep4.png'))
]

windowSize = 800

# functions
def intro(dialogue, img):
    def nextCmd():
        global introPart

        if introPart <= len(introDialogue)-1:
            intro(introDialogue[introPart], introImages[introPart])
            introImageLabel.destroy()
            dialogueLabel.destroy()
            nextButton.destroy()
        elif introPart >= len(introDialogue):
            questionaire(questions[0][0], questions[0][1], questions[0][2])
            introImageLabel.destroy()
            dialogueLabel.destroy()
            nextButton.destroy()
        introPart += 1

    introImageLabel = Label(image=img)
    dialogueLabel = Label(text=dialogue, bg="black", fg="white")
    nextButton = Button(text="Next.", bg="black", fg="white", padx=40, command=nextCmd)
    
    introImageLabel.place(x=0, y=0)
    dialogueLabel.place(x=0, y=0)
    nextButton.place(x=0, y=30)

def questionaire(question, yes, no):
    def answerCmd(answer):
        global dream
        global part

        if part <= len(questions)-1:
            dream += answer
            questionaire(questions[part][0], questions[part][1], questions[part][2])
            questionLabel.destroy()
            yesButton.destroy()
            noButton.destroy()
        elif part >= len(questions):
            endLabel = Label(image=images[dream])
            endLabel.place(x=0, y=0)
            questionLabel.destroy()
            yesButton.destroy()
            noButton.destroy()
        part += 1

        if dream < 0:
            dream = 0
        elif dream > len(images):
            dream = len(images)
        if part > len(questions):
            part = len(questions)

    questionLabel = Label(root, text=question, bg="black", fg="white")
    yesButton = Button(root, text="Yes.", bg="black", fg="white", command=lambda: answerCmd(yes))
    noButton = Button(root, text="No.", bg="black", fg="white", command=lambda: answerCmd(no))

    questionLabel.place(x=windowSize/2-(len(questions[part][0])*3), y=windowSize/4)
    yesButton.place(x=windowSize/3.5, y=windowSize/2)
    noButton.place(x=windowSize/1.5, y=windowSize/2)

# window config
root.configure(background="black")
root.geometry('%s' % windowSize+'x'+'%s' % windowSize)
root.maxsize(windowSize, windowSize); root.minsize(50, 50)
root.iconphoto(True, PhotoImage(file='images/icon.png'))
root.title('Who are you?')

# run
intro(introDialogue[0], introImages[0])

# mainloop
root.mainloop()