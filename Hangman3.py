# Hangperson game to guess words
# uses turtle
import random
import turtle
import math   #optional :-)
import time

wordList = ["conductive", \
            "empirical", "frappe", "petulant", "repudiate", "hamburger", "ubiquitous", \
            "zwieback", "youtube", "wyoming", "yalta", "obfuscating", "austere", \
            "capitalize", "diversification", "enumerate", "persecute", "pitiable", \
            "sparingly", "treacherous"]

secretWord = random.choice(wordList)
wrongLetters = []
correctLetters = []

# DON'T SHOW PEOPLE THIS!!!
print(f"The secret word is {secretWord} ")

wrongGuesses = 0
MAX_GUESSES = 13
screenWord = ""  #now its global

#set up screen
sWidth =1400
sHeight = 700


hypot = int(math.sqrt((sWidth*sWidth) + (sHeight * sHeight)))
turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(sWidth, sHeight)
screen.bgcolor(114, 70, 235)

#setup turtle
t = turtle.getturtle()
t.shape("turtle")
t.color(242, 242, 208)
t.width(int(hypot*0.0035))
t.speed(0)
t.penup()
t.hideturtle()

# Nov 11 we make new turtles
topFont = 60
topScreenTurtle = turtle.Turtle()
topScreenTurtle.shape("turtle")
topScreenTurtle.color(242, 242, 208)
topScreenTurtle.width(int(hypot*0.0035))
topScreenTurtle.speed(0)
topScreenTurtle.penup()
topScreenTurtle.goto(-1 * int(sWidth / 2) + int(sWidth * 0.1),  int(sHeight * 0.5))
topScreenTurtle.setheading(0)


bottomScreenTurtle = turtle.Turtle()
bottomScreenTurtle.shape("turtle")
bottomScreenTurtle.color(242, 242, 208)
bottomScreenTurtle.width(int(hypot*0.0035))
bottomScreenTurtle.speed(0)
bottomScreenTurtle.penup()
bottomScreenTurtle.goto(-1 * int(sWidth/2) + int(sWidth * 0.1), -1 * int(sHeight/2) + int(sHeight * 0.25) )
bottomScreenTurtle.setheading(0)


#turtle position variables
rightHandLoc = (0,0)
leftHandLoc = (0,0)
rightFootLoc = (0,0)
leftFootLoc = (0,0)
armCenterLoc = (0,0)
bodyBotLoc = (0.0)
bodyTopLoc = (0,0)

def drawGallows():
    t.forward(int(sWidth * 0.125))
    t.right(90)
    t.forward(int(sHeight * 0.25))
    t.left(90)
    #draw the bottom line
    t.pendown()
    t.forward(int(sWidth * 0.25))
    #go backward....
    t.backward(int(sWidth* 0.125))
    #draw up
    t.left(90)
    t.forward(int(sHeight* 0.6))
    t.left(90)
    t.forward(int(sWidth * 0.125))
    t.left(90)
    t.forward(int(sHeight * 0.1))

def drawHead():
    t.right(90)
    t.circle(int(sHeight * 0.06))

def drawBody():
    global armCenterLoc, bodyBotLoc, bodyTopLoc
    t.left(90)
    t.penup()
    t.forward(int(sHeight * 0.06) *2)
    t.pendown()
    bodyTopLoc = t.position()
    t.forward(int(sHeight * 0.06) *2)
    bodyBotLoc = t.position()
    t.penup()
    #find arm center loc here
    t.backward(int(sHeight * 0.037) * 2)
    armCenterLoc = t.position()
    t.goto(bodyBotLoc)

def drawLLeg():
    global leftFootLoc, bodyBotLoc
    t.goto(bodyBotLoc)
    t.setheading(-90)
    t.right(20)
    t.pendown()
    t.forward(int(hypot* 0.07))
    leftFootLoc = t.position()
    t.penup()

def drawRLeg():
    global rightFootLoc
    t.goto(bodyBotLoc)
    t.setheading(-90)
    t.left(20)
    t.pendown()
    t.forward(int(hypot * 0.07))
    rightFootLoc = t.position()
    t.penup()

def drawLArm():
    global leftHandLoc
    t.penup()
    t.goto(armCenterLoc)
    t.setheading(-90)
    t.right(50)
    t.pendown()
    t.forward(int(hypot * 0.04))
    leftHandLoc = t.position()
    t.penup()
    t.goto(armCenterLoc)
    t.setheading(-90)

def drawRArm():
    global rightHandLoc
    t.penup()
    t.goto(armCenterLoc)
    t.setheading(-90)
    t.left(50)
    t.pendown()
    t.forward(int(hypot * 0.04))
    rightHandLoc = t.position()
    t.goto(armCenterLoc)
    t.setheading(-90)

def drawRightShoe():
    t.penup()
    t.goto(rightFootLoc)
    t.setheading(-180)
    #t.right(30)
    t.pendown()
    #instead of circle draw arc
    t.circle(int(hypot*0.0060), 90)
    t.circle(int(hypot*0.015), 90)
    t.circle(int(hypot*0.0060), 90)
    t.circle(int(hypot*0.015), 90)
    t.hideturtle()

def drawLeftShoe():
    t.penup()
    t.goto(leftFootLoc)
    t.setheading(180)
    t.pendown()
    #instead of circle draw arc

    t.circle(int(hypot*0.015), 90)
    t.circle(int(hypot*0.0060), 90)
    t.circle(int(hypot*0.015), 90)
    t.circle(int(hypot * 0.0060), 90)
    t.hideturtle()

def drawRightHand():
    t.penup()
    t.goto(rightHandLoc)
    t.setheading(-180)
    t.left(50)
    t.pendown()
    t.circle(int(hypot* 0.0075), 75)
    myH = t.heading()
    for i in range(4):
        t.forward(int(hypot* 0.0075))
        t.circle(int(hypot * 0.0020), 180)
        t.forward(int(hypot* 0.0075))
        t.setheading(myH)
    #palm
    t.left(80)
    #thumb
    t.circle(int(hypot*0.0040), 30)
    t.forward(int(hypot*0.0040))
    t.circle(int(hypot * 0.0020), 180)
    t.forward(int(hypot * 0.0040))
    t.goto(rightHandLoc)
    t.penup()

def drawLeftHand():
    t.penup()
    t.goto(leftHandLoc)
    t.setheading(-180)
    t.left(-50)
    t.pendown()
    t.circle(int(hypot * 0.0075), -75)
    t.setheading(-130)
    myH = t.heading()
    for i in range(4):
        t.forward(int(hypot * 0.0075))
        t.right(180)
        t.circle(int(hypot * 0.0020), -180)
        t.right(180)
        t.forward(int(hypot * 0.0075))
        t.setheading(myH)
    # palm
    t.left(-130)
    # thumb
    t.circle(int(hypot * 0.0040), 30)
    t.forward(int(hypot * 0.0040))
    t.right(180)
    t.circle(int(hypot * 0.0020), -180)
    t.right(180)
    t.forward(int(hypot * 0.0040))
    t.goto(leftHandLoc)
    t.penup()

def drawLeftEye():
    t.penup()
    t.goto(bodyTopLoc)
    t.setheading(90)
    t.forward(int(sHeight * 0.055))
    t.left(90)
    t.forward(int(sHeight * 0.025))
    t.setheading(0)
    style = ('Arial', int(sHeight * 0.045), 'normal')
    turtle.write('x', font=style, align='center')

def drawRightEye():
    t.penup()
    t.goto(bodyTopLoc)
    t.setheading(90)
    t.forward(int(sHeight * 0.055))
    t.right(90)
    t.forward(int(sHeight * 0.025))
    t.setheading(0)
    style = ('Arial', int(sHeight * 0.045), 'normal')
    turtle.write('x', font=style, align='center')

def drawMouth():
    t.penup()
    t.goto(bodyTopLoc)
    t.setheading(90)
    t.forward(int(sHeight * 0.050))
    t.right(90)
    t.forward(int(sHeight * 0.033))
    t.setheading(100)
    t.pendown()
    t.circle(int(sHeight * 0.035), -25)
    t.right(25)
    tongueLoc = t.position()
    t.circle(int(sHeight * 0.040), -95)
    t.right(15)
    t.circle(int(sHeight * 0.035), -30)
    t.penup()
    t.goto(tongueLoc)
    t.setheading(0)
    t.right(45)
    t.right(180)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    t.circle(int(hypot*0.005), -180)
    t.end_fill()

def updateDrawing():

    if wrongGuesses == 0:
        drawGallows()
    if wrongGuesses == 1:
        drawHead()
    if wrongGuesses == 2:
        drawBody()
    if wrongGuesses == 3:
        drawLLeg()
    if wrongGuesses == 4:
        drawRLeg()
    if wrongGuesses == 5:
        drawLArm()
    if wrongGuesses == 6:
        drawRArm()
    if wrongGuesses == 7:
        drawRightShoe()
    if wrongGuesses == 8:
        drawLeftShoe()
    if wrongGuesses == 9:
        drawRightHand()
    if wrongGuesses == 10:
        drawLeftHand()
    if wrongGuesses == 11:
        drawLeftEye()
    if wrongGuesses == 12:
        drawRightEye()
    if wrongGuesses == 13:
        drawMouth()

def drawWrongLetters():
    topScreenTurtle.clear()
    lString = "Wrong Letters: "
    for l in wrongLetters:
        lString = lString + l + ", "

    lString = lString[0: len(lString)-2]

    topScreenTurtle.write(lString, move=False, align="left", font=("Arial", topFont, "normal"))


def drawWord():
    global screenWord
    # step 1 -- save turtle position info
    #currentLoc = t.position()
    #currentHead = t.heading()
    bottomScreenTurtle.clear()
    bottomScreenTurtle.color(0,255,0)
    bottomScreenTurtle.penup()
    bottomScreenTurtle.goto(-1 * int(sWidth/2) + int(sWidth * 0.1), -1 * int(sHeight/2) + int(sHeight * 0.25) )
    #bottomScreenTurtle.showturtle()
    bottomScreenTurtle.setheading(0)

    screenWord = ""

    for letter in secretWord:
        if letter in correctLetters:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "

    bottomScreenTurtle.write(screenWord, move=False, align="left", font=("Arial", 80, "normal"))
    # finish it
    #t.goto(currentLoc)
    #t.setheading(currentHead)
    #bottomScreenTurtle.showturtle()

def getGuess():
    badLetterString = ""
    for letter in wrongLetters:
        badLetterString += letter + ", "

    boxTitle = "Letters Used:" + badLetterString

    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word")
    return theGuess

def writeErrorMessage(msg):
    topScreenTurtle.clear()
    topScreenTurtle.write(msg, move=False, align="left", font=("Arial", topFont, "normal"))
    time.sleep(2)
    topScreenTurtle.clear()

def printWinOrLose(win):
    global screenWord
    topScreenTurtle.clear()
    if win:
        screenWord = secretWord
        drawWord()
        topScreenTurtle.write("You Win!!!", move=False, align="left", font=("Arial", topFont, "normal"))
    else:
        topScreenTurtle.write("I'm sorry. Game over...", move=False, align="left", font=("Arial", topFont, "normal"))

def getWordGuess():
    playerWordGuess = screen.textinput("Guess It", "Enter your guess of the word?")

    if playerWordGuess.lower() == secretWord.lower():
        # celebrate their win!!!!
        #print("Win!!")
        printWinOrLose(True)
        return False  #  false means game over
    else:
        # celebrate their failure!!!
        #print("Lose!!")
        printWinOrLose(False)
        time.sleep(1)
        writeErrorMessage("The secret word is: " + secretWord)
        return False  #  false means game ove


##  Now play the game....

#t.showturtle()
gameOn = True
updateDrawing()
#main game loop
while gameOn:
    drawWord()
    guess = getGuess()
    # step 1 -- see if they want a word
    if guess == "$$":
        gameOn = getWordGuess()
    elif len(guess) != 1:
        writeErrorMessage("I need a single letter. Guess Again")
        drawWrongLetters()
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        writeErrorMessage("I need a letter. Guess Again")
        drawWrongLetters()
    elif guess.lower() in wrongLetters:
        writeErrorMessage("You already guessed " + guess + ". Guess Again")
        drawWrongLetters()
    else:
            #if the letter is good.....
        if guess.lower() in secretWord.lower():
            correctLetters.append(guess.lower())
            drawWord()
        else:
            #if the letter is bad
            wrongLetters.append(guess.lower())
            wrongGuesses += 1
            drawWrongLetters()
            updateDrawing()

        if wrongGuesses >= MAX_GUESSES:
            writeErrorMessage("You are out of guesses. Game Over.")
            gameOn = False
            writeErrorMessage("The secret word is: " + secretWord)

        if "_" not in screenWord:
            drawWord()
            writeErrorMessage("Excellent!!! YOU WIN!!!")
            gameOn = False









    #check the guess()

    #if guess is letter
    # check the letter
    # tell them if right or wrong
    # if its wrong show it on the screen
    # if its wrong take away a chance
    # if its wrong add a body part
    # if its right show the letter
    # if you are wrong and you are out of chances then stop the game

    #if they guess the word  -- done
    #if they are right they win -- done
    #if they are wrong they lose -- done



















turtle.mainloop()






