# Match The Cards Game Code

# Importing libraries and pygameRogers Module
import random
import sys
import pygame
import easygui
from pygameModule import *

# Creating new Game
g = Game(1280,760)

# ------------------------------- Defining Standard Colors --------------------------------------------------------
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (31,120,55)
RED = (255,0,0)
BROWN = (52,28,3)
YELLOW = (255, 215, 0)

# ------------------------------- Creating Resources ---------------------------------------------
simpleBackground = g.makeBackground(BLACK)
menuBackground = g.makeBackground("img\\menubg.png")
tableBackground = g.makeBackground("img\\table3.png")
finalBackground = g.makeBackground("img\\finalbg.png")
howToPlayBackground = g.makeBackground("img\\howto.png")
normalFont = g.makeFont("sans-serif", 50)
normalFont2 = g.makeFont("MS Serif", 50)
restartFont = g.makeFont("MS-serif", 35)
timeFont = g.makeFont("Arial", 30)
introFont1 = g.makeFont("sans-serif", 50)
introFont2 = g.makeFont("Monospace", 85)


diamondPics = []
heartPics = []
spadePics = []
clubPics = []

for i in range (2, 15):
	diamondPics.append(g.makeSpriteImage("cards\\DIAMONDS" + str(i) + ".jpg"))
for i in range(2,15):
	heartPics.append(g.makeSpriteImage("cards\\HEARTS" + str(i)+ ".jpg"))
for i in range(2,15):
	spadePics.append(g.makeSpriteImage("cards\\SPADES" + str(i)+".jpg"))
for i in range(2,15):
	clubPics.append(g.makeSpriteImage("cards\\CLUBS" + str(i)+".jpg"))
topCard = g.makeSpriteImage("cards\\TOP.jpg")
blankCard = g.makeSpriteImage("img\\blank.png")


# ------------------------------- Creating Rooms --------------------------------------------------

r0 = Room("Main Menu | Match The Cards - Shayyan Husein", menuBackground)
r1 = Room("Match The Cards | Match The Cards - Shayyan Husein",tableBackground)
r2 = Room("Final Screen | Match The Cards - Shayyan Husein", finalBackground)
r3 = Room("How to Play | Match The Cards - Shayyan Husein", howToPlayBackground)
g.addRoom(r0)																	
g.addRoom(r1)
g.addRoom(r2)
g.addRoom(r3)


# ------------------------------ Classes for Game Objects --------------------------------------------

# Singular Card object that will be used in a deck
class Card(GameObject):
	def __init__(self, picture, value, suit, xPos, yPos):
		GameObject.__init__(self, picture)

		self.value = value			
		self.suit = suit
		self.rect.x = xPos
		self.rect.y = yPos
		self.faceDown = topCard
		self.faceUp = picture
		self.image = self.faceDown
		self.timer = Alarm()

	#Update game State based on input states
	def update(self):

		#Check for Mouse Press Event
		self.checkMousePressedOnMe(event)

		# Checks for mouse release and if the card is face down
		if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP and len(deck.upList) < 2 and self.image == self.faceDown:
			self.image = self.faceUp
			deck.upList.append(self)
			self.mouseHasPressedOnMe = False
			# If there are two cards up, the timer is set to 1 second before evaluating if the cards are the same
			if len(deck.upList) == 2:
				deck.timer.setAlarm(1000)

		# Checks if the timer is finished (allows user to see the cards being compared instead of instantly comparing them) and checking if the cards are the same
		if len(deck.upList) == 2:
			if deck.timer.finished():
				# If the cards are the same, they are removed from the game
				if deck.upList[0].value == deck.upList[1].value:
					deck.upList[0].image = blankCard
					deck.upList[1].image = blankCard
					deck.upList[0].kill()
					deck.upList[1].kill()
					deck.upList = []
					# keeps track of how many cards have been removed from the game
					deck.cardsGone += 2
				else:
					# If the cards are not the same, they are flipped back over
					deck.upList[0].image = deck.upList[0].faceDown
					deck.upList[1].image = deck.upList[1].faceDown
					deck.upList = []


	# Output the string representation of the object if needed
	def __str__(self):
		return str(self.value) + self.suit

# Card Deck of Cards Class
class CardDeck(GameObject):

	def __init__(self, picture, xPos, yPos,):
		GameObject.__init__(self, picture)

		self.rect.x = xPos
		self.rect.y = yPos
		self.deck = []
		self.upList = []
		l1, l2, l3, l4 = [], [], [], []
		self.cardsGone = 0
		self.timer = Alarm()


		# ------------------ Creating a Shorter Deck by Making a List of Card Objects ------------------ 
		for i in range(0, len(diamondPics) - 4):										 

			c = Card(diamondPics[i], (i+2), "D", 50 + i*85, 80)
			l1.append(c)
			r1.addObject(c)
		self.deck=(l1)

		for i in range(0,len(heartPics) - 4):
			c = Card(heartPics[i], (i+2), "H", 50 + i*85, 230)
			l2.append(c)
			r1.addObject(c)
		self.deck+=(l2)

		for i in range(0,len(spadePics) - 4):
			c = Card(spadePics[i], (i+2), "S", 50 + i*85, 380)
			l3.append(c)
			r1.addObject(c)
		self.deck+=(l3)

		for i in range(0,len(clubPics) - 4):
			c = Card(clubPics[i], (i+2), "C", 50 + i*85, 530)
			l4.append(c)
			r1.addObject(c)
		self.deck+=(l4)

		# ------------------ Shuffle Deck ------------------ 
		self.deck = random.sample(self.deck, len(self.deck))
		l1, l2, l3, l4 = self.deck[0:9], self.deck[9:18], self.deck[18:27], self.deck[27:36]
		self.deck = []
		self.deck.append(l1)
		self.deck.append(l2)
		self.deck.append(l3)
		self.deck.append(l4)
		for i in range(4):
			for j in range(9):
				self.deck[i][j].rect.x = 120 + j*120
				self.deck[i][j].rect.y = 130 + i*150
	


	# Output if needed
	def __str__(self):
		s = ""
		print("Deck:")
		for i in range(len(self.deck)):
			for j in range(len(self.deck[i])):
				s = s + str((self.deck[i][j])) + " "
			s = s + "\n" 
		return s

# Creating Menu Buttons to navigate between rooms
class MenuButton(TextRectangle):
	def __init__(self, goToRoomIndex, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
		TextRectangle.__init__(self,text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)
		self.clickedRoomIndex = goToRoomIndex
	#Update game State based on input states
	def update(self):

		#Check for Mouse Press Event
		self.checkMousePressedOnMe(event)

		#Wait until mouse released to generate
		if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
			g.goToRoom(self.clickedRoomIndex)
			self.mouseHasPressedOnMe = False

# Creating Restart Button to restart the game
class RestartButton(TextRectangle):
	def __init__(self, goToRoomIndex, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
		TextRectangle.__init__(self,text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)
		self.clickedRoomIndex = goToRoomIndex
		self.index = 0
	#Update game State based on input states
	def update(self):

		#Check for Mouse Press Event
		self.checkMousePressedOnMe(event)

		#Wait until mouse released to generate
		if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
			g.goToRoom(self.clickedRoomIndex)
			deck = CardDeck(topCard, 2000,2000)
			r1.addObject(deck)
			timeText.restart()
			self.mouseHasPressedOnMe = False
			
# Creating Exit Button
class ExitButton(TextRectangle):
	def __init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
		TextRectangle.__init__(self,text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)
	#Update game State based on input states
	def update(self):

		#Check for Mouse Press Event
		self.checkMousePressedOnMe(event)

		#Wait until mouse released to generate
		if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
			pygame.quit()
			sys.exit()

# Time Display Class
class DisplayTimer(TextRectangle):

	def __init__(self,text, xPos, yPos, font, textColor, buttonWidth = None, buttonHeight = None, buttonColor = None):
		TextRectangle.__init__(self,text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)

		# Creating Timer variable for timer loop below
		self.seconds = int(text) 
		self.timer = Alarm()
		self.minutes = 0
		self.winningTimeSeconds = 0
		self.printTime = True
		self.setup = True
		self.hasRestarted = False

	# Restarts variables for reiteration of game
	def restart(self):
		self.timer = Alarm()
		self.seconds = 0
		self.minutes = 0
		self.winningTimeSeconds = 0
		self.printTime = True
		self.setup = True
		deck.cardsGone = 0
		self.hasRestarted = True


	# Manages how the time is displayed
	def timeManager(self):

		# if the seconds is over 60, make it 0 and add 1 to minutes
		if self.seconds > 59:
			self.seconds = 0
			self.minutes += 1
		if self.seconds < 10:
			self.extraZero = "0"
		else:
			self.extraZero = ""

		# set self.text to the minutes and seconds
		self.text = str(self.minutes) + ":" + (self.extraZero) + str(self.seconds)




	# Update Game 
	def update(self):
		if self.setup:
			self.timer.setAlarm(1000)
			self.setup = False
		self.timeManager()
		self.setText(self.text)

		# Runs a timer until timer variable reaches 0
		if self.timer.finished() and self.seconds >= 0 and deck.cardsGone != 36:
			self.timer.setAlarm(1000)
			self.seconds += 1
		elif deck.cardsGone == 36 and self.printTime:
			self.winningTimeSeconds = self.seconds + self.minutes*60
			print(self.winningTimeSeconds, " seconds is your time.")
			self.printTime = False 
			
			# Outputting the username and time to a file and sorting it by time (lowest to highest)
			f = open("scores.txt", "a")
			f.write(username.username + "," + str(self.winningTimeSeconds) + "\n")			
			f.close()

			# Moving to the highscores room
			g.goToRoom(2)

# Text to display Username
class Username(TextRectangle):

	def __init__(self,text, xPos, yPos, font, textColor, buttonWidth = None, buttonHeight = None, buttonColor = None):
		TextRectangle.__init__(self,text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)
		self.setup = True
		self.timer = Alarm()
		self.timer.setAlarm(100)
		
	
	def update(self):
		if self.setup and self.timer.finished():
			self.username = easygui.enterbox("What is your username? (1 Character Min, 20 Character Max)", "Enter Username to Continue")
			while self.username == None or self.username == "" or (len(self.username)) > 20:
				self.username = easygui.enterbox("What is your username? (1 Character Min, 20 Character Max)", "Enter Username to Continue")
			self.setText(self.username)
			self.rect.x = 1150 - (len(self.username)*20)
			self.setup = False

# Leaderboard Display
class LeaderboardDisplay(TextRectangle):

	def __init__(self,text, xPos, yPos, font, textColor, buttonWidth = None, buttonHeight = None, buttonColor = None):
		TextRectangle.__init__(self,text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)
		

	# convert seconds to minutes and seconds
	def secondsToTime(self, seconds):
		seconds = int(seconds)
		mins = seconds // 60
		secs = seconds % 60
		# if the seconds is less than 10, add a 0 in front of it
		if secs < 10:
			extraZero = "0"
		else:
			extraZero = ""

		timeString = str(mins) + ":" + (extraZero) + str(secs)
		# set self.text to the minutes and seconds
		return timeString


	# Update Game
	def update(self):
	
		# open the file
		f = open("scores.txt", "r")

		# take the first 3 lines as 3 different list
		leaderboard = []
		while True:
			line = f.readline()
			if line == "":
				break
			else:

				tokens = line.split(",")

				row = []
				row.append(tokens[0])
				# strip out the newline character
				row.append(tokens[1].strip("\n"))
				leaderboard.append(row)

		# sorting the leaderboard based on seconds taken to complete the game
		newLeaderboard = sorted(leaderboard, key=lambda x: int(x[1]))

		p1.setText(newLeaderboard[0][0])
		s1.setText(self.secondsToTime(newLeaderboard[0][1]))
		p2.setText(newLeaderboard[1][0])
		s2.setText(self.secondsToTime(newLeaderboard[1][1]))
		p3.setText(newLeaderboard[2][0])
		s3.setText(self.secondsToTime(newLeaderboard[2][1]))
		cp.setText(username.username)
		cs.setText(self.secondsToTime(leaderboard[-1][1]))

#------------------------------- INITIALIZE OBJECTS AND ADD THEM TO THEIR ROOMS ----------------------------------

# making room navigation buttons
startButton = MenuButton(1,"START", 390,350,normalFont, YELLOW, 220, 90, BLACK)	
r0.addObject(startButton)
startButton2 = MenuButton(1,"START", 90,43,normalFont, YELLOW, 180, 80, BLACK)	
r3.addObject(startButton2)
instructionsButton = MenuButton(3," HOW TO PLAY ", 630,350,normalFont, YELLOW, 270, 90, BLACK)	
r0.addObject(instructionsButton)

# make a restart button and an exit button
restartButton = RestartButton(1," RESTART ", 27,275,restartFont, YELLOW, 150, 70, BLACK)
r2.addObject(restartButton)
exitButton = ExitButton(" EXIT ", 27,375,restartFont, YELLOW, 150, 70, BLACK)
r2.addObject(exitButton)

# Make a deck of cards
deck = CardDeck(topCard, 2000,2000)

# Make a timer
timeText = DisplayTimer("1", 80,60,normalFont,WHITE)
r1.addObject(timeText)

# Make a username
username = Username("", 1200, 60, normalFont, WHITE)
r0.addObject(username)
r1.addObject(username)

# Make a leaderboard
leaderboardDisplay = LeaderboardDisplay("", 100, 100, normalFont, WHITE)
r2.addObject(leaderboardDisplay)

# text boxes for top 3 leaderboard times and current player's time
p1 = TextRectangle("", 278, 270, normalFont2, BLACK)
s1 = TextRectangle("", 970, 270, normalFont2, BLACK)
p2 = TextRectangle("", 278, 382, normalFont2, BLACK)
s2 = TextRectangle("", 970, 382, normalFont2, BLACK)
p3 = TextRectangle("", 278, 490, normalFont2, BLACK)
s3 = TextRectangle("", 970, 490, normalFont2, BLACK)
cp = TextRectangle("", 278, 665, normalFont2, WHITE)
cs = TextRectangle("", 970, 665, normalFont2, WHITE)
r2.addObject(p1)
r2.addObject(s1)
r2.addObject(p2)
r2.addObject(s2)
r2.addObject(p3)
r2.addObject(s3)
r2.addObject(cp)
r2.addObject(cs)

#-------------------------------------  START GAME  ------------------------------------------
g.start()
while g.running :

	#How often the game loop executes each second
	dt = g.clock.tick(60)

	#Check Game Events
	for event in pygame.event.get():

		#Check for [x]
		if event.type == pygame.QUIT:
			g.stop()

	#Update All objects in Room 
	g.currentRoom().updateObjects()

	#Render Background to the game surface
	g.currentRoom().renderBackground(g)

	#Render Objects to the game surface
	g.currentRoom().renderObjects(g)

	#Draw everything on the screen
	pygame.display.flip()

pygame.quit()