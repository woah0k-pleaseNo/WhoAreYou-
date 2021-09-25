from tkinter import *
from PIL import ImageTk, Image

# variables
root = Tk()

background = "black"
foreground = "white"
dream = 0
q = 1
p = 0

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

windowSize = 800

# window config
root.configure(background=background)
root.title('Who are you?')
root.iconphoto(True, PhotoImage(file='images/icon.png'))
root.geometry('%s' % windowSize+'x'+'%s' % windowSize)
root.maxsize(windowSize, windowSize); root.minsize(50, 50)

# functions
def clamp(num, min, max):
    if num < min:
        num = min
    elif num > max:
        num = max
    else:
        num = num
    ans = num; return ans

def end(img):
    endLabel = Label(image=img)
    endLabel.place(x=0, y=0)

def questionaire(question, yes, no):
    def ansCmd(answer):
        global dream
        global q
        if q <= 24:
            dream += answer
            dream = clamp(dream, 0, 24)
            questionaire(questions[q][0], questions[q][1], questions[q][2])
            questionLabel.destroy()
            yesButton.destroy()
            noButton.destroy()
        if q >= 25:
            end(images[dream])
        q += 1
        
    questionLabel = Label(text=question, bg=background, fg=foreground)
    yesButton = Button(text="Yes.", bg=background, fg=foreground, command=lambda: ansCmd(yes))
    noButton = Button(text="No.", bg=background, fg=foreground, command=lambda: ansCmd(no))

    questionLabel.place(x=windowSize/2.5, y=windowSize/4)
    yesButton.place(x=windowSize/3.5, y=windowSize/2)
    noButton.place(x=windowSize/1.5, y=windowSize/2)

# program
questionaire(questions[0][0], questions[0][1], questions[0][2])

# mainloop
root.mainloop()