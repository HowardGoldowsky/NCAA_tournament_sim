#! /usr/bin/env python

# MarchMadness.py
# A very small NCAA basketball simulation game, with eight hard-coded teams.
# Written by Howard Goldowsky, 2013

import Tkinter
import random
import time


class Team():
    def __init__(self, name):
        self.wins = 0
        self.points = 0
        self.name = name
        self.scorePosX = 0  # X coordinate of score
        self.scorePosY = 0  # Y coordinate of score
        self.text = w.create_text(self.scorePosX, self.scorePosY, text=self.points, anchor='w')

    def DisplayScore(self):
        w.delete(self.text)
        self.text = w.create_text(self.scorePosX, self.scorePosY, text=self.points, anchor='w')
        w.update()


# END Class Team() 

class Application():
    def __init__(self, parent):

        self.timePosX = 340
        self.timePosY = 50
        self.round = 0
        self.time_remain = 120
        self.play_button = Tkinter.Button(text='Play!', command=self.PlayGames)
        self.play_button.place(x=290, y=20, width=100, height=20)
        self.time_text = w.create_text(self.timePosX, self.timePosY, text=self.time_remain, anchor='w')
        self.time_label = w.create_text(self.timePosX - 100, self.timePosY, text='Time Remaining:', anchor='w',
                                        fill='blue')

        # Initialize teams
        Georgetown = Team('Georgetown')
        MIT = Team('Buffalo')
        Iona = Team('Iona')
        Stanford = Team('Stanford')
        Louisville = Team('Lousiville')
        Michigan = Team('Michigan')
        Harvard = Team('Harvard')
        Kansas = Team('Kansas')

        self.TeamList = [Georgetown, MIT, Iona, Stanford, Louisville, Michigan, Harvard, Kansas]  # Global variable
        random.shuffle(self.TeamList)
        self.tempTeamList = list(self.TeamList)  # copies by value

        self.InitDisplay()

    def DisplayTimeRemain(self):

        w.delete(self.time_text)
        self.time_text = w.create_text(self.timePosX, self.timePosY, text=self.time_remain, anchor='w', fill='red')
        w.update()

    def PlayGames(self):

        for team in self.TeamList:
            team.points = 0

        if len(self.TeamList) == 1:
            print ('Game Over')
            return

        self.round = self.round + 1

        for i in range(0, 120):
            for team in self.TeamList:
                time.sleep(0.01)
                team.points = team.points + int(random.randint(0, 99) > 55)
                team.DisplayScore()
                self.time_remain = 119 - i
                self.DisplayTimeRemain()

        for i, team in enumerate(self.TeamList):

            if i % 2 == 0:

                if self.TeamList[i].points > self.TeamList[i + 1].points:
                    self.TeamList[i].wins = self.TeamList[i].wins + 1  # add win to winning team

                if self.TeamList[i].points < self.TeamList[i + 1].points:
                    self.TeamList[i + 1].wins = self.TeamList[i + 1].wins + 1  # add win to winning team

                if self.TeamList[i].points == self.TeamList[i + 1].points:
                    self.TeamList[i].wins = self.TeamList[i].wins + 1  # add win to winning team
                    self.TeamList[i].points = self.TeamList[
                                                  i].points + 1  # cheat and give first team an extra point and the win
                    self.TeamList[i].DisplayScore()

        self.tempTeamList = list(self.TeamList)

        for team in self.TeamList:
            if team.wins == self.round - 1:
                self.tempTeamList.remove(team)

        self.TeamList = list(self.tempTeamList)
        self.UpdateDisplay()  # Display remaining teams

    def UpdateDisplay(self):

        if len(self.TeamList) == 4:

            for i, team in enumerate(self.TeamList):
                team.scorePosX = 180
                team.scorePosY = i * 80 + 45
                w.create_text(team.scorePosX - 70, team.scorePosY, text=team.name, anchor='w')
                team.text = w.create_text(team.scorePosX, team.scorePosY, text=0, anchor='w')

        if len(self.TeamList) == 2:

            for i, team in enumerate(self.TeamList):
                team.scorePosX = 280
                team.scorePosY = i * 160 + 90
                w.create_text(team.scorePosX - 70, team.scorePosY, text=team.name, anchor='w')
                team.text = w.create_text(team.scorePosX, team.scorePosY, text=0, anchor='w')

        if len(self.TeamList) == 1:  # Just display champion

            for team in self.TeamList:
                team.scorePosX = 310
                team.scorePosY = 170
                w.create_text(team.scorePosX, team.scorePosY, text=team.name, fill='black', anchor='w')
            # team.text = w.create_text(team.scorePosX,team.scorePosY,text=0,anchor='w')

    def InitDisplay(self):

        for i in range(len(self.TeamList)):

            ypos = (i + 1) * 40
            w.create_line(0, ypos, 100, ypos)
            w.create_text(10, i * 40 + 25, text=self.TeamList[i].name, anchor='w')  # print 8 team names
            self.TeamList[i].scorePosX = 80
            self.TeamList[i].scorePosY = ypos - 15
            self.TeamList[i].DisplayScore()

            if i % 2 == 0:
                ypos = (i + 1.5) * 40
                w.create_line(100, ypos, 200, ypos)
                w.create_line(100, ypos - 20, 100, ypos + 20)

            if i % 4 == 0:
                ypos = (i + 2.5) * 40
                w.create_line(200, ypos, 300, ypos)
                w.create_line(200, ypos - 40, 200, ypos + 40)

            if i % 8 == 0:
                ypos = (i + 4.5) * 40
                w.create_line(300, ypos, 400, ypos)
                w.create_line(300, ypos - 80, 300, ypos + 80)

        w.create_text(320, 200, text='Champion', fill='blue', anchor='w')


# END Class App() 

# Begin the main program

# Main program
root = Tkinter.Tk()  # Root level window method call
root.title('March Madness')  # Add title to window
w = Tkinter.Canvas(root, width=400, height=350)  # Create a canvas object, root as parent
w.grid()  # Locate using pack()

app = Application(root)  # Create an instance of the main app
root.mainloop()  # Begin the main loop of the GUI instance
