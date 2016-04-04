from tkinter import*
from gameboard import*
import sys

root = Tk()
root.title("Project Lights")
root.geometry("900x700")
bgImage = PhotoImage(file = 'background.png')

images = list()
bg = PhotoImage(file = 'bg.png')
block = PhotoImage(file = 'block.png')
LaserOne = PhotoImage(file = 'LaserOne.png')
LaserTwo = PhotoImage(file = 'LaserTwo.png')
LensX = PhotoImage(file = 'LensX.png')
LensY = PhotoImage(file = 'LensY.png')
Mirror1 = PhotoImage(file = 'Mirror1.png')
Mirror2 = PhotoImage(file = 'Mirror2.png')
Mirror3 = PhotoImage(file = 'Mirror3.png')
Mirror4 = PhotoImage(file = 'Mirror4.png')
Mirror1B = PhotoImage(file = 'Mirror1B.png')
Mirror2B = PhotoImage(file = 'Mirror2B.png')
Mirror3B = PhotoImage(file = 'Mirror3B.png')
Mirror4B = PhotoImage(file = 'Mirror4B.png')
Mirror1R = PhotoImage(file = 'Mirror1R.png')
Mirror2R = PhotoImage(file = 'Mirror2R.png')
Mirror3R = PhotoImage(file = 'Mirror3R.png')
Mirror4R = PhotoImage(file = 'Mirror4R.png')
B0 = PhotoImage(file = 'B0.png')
B0B45 = PhotoImage(file = 'B0B45.png')
B0B45B90 = PhotoImage(file = 'B0B45B90.png')
B0B45B90B135 = PhotoImage(file = 'B0B45B90B135.png')
B0B45B90R135 = PhotoImage(file = 'B0B45B90R135.png')
B0B45B135 = PhotoImage(file = 'B0B45B135.png')
B0B45R90 = PhotoImage(file = 'B0B45R90.png')
B0B45R90B135 = PhotoImage(file = 'B0B45R90B135.png')
B0B45R90R135 = PhotoImage(file = 'B0B45R90R135.png')
B0B45R135 = PhotoImage(file = 'B0B45R135.png')
B0B90 = PhotoImage(file = 'B0B90.png')
B0B90B135 = PhotoImage(file = 'B0B90B135.png')
B0B90R135 = PhotoImage(file = 'B0B90R135.png')
B0B135 = PhotoImage(file = 'B0B135.png')
B0R45 = PhotoImage(file = 'B0R45.png')
B0R45B90 = PhotoImage(file = 'B0R45B90.png')
B0R45B90B135 = PhotoImage(file = 'B0R45B90B135.png')
B0R45B90R135 = PhotoImage(file = 'B0R45B90R135.png')
B0R45B135 = PhotoImage(file = 'B0R45B135.png')
B0R45R90 = PhotoImage(file = 'B0R45R90.png')
B0R45R90B135 = PhotoImage(file = 'B0R45R90B135.png')
B0R45R90R135 = PhotoImage(file = 'B0R45R90R135.png')
B0R45R135 = PhotoImage(file = 'B0R45R135.png')
B0R90 = PhotoImage(file = 'B0R90.png')
B0R90B135 = PhotoImage(file = 'B0R90B135.png')
B0R90R135 = PhotoImage(file = 'B0R90R135.png')
B0R135 = PhotoImage(file = 'B0R135.png')
B45 = PhotoImage(file = 'B45.png')
B45B90B135 = PhotoImage(file = 'B45B90B135.png')
B45B90R135 = PhotoImage(file = 'B45B90R135.png')
B45B135 = PhotoImage(file = 'B45B135.png')
B45R90 = PhotoImage(file = 'B45R90.png')
B45R90B135 = PhotoImage(file = 'B45R90B135.png')
B45R90R135 = PhotoImage(file = 'B45R90R135.png')
B45R135 = PhotoImage(file = 'B45R135.png')
B90 = PhotoImage(file = 'B90.png')
B90B45 = PhotoImage(file = 'B90B45.png')
B90B135 = PhotoImage(file = 'B90B135.png')
B90R135 = PhotoImage(file = 'B90R135.png')
B135 = PhotoImage(file = 'B135.png')
R0 = PhotoImage(file = 'R0.png')
R0R45 = PhotoImage(file = 'R0R45.png')
R0R45R90 = PhotoImage(file = 'R0R45R90.png')
R90 = PhotoImage(file = 'R90.png')
R90B135 = PhotoImage(file = 'R90B135.png')
R90R135 = PhotoImage(file = 'R90R135.png')
R135 = PhotoImage(file = 'R135.png')
R0B45 = PhotoImage(file = 'R0B45.png')
R0B45B90B135 = PhotoImage(file = 'R0B45B90B135.png')
R0B45B90R135 = PhotoImage(file = 'R0B45B90R135.png')
R0B45B135 = PhotoImage(file = 'R0B45B135.png')
R0B45R90 = PhotoImage(file = 'R0B45R90.png')
R0B45R90B135 = PhotoImage(file = 'R0B45R90B135.png')
R0B45R90R135 = PhotoImage(file = 'R0B45R90R135.png')
R0B45R135 = PhotoImage(file = 'R0B45R135.png')
R0B90 = PhotoImage(file = 'R0B90.png')
R0B90B135 = PhotoImage(file = 'R0B90B135.png')
R0B90R135 = PhotoImage(file = 'R0B90R135.png')
R0B135 = PhotoImage(file = 'R0B135.png')
R0R45B90 = PhotoImage(file = 'R0R45B90.png')
R0R45B90B135 = PhotoImage(file = 'R0R45B90B135.png')
R0R45B90R135 = PhotoImage(file = 'R0R45B90R135.png')
R0R45B135 = PhotoImage(file = 'R0R45B135.png')
R0R45R90B135 = PhotoImage(file = 'R0R45R90B135.png')
R0R45R90R135 = PhotoImage(file = 'R0R45R90R135.png')
R0R45R135 = PhotoImage(file = 'R0R45R135.png')
R0R90 = PhotoImage(file = 'R0R90.png')
R0R90B135 = PhotoImage(file = 'R0R90B135.png')
R0R90R135 = PhotoImage(file = 'R0R90R135.png')
R0R135 = PhotoImage(file = 'R0R135.png')
R45 = PhotoImage(file = 'R45.png')
R45B90 = PhotoImage(file = 'R45B90.png')
R45B90B135 = PhotoImage(file = 'R45B90B135.png')
R45B90R135 = PhotoImage(file = 'R45B90R135.png')
R45B135 = PhotoImage(file = 'R45B135.png')
R45R90 = PhotoImage(file = 'R45R90.png')
R45R90B135 = PhotoImage(file = 'R45R90B135.png')
R45R90R135 = PhotoImage(file = 'R45R90R135.png')
R45R135 = PhotoImage(file = 'R45R135.png')

images.append(bg)               #0
images.append(LaserOne)         #1
images.append(LaserTwo)         #2
images.append(LensX)            #3
images.append(LensY)            #4
images.append(Mirror1)          #5
images.append(Mirror2)          #6
images.append(Mirror3)          #7
images.append(Mirror4)          #8
images.append(block)            #9
images.append(Mirror1B)         #10
images.append(Mirror2B)         #11
images.append(Mirror3B)         #12
images.append(Mirror4B)         #13
images.append(Mirror1R)         #14
images.append(Mirror2R)         #15
images.append(Mirror3R)         #16
images.append(Mirror4R)         #17
images.append(B0) 	            #18
images.append(B0B45) 	        #19
images.append(B0B45B90) 	    #20
images.append(B0B45B90B135)     #21
images.append(B0B45B90R135) 	#22
images.append(B0B45B135) 	    #23
images.append(B0B45R90) 	    #24
images.append(B0B45R90B135) 	#25
images.append(B0B45R90R135) 	#26
images.append(B0B45R135) 	    #27
images.append(B0B90) 	        #28
images.append(B0B90B135) 	    #29
images.append(B0B90R135) 	    #30
images.append(B0B135) 	        #31
images.append(B0R45) 	        #32
images.append(B0R45B90) 	    #33
images.append(B0R45B90B135) 	#34
images.append(B0R45B90R135) 	#35
images.append(B0R45B135) 	    #36
images.append(B0R45R90) 	    #37
images.append(B0R45R90B135) 	#38
images.append(B0R45R90R135) 	#39
images.append(B0R45R135) 	    #40
images.append(B0R90) 	        #41
images.append(B0R90B135) 	    #42
images.append(B0R90R135) 	    #43
images.append(B0R135) 	        #44
images.append(B45) 	            #45
images.append(B45B90B135) 	    #46
images.append(B45B90R135) 	    #47
images.append(B45B135) 	        #48
images.append(B45R90) 	        #49
images.append(B45R90B135) 	    #50
images.append(B45R90R135) 	    #51
images.append(B45R135) 	        #52
images.append(B90)          	#53
images.append(B90B45) 	        #54
images.append(B90B135) 	        #55
images.append(B90R135) 	        #56
images.append(B135) 	        #57
images.append(R0) 	            #58
images.append(R0R45) 	        #59
images.append(R0R45R90) 	    #60
images.append(R90) 	            #61
images.append(R90B135) 	        #62
images.append(R90R135) 	        #63
images.append(R135) 	        #64
images.append(R0B45) 	        #65
images.append(R0B45B90B135) 	#66
images.append(R0B45B90R135) 	#67
images.append(R0B45B135) 	    #68
images.append(R0B45R90) 	    #69
images.append(R0B45R90B135)     #70
images.append(R0B45R90R135) 	#71
images.append(R0B45R135) 	    #72
images.append(R0B90) 	        #73
images.append(R0B90B135) 	    #74
images.append(R0B90R135) 	    #75
images.append(R0B135) 	        #76
images.append(R0R45B90) 	    #77
images.append(R0R45B90B135) 	#78
images.append(R0R45B90R135) 	#79
images.append(R0R45B135) 	    #80
images.append(R0R45R90B135) 	#81
images.append(R0R45R90R135) 	#82
images.append(R0R45R135) 	    #83
images.append(R0R90) 	        #84
images.append(R0R90B135)     	#85
images.append(R0R90R135) 	    #86
images.append(R0R135) 	        #87
images.append(R45) 	            #88
images.append(R45B90) 	        #89
images.append(R45B90B135) 	    #90
images.append(R45B90R135) 	    #91
images.append(R45B135) 	        #92
images.append(R45R90) 	        #93
images.append(R45R90B135) 	    #94
images.append(R45R90R135) 	    #95
images.append(R45R135) 	        #96


class Application(Frame):
    def closeWindow():
        exit()

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self,master)

        bgLabel = Label(root, image = bgImage)
        bgLabel.pack()
        self.buttons = list()
        self.selected = None

        self.mirror1Button = Button(master, image = Mirror1, state = ACTIVE)
        self.mirror2Button = Button(master, image = Mirror2, state = ACTIVE)
        self.mirror3Button = Button(master, image = Mirror3)
        self.mirror4Button = Button(master, image = Mirror4)
        self.lensXButton = Button(master, image = LensX)
        self.lensYButton = Button(master, image = LensY)
        self.blockButton = Button(master, image = block)

        self.buttonA1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonA12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonB12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonC12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonD12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE4 = Button(master, image = LaserOne, relief = SUNKEN, bd = 0)
        self.buttonE5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonE12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonF12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonG12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH4 = Button(master, image = LaserTwo, relief = SUNKEN, bd = 0)
        self.buttonH5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonH12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonI12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonJ12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonK12 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL1 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL2 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL3 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL4 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL5 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL6 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL7 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL8 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL9 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL10 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL11 = Button(master, image = bg, relief = SUNKEN, bd = 0)
        self.buttonL12 = Button(master, image = bg, relief = SUNKEN, bd = 0)

        self.mirror1Button.place(x = 820, y = 150, width = 50, height = 50)
        self.mirror2Button.place(x = 720, y = 150, width = 50, height = 50)
        self.mirror3Button.place(x = 720, y = 50, width = 50, height = 50)
        self.mirror4Button.place(x = 820, y = 50, width = 50, height = 50)
        self.lensXButton.place(x = 720, y = 250, width = 50, height = 50)
        self.lensYButton.place(x = 820, y = 250, width = 50, height = 50)
        self.blockButton.place(x = 720, y = 350, width = 50, height = 50)
        
        self.buttonA1.place(x = 50, y = 50, width = 50, height = 50)
        self.buttonA2.place(x = 100, y = 50, width = 50, height = 50)
        self.buttonA3.place(x = 150, y = 50, width = 50, height = 50)
        self.buttonA4.place(x = 200, y = 50, width = 50, height = 50)
        self.buttonA5.place(x = 250, y = 50, width = 50, height = 50)
        self.buttonA6.place(x = 300, y = 50, width = 50, height = 50)
        self.buttonA7.place(x = 350, y = 50, width = 50, height = 50)
        self.buttonA8.place(x = 400, y = 50, width = 50, height = 50)
        self.buttonA9.place(x = 450, y = 50, width = 50, height = 50)
        self.buttonA10.place(x = 500, y = 50, width = 50, height = 50)
        self.buttonA11.place(x = 550, y = 50, width = 50, height = 50)
        self.buttonA12.place(x = 600, y = 50, width = 50, height = 50)
        self.buttonB1.place(x = 50, y = 100, width = 50, height = 50)
        self.buttonB2.place(x = 100, y = 100, width = 50, height = 50)
        self.buttonB3.place(x = 150, y = 100, width = 50, height = 50)
        self.buttonB4.place(x = 200, y = 100, width = 50, height = 50)
        self.buttonB5.place(x = 250, y = 100, width = 50, height = 50)
        self.buttonB6.place(x = 300, y = 100, width = 50, height = 50)
        self.buttonB7.place(x = 350, y = 100, width = 50, height = 50)
        self.buttonB8.place(x = 400, y = 100, width = 50, height = 50)
        self.buttonB9.place(x = 450, y = 100, width = 50, height = 50)
        self.buttonB10.place(x = 500, y = 100, width = 50, height = 50)
        self.buttonB11.place(x = 550, y = 100, width = 50, height = 50)
        self.buttonB12.place(x = 600, y = 100, width = 50, height = 50)
        self.buttonC1.place(x = 50, y = 150, width = 50, height = 50)
        self.buttonC2.place(x = 100, y = 150, width = 50, height = 50)
        self.buttonC3.place(x = 150, y = 150, width = 50, height = 50)
        self.buttonC4.place(x = 200, y = 150, width = 50, height = 50)
        self.buttonC5.place(x = 250, y = 150, width = 50, height = 50)
        self.buttonC6.place(x = 300, y = 150, width = 50, height = 50)
        self.buttonC7.place(x = 350, y = 150, width = 50, height = 50)
        self.buttonC8.place(x = 400, y = 150, width = 50, height = 50)
        self.buttonC9.place(x = 450, y = 150, width = 50, height = 50)
        self.buttonC10.place(x = 500, y = 150, width = 50, height = 50)
        self.buttonC11.place(x = 550, y = 150, width = 50, height = 50)
        self.buttonC12.place(x = 600, y = 150, width = 50, height = 50)
        self.buttonD1.place(x = 50, y = 200, width = 50, height = 50)
        self.buttonD2.place(x = 100, y = 200, width = 50, height = 50)
        self.buttonD3.place(x = 150, y = 200, width = 50, height = 50)
        self.buttonD4.place(x = 200, y = 200, width = 50, height = 50)
        self.buttonD5.place(x = 250, y = 200, width = 50, height = 50)
        self.buttonD6.place(x = 300, y = 200, width = 50, height = 50)
        self.buttonD7.place(x = 350, y = 200, width = 50, height = 50)
        self.buttonD8.place(x = 400, y = 200, width = 50, height = 50)
        self.buttonD9.place(x = 450, y = 200, width = 50, height = 50)
        self.buttonD10.place(x = 500, y = 200, width = 50, height = 50)
        self.buttonD11.place(x = 550, y = 200, width = 50, height = 50)
        self.buttonD12.place(x = 600, y = 200, width = 50, height = 50)
        self.buttonE1.place(x = 50, y = 250, width = 50, height = 50)
        self.buttonE2.place(x = 100, y = 250, width = 50, height = 50)
        self.buttonE3.place(x = 150, y = 250, width = 50, height = 50)
        self.buttonE4.place(x = 200, y = 250, width = 50, height = 50)
        self.buttonE5.place(x = 250, y = 250, width = 50, height = 50)
        self.buttonE6.place(x = 300, y = 250, width = 50, height = 50)
        self.buttonE7.place(x = 350, y = 250, width = 50, height = 50)
        self.buttonE8.place(x = 400, y = 250, width = 50, height = 50)
        self.buttonE9.place(x = 450, y = 250, width = 50, height = 50)
        self.buttonE10.place(x = 500, y = 250, width = 50, height = 50)
        self.buttonE11.place(x = 550, y = 250, width = 50, height = 50)
        self.buttonE12.place(x = 600, y = 250, width = 50, height = 50)
        self.buttonF1.place(x = 50, y = 300, width = 50, height = 50)
        self.buttonF2.place(x = 100, y = 300, width = 50, height = 50)
        self.buttonF3.place(x = 150, y = 300, width = 50, height = 50)
        self.buttonF4.place(x = 200, y = 300, width = 50, height = 50)
        self.buttonF5.place(x = 250, y = 300, width = 50, height = 50)
        self.buttonF6.place(x = 300, y = 300, width = 50, height = 50)
        self.buttonF7.place(x = 350, y = 300, width = 50, height = 50)
        self.buttonF8.place(x = 400, y = 300, width = 50, height = 50)
        self.buttonF9.place(x = 450, y = 300, width = 50, height = 50)
        self.buttonF10.place(x = 500, y = 300, width = 50, height = 50)
        self.buttonF11.place(x = 550, y = 300, width = 50, height = 50)
        self.buttonF12.place(x = 600, y = 300, width = 50, height = 50)
        self.buttonG1.place(x = 50, y = 350, width = 50, height = 50)
        self.buttonG2.place(x = 100, y = 350, width = 50, height = 50)
        self.buttonG3.place(x = 150, y = 350, width = 50, height = 50)
        self.buttonG4.place(x = 200, y = 350, width = 50, height = 50)
        self.buttonG5.place(x = 250, y = 350, width = 50, height = 50)
        self.buttonG6.place(x = 300, y = 350, width = 50, height = 50)
        self.buttonG7.place(x = 350, y = 350, width = 50, height = 50)
        self.buttonG8.place(x = 400, y = 350, width = 50, height = 50)
        self.buttonG9.place(x = 450, y = 350, width = 50, height = 50)
        self.buttonG10.place(x = 500, y = 350, width = 50, height = 50)
        self.buttonG11.place(x = 550, y = 350, width = 50, height = 50)
        self.buttonG12.place(x = 600, y = 350, width = 50, height = 50)
        self.buttonH1.place(x = 50, y = 400, width = 50, height = 50)
        self.buttonH2.place(x = 100, y = 400, width = 50, height = 50)
        self.buttonH3.place(x = 150, y = 400, width = 50, height = 50)
        self.buttonH4.place(x = 200, y = 400, width = 50, height = 50)
        self.buttonH5.place(x = 250, y = 400, width = 50, height = 50)
        self.buttonH6.place(x = 300, y = 400, width = 50, height = 50)
        self.buttonH7.place(x = 350, y = 400, width = 50, height = 50)
        self.buttonH8.place(x = 400, y = 400, width = 50, height = 50)
        self.buttonH9.place(x = 450, y = 400, width = 50, height = 50)
        self.buttonH10.place(x = 500, y = 400, width = 50, height = 50)
        self.buttonH11.place(x = 550, y = 400, width = 50, height = 50)
        self.buttonH12.place(x = 600, y = 400, width = 50, height = 50)
        self.buttonI1.place(x = 50, y = 450, width = 50, height = 50)
        self.buttonI2.place(x = 100, y = 450, width = 50, height = 50)
        self.buttonI3.place(x = 150, y = 450, width = 50, height = 50)
        self.buttonI4.place(x = 200, y = 450, width = 50, height = 50)
        self.buttonI5.place(x = 250, y = 450, width = 50, height = 50)
        self.buttonI6.place(x = 300, y = 450, width = 50, height = 50)
        self.buttonI7.place(x = 350, y = 450, width = 50, height = 50)
        self.buttonI8.place(x = 400, y = 450, width = 50, height = 50)
        self.buttonI9.place(x = 450, y = 450, width = 50, height = 50)
        self.buttonI10.place(x = 500, y = 450, width = 50, height = 50)
        self.buttonI11.place(x = 550, y = 450, width = 50, height = 50)
        self.buttonI12.place(x = 600, y = 450, width = 50, height = 50)
        self.buttonJ1.place(x = 50, y = 500, width = 50, height = 50)
        self.buttonJ2.place(x = 100, y = 500, width = 50, height = 50)
        self.buttonJ3.place(x = 150, y = 500, width = 50, height = 50)
        self.buttonJ4.place(x = 200, y = 500, width = 50, height = 50)
        self.buttonJ5.place(x = 250, y = 500, width = 50, height = 50)
        self.buttonJ6.place(x = 300, y = 500, width = 50, height = 50)
        self.buttonJ7.place(x = 350, y = 500, width = 50, height = 50)
        self.buttonJ8.place(x = 400, y = 500, width = 50, height = 50)
        self.buttonJ9.place(x = 450, y = 500, width = 50, height = 50)
        self.buttonJ10.place(x = 500, y = 500, width = 50, height = 50)
        self.buttonJ11.place(x = 550, y = 500, width = 50, height = 50)
        self.buttonJ12.place(x = 600, y = 500, width = 50, height = 50)
        self.buttonK1.place(x = 50, y = 550, width = 50, height = 50)
        self.buttonK2.place(x = 100, y = 550, width = 50, height = 50)
        self.buttonK3.place(x = 150, y = 550, width = 50, height = 50)
        self.buttonK4.place(x = 200, y = 550, width = 50, height = 50)
        self.buttonK5.place(x = 250, y = 550, width = 50, height = 50)
        self.buttonK6.place(x = 300, y = 550, width = 50, height = 50)
        self.buttonK7.place(x = 350, y = 550, width = 50, height = 50)
        self.buttonK8.place(x = 400, y = 550, width = 50, height = 50)
        self.buttonK9.place(x = 450, y = 550, width = 50, height = 50)
        self.buttonK10.place(x = 500, y = 550, width = 50, height = 50)
        self.buttonK11.place(x = 550, y = 550, width = 50, height = 50)
        self.buttonK12.place(x = 600, y = 550, width = 50, height = 50)
        self.buttonL1.place(x = 50, y = 600, width = 50, height = 50)
        self.buttonL2.place(x = 100, y = 600, width = 50, height = 50)
        self.buttonL3.place(x = 150, y = 600, width = 50, height = 50)
        self.buttonL4.place(x = 200, y = 600, width = 50, height = 50)
        self.buttonL5.place(x = 250, y = 600, width = 50, height = 50)
        self.buttonL6.place(x = 300, y = 600, width = 50, height = 50)
        self.buttonL7.place(x = 350, y = 600, width = 50, height = 50)
        self.buttonL8.place(x = 400, y = 600, width = 50, height = 50)
        self.buttonL9.place(x = 450, y = 600, width = 50, height = 50)
        self.buttonL10.place(x = 500, y = 600, width = 50, height = 50)
        self.buttonL11.place(x = 550, y = 600, width = 50, height = 50)
        self.buttonL12.place(x = 600, y = 600, width = 50, height = 50)

        self.buttons.append(self.buttonA1)
        self.buttons.append(self.buttonA2)
        self.buttons.append(self.buttonA3)
        self.buttons.append(self.buttonA4)
        self.buttons.append(self.buttonA5)
        self.buttons.append(self.buttonA6)
        self.buttons.append(self.buttonA7)
        self.buttons.append(self.buttonA8)
        self.buttons.append(self.buttonA9)
        self.buttons.append(self.buttonA10)
        self.buttons.append(self.buttonA11)
        self.buttons.append(self.buttonA12)
        self.buttons.append(self.buttonB1)
        self.buttons.append(self.buttonB2)
        self.buttons.append(self.buttonB3)
        self.buttons.append(self.buttonB4)
        self.buttons.append(self.buttonB5)
        self.buttons.append(self.buttonB6)
        self.buttons.append(self.buttonB7)
        self.buttons.append(self.buttonB8)
        self.buttons.append(self.buttonB9)
        self.buttons.append(self.buttonB10)
        self.buttons.append(self.buttonB11)
        self.buttons.append(self.buttonB12)
        self.buttons.append(self.buttonC1)
        self.buttons.append(self.buttonC2)
        self.buttons.append(self.buttonC3)
        self.buttons.append(self.buttonC4)
        self.buttons.append(self.buttonC5)
        self.buttons.append(self.buttonC6)
        self.buttons.append(self.buttonC7)
        self.buttons.append(self.buttonC8)
        self.buttons.append(self.buttonC9)
        self.buttons.append(self.buttonC10)
        self.buttons.append(self.buttonC11)
        self.buttons.append(self.buttonC12)
        self.buttons.append(self.buttonD1)
        self.buttons.append(self.buttonD2)
        self.buttons.append(self.buttonD3)
        self.buttons.append(self.buttonD4)
        self.buttons.append(self.buttonD5)
        self.buttons.append(self.buttonD6)
        self.buttons.append(self.buttonD7)
        self.buttons.append(self.buttonD8)
        self.buttons.append(self.buttonD9)
        self.buttons.append(self.buttonD10)
        self.buttons.append(self.buttonD11)
        self.buttons.append(self.buttonD12)
        self.buttons.append(self.buttonE1)
        self.buttons.append(self.buttonE2)
        self.buttons.append(self.buttonE3)
        self.buttons.append(self.buttonE4)
        self.buttons.append(self.buttonE5)
        self.buttons.append(self.buttonE6)
        self.buttons.append(self.buttonE7)
        self.buttons.append(self.buttonE8)
        self.buttons.append(self.buttonE9)
        self.buttons.append(self.buttonE10)
        self.buttons.append(self.buttonE11)
        self.buttons.append(self.buttonE12)
        self.buttons.append(self.buttonF1)
        self.buttons.append(self.buttonF2)
        self.buttons.append(self.buttonF3)
        self.buttons.append(self.buttonF4)
        self.buttons.append(self.buttonF5)
        self.buttons.append(self.buttonF6)
        self.buttons.append(self.buttonF7)
        self.buttons.append(self.buttonF8)
        self.buttons.append(self.buttonF9)
        self.buttons.append(self.buttonF10)
        self.buttons.append(self.buttonF11)
        self.buttons.append(self.buttonF12)
        self.buttons.append(self.buttonG1)
        self.buttons.append(self.buttonG2)
        self.buttons.append(self.buttonG3)
        self.buttons.append(self.buttonG4)
        self.buttons.append(self.buttonG5)
        self.buttons.append(self.buttonG6)
        self.buttons.append(self.buttonG7)
        self.buttons.append(self.buttonG8)
        self.buttons.append(self.buttonG9)
        self.buttons.append(self.buttonG10)
        self.buttons.append(self.buttonG11)
        self.buttons.append(self.buttonG12)
        self.buttons.append(self.buttonH1)
        self.buttons.append(self.buttonH2)
        self.buttons.append(self.buttonH3)
        self.buttons.append(self.buttonH4)
        self.buttons.append(self.buttonH5)
        self.buttons.append(self.buttonH6)
        self.buttons.append(self.buttonH7)
        self.buttons.append(self.buttonH8)
        self.buttons.append(self.buttonH9)
        self.buttons.append(self.buttonH10)
        self.buttons.append(self.buttonH11)
        self.buttons.append(self.buttonH12)
        self.buttons.append(self.buttonI1)
        self.buttons.append(self.buttonI2)
        self.buttons.append(self.buttonI3)
        self.buttons.append(self.buttonI4)
        self.buttons.append(self.buttonI5)
        self.buttons.append(self.buttonI6)
        self.buttons.append(self.buttonI7)
        self.buttons.append(self.buttonI8)
        self.buttons.append(self.buttonI9)
        self.buttons.append(self.buttonI10)
        self.buttons.append(self.buttonI11)
        self.buttons.append(self.buttonI12)
        self.buttons.append(self.buttonJ1)
        self.buttons.append(self.buttonJ2)
        self.buttons.append(self.buttonJ3)
        self.buttons.append(self.buttonJ4)
        self.buttons.append(self.buttonJ5)
        self.buttons.append(self.buttonJ6)
        self.buttons.append(self.buttonJ7)
        self.buttons.append(self.buttonJ8)
        self.buttons.append(self.buttonJ9)
        self.buttons.append(self.buttonJ10)
        self.buttons.append(self.buttonJ11)
        self.buttons.append(self.buttonJ12)
        self.buttons.append(self.buttonK1)
        self.buttons.append(self.buttonK2)
        self.buttons.append(self.buttonK3)
        self.buttons.append(self.buttonK4)
        self.buttons.append(self.buttonK5)
        self.buttons.append(self.buttonK6)
        self.buttons.append(self.buttonK7)
        self.buttons.append(self.buttonK8)
        self.buttons.append(self.buttonK9)
        self.buttons.append(self.buttonK10)
        self.buttons.append(self.buttonK11)
        self.buttons.append(self.buttonK12)
        self.buttons.append(self.buttonL1)
        self.buttons.append(self.buttonL2)
        self.buttons.append(self.buttonL3)
        self.buttons.append(self.buttonL4)
        self.buttons.append(self.buttonL5)
        self.buttons.append(self.buttonL6)
        self.buttons.append(self.buttonL7)
        self.buttons.append(self.buttonL8)
        self.buttons.append(self.buttonL9)
        self.buttons.append(self.buttonL10)
        self.buttons.append(self.buttonL11)
        self.buttons.append(self.buttonL12)

        self.mirror1Button['command'] = self.mirror1
        self.mirror2Button['command'] = self.mirror2
        self.mirror3Button['command'] = self.mirror3
        self.mirror4Button['command'] = self.mirror4
        self.lensXButton['command'] = self.lensX
        self.lensYButton['command'] = self.lensY
        self.blockButton['command'] = self.block

        self.buttonA1['command'] = self.clickA1
        self.buttonA2['command'] = self.clickA2
        self.buttonA3['command'] = self.clickA3
        self.buttonA4['command'] = self.clickA4
        self.buttonA5['command'] = self.clickA5
        self.buttonA6['command'] = self.clickA6
        self.buttonA7['command'] = self.clickA7
        self.buttonA8['command'] = self.clickA8
        self.buttonA9['command'] = self.clickA9
        self.buttonA10['command'] = self.clickA10
        self.buttonA11['command'] = self.clickA11
        self.buttonA12['command'] = self.clickA12
        self.buttonB1['command'] = self.clickB1
        self.buttonB2['command'] = self.clickB2
        self.buttonB3['command'] = self.clickB3
        self.buttonB4['command'] = self.clickB4
        self.buttonB5['command'] = self.clickB5
        self.buttonB6['command'] = self.clickB6
        self.buttonB7['command'] = self.clickB7
        self.buttonB8['command'] = self.clickB8
        self.buttonB9['command'] = self.clickB9
        self.buttonB10['command'] = self.clickB10
        self.buttonB11['command'] = self.clickB11
        self.buttonB12['command'] = self.clickB12
        self.buttonC1['command'] = self.clickC1
        self.buttonC2['command'] = self.clickC2
        self.buttonC3['command'] = self.clickC3
        self.buttonC4['command'] = self.clickC4
        self.buttonC5['command'] = self.clickC5
        self.buttonC6['command'] = self.clickC6
        self.buttonC7['command'] = self.clickC7
        self.buttonC8['command'] = self.clickC8
        self.buttonC9['command'] = self.clickC9
        self.buttonC10['command'] = self.clickC10
        self.buttonC11['command'] = self.clickC11
        self.buttonC12['command'] = self.clickC12
        self.buttonD1['command'] = self.clickD1
        self.buttonD2['command'] = self.clickD2
        self.buttonD3['command'] = self.clickD3
        self.buttonD4['command'] = self.clickD4
        self.buttonD5['command'] = self.clickD5
        self.buttonD6['command'] = self.clickD6
        self.buttonD7['command'] = self.clickD7
        self.buttonD8['command'] = self.clickD8
        self.buttonD9['command'] = self.clickD9
        self.buttonD10['command'] = self.clickD10
        self.buttonD11['command'] = self.clickD11
        self.buttonD12['command'] = self.clickD12
        self.buttonE1['command'] = self.clickE1
        self.buttonE2['command'] = self.clickE2
        self.buttonE3['command'] = self.clickE3
        self.buttonE4['command'] = self.clickE4
        self.buttonE5['command'] = self.clickE5
        self.buttonE6['command'] = self.clickE6
        self.buttonE7['command'] = self.clickE7
        self.buttonE8['command'] = self.clickE8
        self.buttonE9['command'] = self.clickE9
        self.buttonE10['command'] = self.clickE10
        self.buttonE11['command'] = self.clickE11
        self.buttonE12['command'] = self.clickE12
        self.buttonF1['command'] = self.clickF1
        self.buttonF2['command'] = self.clickF2
        self.buttonF3['command'] = self.clickF3
        self.buttonF4['command'] = self.clickF4
        self.buttonF5['command'] = self.clickF5
        self.buttonF6['command'] = self.clickF6
        self.buttonF7['command'] = self.clickF7
        self.buttonF8['command'] = self.clickF8
        self.buttonF9['command'] = self.clickF9
        self.buttonF10['command'] = self.clickF10
        self.buttonF11['command'] = self.clickF11
        self.buttonF12['command'] = self.clickF12
        self.buttonG1['command'] = self.clickG1
        self.buttonG2['command'] = self.clickG2
        self.buttonG3['command'] = self.clickG3
        self.buttonG4['command'] = self.clickG4
        self.buttonG5['command'] = self.clickG5
        self.buttonG6['command'] = self.clickG6
        self.buttonG7['command'] = self.clickG7
        self.buttonG8['command'] = self.clickG8
        self.buttonG9['command'] = self.clickG9
        self.buttonG10['command'] = self.clickG10
        self.buttonG11['command'] = self.clickG11
        self.buttonG12['command'] = self.clickG12
        self.buttonH1['command'] = self.clickH1
        self.buttonH2['command'] = self.clickH2
        self.buttonH3['command'] = self.clickH3
        self.buttonH4['command'] = self.clickH4
        self.buttonH5['command'] = self.clickH5
        self.buttonH6['command'] = self.clickH6
        self.buttonH7['command'] = self.clickH7
        self.buttonH8['command'] = self.clickH8
        self.buttonH9['command'] = self.clickH9
        self.buttonH10['command'] = self.clickH10
        self.buttonH11['command'] = self.clickH11
        self.buttonH12['command'] = self.clickH12
        self.buttonI1['command'] = self.clickI1
        self.buttonI2['command'] = self.clickI2
        self.buttonI3['command'] = self.clickI3
        self.buttonI4['command'] = self.clickI4
        self.buttonI5['command'] = self.clickI5
        self.buttonI6['command'] = self.clickI6
        self.buttonI7['command'] = self.clickI7
        self.buttonI8['command'] = self.clickI8
        self.buttonI9['command'] = self.clickI9
        self.buttonI10['command'] = self.clickI10
        self.buttonI11['command'] = self.clickI11
        self.buttonI12['command'] = self.clickI12
        self.buttonJ1['command'] = self.clickJ1
        self.buttonJ2['command'] = self.clickJ2
        self.buttonJ3['command'] = self.clickJ3
        self.buttonJ4['command'] = self.clickJ4
        self.buttonJ5['command'] = self.clickJ5
        self.buttonJ6['command'] = self.clickJ6
        self.buttonJ7['command'] = self.clickJ7
        self.buttonJ8['command'] = self.clickJ8
        self.buttonJ9['command'] = self.clickJ9
        self.buttonJ10['command'] = self.clickJ10
        self.buttonJ11['command'] = self.clickJ11
        self.buttonJ12['command'] = self.clickJ12
        self.buttonK1['command'] = self.clickK1
        self.buttonK2['command'] = self.clickK2
        self.buttonK3['command'] = self.clickK3
        self.buttonK4['command'] = self.clickK4
        self.buttonK5['command'] = self.clickK5
        self.buttonK6['command'] = self.clickK6
        self.buttonK7['command'] = self.clickK7
        self.buttonK8['command'] = self.clickK8
        self.buttonK9['command'] = self.clickK9
        self.buttonK10['command'] = self.clickK10
        self.buttonK11['command'] = self.clickK11
        self.buttonK12['command'] = self.clickK12
        self.buttonL1['command'] = self.clickL1
        self.buttonL2['command'] = self.clickL2
        self.buttonL3['command'] = self.clickL3
        self.buttonL4['command'] = self.clickL4
        self.buttonL5['command'] = self.clickL5
        self.buttonL6['command'] = self.clickL6
        self.buttonL7['command'] = self.clickL7
        self.buttonL8['command'] = self.clickL8
        self.buttonL9['command'] = self.clickL9
        self.buttonL10['command'] = self.clickL10
        self.buttonL11['command'] = self.clickL11
        self.buttonL12['command'] = self.clickL12



    def update_images(self, board):
        red = (4,3)
        redtile = (4,4)
        while redtile:
            rednext = board.tiles[ redtile[0]*12 + redtile[1] ].laser(red)
            red = redtile
            redtile = rednext
        blue = (7,3)
        bluetile = (7,4)
        while bluetile:
            bluenext = board.tiles[ bluetile[0]*12 + bluetile[1] ].laser(blue)
            blue = bluetile
            bluetile = bluenext
        for atile in range(144):
                self.buttons[atile]['image'] = images[board.tiles[atile].img]



    def mirror1(self):
        self.selected = 'm1'
    def mirror2(self):
        self.selected = 'm2'
    def mirror3(self):
        self.selected = 'm3'
    def mirror4(self):
        self.selected = 'm4'
    def lensX(self):
        self.selected = 'lensX'
    def lensY(self):
        self.selected = 'lensY'
    def block(self):
        self.selected = 'block'


    def clickA1(self):
        if self.selected == 'm1':
            board.tiles[0].mirror1()
        if self.selected == 'm2':
            board.tiles[0].mirror2()
        if self.selected == 'm3':
            board.tiles[0].mirror3()
        if self.selected == 'm4':
            board.tiles[0].mirror4()
        if self.selected == 'lensX':
            board.tiles[0].lensX()
        if self.selected == 'lensY':
            board.tiles[0].lensY()
        if self.selected == 'block':
            board.tiles[0].block()
        self.update_images(board)
    def clickA2(self):
        if self.selected == 'm1':
            board.tiles[1].mirror1()
        if self.selected == 'm2':
            board.tiles[1].mirror2()
        if self.selected == 'm3':
            board.tiles[1].mirror3()
        if self.selected == 'm4':
            board.tiles[1].mirror4()
        if self.selected == 'lensX':
            board.tiles[1].lensX()
        if self.selected == 'lensY':
            board.tiles[1].lensY()
        if self.selected == 'block':
            board.tiles[1].block()
        self.update_images(board)
    def clickA3(self):
        if self.selected == 'm1':
            board.tiles[2].mirror1()
        if self.selected == 'm2':
            board.tiles[2].mirror2()
        if self.selected == 'm3':
            board.tiles[2].mirror3()
        if self.selected == 'm4':
            board.tiles[2].mirror4()
        if self.selected == 'lensX':
            board.tiles[2].lensX()
        if self.selected == 'lensY':
            board.tiles[2].lensY()
        if self.selected == 'block':
            board.tiles[2].block()
        self.update_images(board)
    def clickA4(self):
        if self.selected == 'm1':
            board.tiles[3].mirror1()
        if self.selected == 'm2':
            board.tiles[3].mirror2()
        if self.selected == 'm3':
            board.tiles[3].mirror3()
        if self.selected == 'm4':
            board.tiles[3].mirror4()
        if self.selected == 'lensX':
            board.tiles[3].lensX()
        if self.selected == 'lensY':
            board.tiles[3].lensY()
        if self.selected == 'block':
            board.tiles[3].block()
        self.update_images(board)
    def clickA5(self):
        if self.selected == 'm1':
            board.tiles[4].mirror1()
        if self.selected == 'm2':
            board.tiles[4].mirror2()
        if self.selected == 'm3':
            board.tiles[4].mirror3()
        if self.selected == 'm4':
            board.tiles[4].mirror4()
        if self.selected == 'lensX':
            board.tiles[4].lensX()
        if self.selected == 'lensY':
            board.tiles[4].lensY()
        if self.selected == 'block':
            board.tiles[4].block()
        self.update_images(board)
    def clickA6(self):
        if self.selected == 'm1':
            board.tiles[5].mirror1()
        if self.selected == 'm2':
            board.tiles[5].mirror2()
        if self.selected == 'm3':
            board.tiles[5].mirror3()
        if self.selected == 'm4':
            board.tiles[5].mirror4()
        if self.selected == 'lensX':
            board.tiles[5].lensX()
        if self.selected == 'lensY':
            board.tiles[5].lensY()
        if self.selected == 'block':
            board.tiles[5].block()
        self.update_images(board)
    def clickA7(self):
        if self.selected == 'm1':
            board.tiles[6].mirror1()
        if self.selected == 'm2':
            board.tiles[6].mirror2()
        if self.selected == 'm3':
            board.tiles[6].mirror3()
        if self.selected == 'm4':
            board.tiles[6].mirror4()
        if self.selected == 'lensX':
            board.tiles[6].lensX()
        if self.selected == 'lensY':
            board.tiles[6].lensY()
        if self.selected == 'block':
            board.tiles[6].block()
        self.update_images(board)
    def clickA8(self):
        if self.selected == 'm1':
            board.tiles[7].mirror1()
        if self.selected == 'm2':
            board.tiles[7].mirror2()
        if self.selected == 'm3':
            board.tiles[7].mirror3()
        if self.selected == 'm4':
            board.tiles[7].mirror4()
        if self.selected == 'lensX':
            board.tiles[7].lensX()
        if self.selected == 'lensY':
            board.tiles[7].lensY()
        if self.selected == 'block':
            board.tiles[7].block()
        self.update_images(board)
    def clickA9(self):
        if self.selected == 'm1':
            board.tiles[8].mirror1()
        if self.selected == 'm2':
            board.tiles[8].mirror2()
        if self.selected == 'm3':
            board.tiles[8].mirror3()
        if self.selected == 'm4':
            board.tiles[8].mirror4()
        if self.selected == 'lensX':
            board.tiles[8].lensX()
        if self.selected == 'lensY':
            board.tiles[8].lensY()
        if self.selected == 'block':
            board.tiles[8].block()
        self.update_images(board)
    def clickA10(self):
        if self.selected == 'm1':
            board.tiles[9].mirror1()
        if self.selected == 'm2':
            board.tiles[9].mirror2()
        if self.selected == 'm3':
            board.tiles[9].mirror3()
        if self.selected == 'm4':
            board.tiles[9].mirror4()
        if self.selected == 'lensX':
            board.tiles[9].lensX()
        if self.selected == 'lensY':
            board.tiles[9].lensY()
        if self.selected == 'block':
            board.tiles[9].block()
        self.update_images(board)
    def clickA11(self):
        if self.selected == 'm1':
            board.tiles[10].mirror1()
        if self.selected == 'm2':
            board.tiles[10].mirror2()
        if self.selected == 'm3':
            board.tiles[10].mirror3()
        if self.selected == 'm4':
            board.tiles[10].mirror4()
        if self.selected == 'lensX':
            board.tiles[10].lensX()
        if self.selected == 'lensY':
            board.tiles[10].lensY()
        if self.selected == 'block':
            board.tiles[10].block()
        self.update_images(board)
    def clickA12(self):
        if self.selected == 'm1':
            board.tiles[11].mirror1()
        if self.selected == 'm2':
            board.tiles[11].mirror2()
        if self.selected == 'm3':
            board.tiles[11].mirror3()
        if self.selected == 'm4':
            board.tiles[11].mirror4()
        if self.selected == 'lensX':
            board.tiles[11].lensX()
        if self.selected == 'lensY':
            board.tiles[11].lensY()
        if self.selected == 'block':
            board.tiles[11].block()
        self.update_images(board)
    def clickB1(self):
        if self.selected == 'm1':
            board.tiles[12].mirror1()
        if self.selected == 'm2':
            board.tiles[12].mirror2()
        if self.selected == 'm3':
            board.tiles[12].mirror3()
        if self.selected == 'm4':
            board.tiles[12].mirror4()
        if self.selected == 'lensX':
            board.tiles[12].lensX()
        if self.selected == 'lensY':
            board.tiles[12].lensY()
        if self.selected == 'block':
            board.tiles[12].block()
        self.update_images(board)
    def clickB2(self):
        if self.selected == 'm1':
            board.tiles[13].mirror1()
        if self.selected == 'm2':
            board.tiles[13].mirror2()
        if self.selected == 'm3':
            board.tiles[13].mirror3()
        if self.selected == 'm4':
            board.tiles[13].mirror4()
        if self.selected == 'lensX':
            board.tiles[13].lensX()
        if self.selected == 'lensY':
            board.tiles[13].lensY()
        if self.selected == 'block':
            board.tiles[13].block()
        self.update_images(board)
    def clickB3(self):
        if self.selected == 'm1':
            board.tiles[14].mirror1()
        if self.selected == 'm2':
            board.tiles[14].mirror2()
        if self.selected == 'm3':
            board.tiles[14].mirror3()
        if self.selected == 'm4':
            board.tiles[14].mirror4()
        if self.selected == 'lensX':
            board.tiles[14].lensX()
        if self.selected == 'lensY':
            board.tiles[14].lensY()
        if self.selected == 'block':
            board.tiles[14].block()
        self.update_images(board)
    def clickB4(self):
        if self.selected == 'm1':
            board.tiles[15].mirror1()
        if self.selected == 'm2':
            board.tiles[15].mirror2()
        if self.selected == 'm3':
            board.tiles[15].mirror3()
        if self.selected == 'm4':
            board.tiles[15].mirror4()
        if self.selected == 'lensX':
            board.tiles[15].lensX()
        if self.selected == 'lensY':
            board.tiles[15].lensY()
        if self.selected == 'block':
            board.tiles[15].block()
        self.update_images(board)
    def clickB5(self):
        if self.selected == 'm1':
            board.tiles[16].mirror1()
        if self.selected == 'm2':
            board.tiles[16].mirror2()
        if self.selected == 'm3':
            board.tiles[16].mirror3()
        if self.selected == 'm4':
            board.tiles[16].mirror4()
        if self.selected == 'lensX':
            board.tiles[16].lensX()
        if self.selected == 'lensY':
            board.tiles[16].lensY()
        if self.selected == 'block':
            board.tiles[16].block()
        self.update_images(board)
    def clickB6(self):
        if self.selected == 'm1':
            board.tiles[17].mirror1()
        if self.selected == 'm2':
            board.tiles[17].mirror2()
        if self.selected == 'm3':
            board.tiles[17].mirror3()
        if self.selected == 'm4':
            board.tiles[17].mirror4()
        if self.selected == 'lensX':
            board.tiles[17].lensX()
        if self.selected == 'lensY':
            board.tiles[17].lensY()
        if self.selected == 'block':
            board.tiles[17].block()
        self.update_images(board)
    def clickB7(self):
        if self.selected == 'm1':
            board.tiles[18].mirror1()
        if self.selected == 'm2':
            board.tiles[18].mirror2()
        if self.selected == 'm3':
            board.tiles[18].mirror3()
        if self.selected == 'm4':
            board.tiles[18].mirror4()
        if self.selected == 'lensX':
            board.tiles[18].lensX()
        if self.selected == 'lensY':
            board.tiles[18].lensY()
        if self.selected == 'block':
            board.tiles[18].block()
        self.update_images(board)
    def clickB8(self):
        if self.selected == 'm1':
            board.tiles[19].mirror1()
        if self.selected == 'm2':
            board.tiles[19].mirror2()
        if self.selected == 'm3':
            board.tiles[19].mirror3()
        if self.selected == 'm4':
            board.tiles[19].mirror4()
        if self.selected == 'lensX':
            board.tiles[19].lensX()
        if self.selected == 'lensY':
            board.tiles[19].lensY()
        if self.selected == 'block':
            board.tiles[19].block()
        self.update_images(board)
    def clickB9(self):
        if self.selected == 'm1':
            board.tiles[20].mirror1()
        if self.selected == 'm2':
            board.tiles[20].mirror2()
        if self.selected == 'm3':
            board.tiles[20].mirror3()
        if self.selected == 'm4':
            board.tiles[20].mirror4()
        if self.selected == 'lensX':
            board.tiles[20].lensX()
        if self.selected == 'lensY':
            board.tiles[20].lensY()
        if self.selected == 'block':
            board.tiles[20].block()
        self.update_images(board)
    def clickB10(self):
        if self.selected == 'm1':
            board.tiles[21].mirror1()
        if self.selected == 'm2':
            board.tiles[21].mirror2()
        if self.selected == 'm3':
            board.tiles[21].mirror3()
        if self.selected == 'm4':
            board.tiles[21].mirror4()
        if self.selected == 'lensX':
            board.tiles[21].lensX()
        if self.selected == 'lensY':
            board.tiles[21].lensY()
        if self.selected == 'block':
            board.tiles[21].block()
        self.update_images(board)
    def clickB11(self):
        if self.selected == 'm1':
            board.tiles[22].mirror1()
        if self.selected == 'm2':
            board.tiles[22].mirror2()
        if self.selected == 'm3':
            board.tiles[22].mirror3()
        if self.selected == 'm4':
            board.tiles[22].mirror4()
        if self.selected == 'lensX':
            board.tiles[22].lensX()
        if self.selected == 'lensY':
            board.tiles[22].lensY()
        if self.selected == 'block':
            board.tiles[22].block()
        self.update_images(board)
    def clickB12(self):
        if self.selected == 'm1':
            board.tiles[23].mirror1()
        if self.selected == 'm2':
            board.tiles[23].mirror2()
        if self.selected == 'm3':
            board.tiles[23].mirror3()
        if self.selected == 'm4':
            board.tiles[23].mirror4()
        if self.selected == 'lensX':
            board.tiles[23].lensX()
        if self.selected == 'lensY':
            board.tiles[23].lensY()
        if self.selected == 'block':
            board.tiles[23].block()
        self.update_images(board)
    def clickC1(self):
        if self.selected == 'm1':
            board.tiles[24].mirror1()
        if self.selected == 'm2':
            board.tiles[24].mirror2()
        if self.selected == 'm3':
            board.tiles[24].mirror3()
        if self.selected == 'm4':
            board.tiles[24].mirror4()
        if self.selected == 'lensX':
            board.tiles[24].lensX()
        if self.selected == 'lensY':
            board.tiles[24].lensY()
        if self.selected == 'block':
            board.tiles[24].block()
        self.update_images(board)
    def clickC2(self):
        if self.selected == 'm1':
            board.tiles[25].mirror1()
        if self.selected == 'm2':
            board.tiles[25].mirror2()
        if self.selected == 'm3':
            board.tiles[25].mirror3()
        if self.selected == 'm4':
            board.tiles[25].mirror4()
        if self.selected == 'lensX':
            board.tiles[25].lensX()
        if self.selected == 'lensY':
            board.tiles[25].lensY()
        if self.selected == 'block':
            board.tiles[25].block()
        self.update_images(board)
    def clickC3(self):
        if self.selected == 'm1':
            board.tiles[26].mirror1()
        if self.selected == 'm2':
            board.tiles[26].mirror2()
        if self.selected == 'm3':
            board.tiles[26].mirror3()
        if self.selected == 'm4':
            board.tiles[26].mirror4()
        if self.selected == 'lensX':
            board.tiles[26].lensX()
        if self.selected == 'lensY':
            board.tiles[26].lensY()
        if self.selected == 'block':
            board.tiles[26].block()
        self.update_images(board)
    def clickC4(self):
        if self.selected == 'm1':
            board.tiles[27].mirror1()
        if self.selected == 'm2':
            board.tiles[27].mirror2()
        if self.selected == 'm3':
            board.tiles[27].mirror3()
        if self.selected == 'm4':
            board.tiles[27].mirror4()
        if self.selected == 'lensX':
            board.tiles[27].lensX()
        if self.selected == 'lensY':
            board.tiles[27].lensY()
        if self.selected == 'block':
            board.tiles[27].block()
        self.update_images(board)
    def clickC5(self):
        if self.selected == 'm1':
            board.tiles[28].mirror1()
        if self.selected == 'm2':
            board.tiles[28].mirror2()
        if self.selected == 'm3':
            board.tiles[28].mirror3()
        if self.selected == 'm4':
            board.tiles[28].mirror4()
        if self.selected == 'lensX':
            board.tiles[28].lensX()
        if self.selected == 'lensY':
            board.tiles[28].lensY()
        if self.selected == 'block':
            board.tiles[28].block()
        self.update_images(board)
    def clickC6(self):
        if self.selected == 'm1':
            board.tiles[29].mirror1()
        if self.selected == 'm2':
            board.tiles[29].mirror2()
        if self.selected == 'm3':
            board.tiles[29].mirror3()
        if self.selected == 'm4':
            board.tiles[29].mirror4()
        if self.selected == 'lensX':
            board.tiles[29].lensX()
        if self.selected == 'lensY':
            board.tiles[29].lensY()
        if self.selected == 'block':
            board.tiles[29].block()
        self.update_images(board)
    def clickC7(self):
        if self.selected == 'm1':
            board.tiles[30].mirror1()
        if self.selected == 'm2':
            board.tiles[30].mirror2()
        if self.selected == 'm3':
            board.tiles[30].mirror3()
        if self.selected == 'm4':
            board.tiles[30].mirror4()
        if self.selected == 'lensX':
            board.tiles[30].lensX()
        if self.selected == 'lensY':
            board.tiles[30].lensY()
        if self.selected == 'block':
            board.tiles[30].block()
        self.update_images(board)
    def clickC8(self):
        if self.selected == 'm1':
            board.tiles[31].mirror1()
        if self.selected == 'm2':
            board.tiles[31].mirror2()
        if self.selected == 'm3':
            board.tiles[31].mirror3()
        if self.selected == 'm4':
            board.tiles[31].mirror4()
        if self.selected == 'lensX':
            board.tiles[31].lensX()
        if self.selected == 'lensY':
            board.tiles[31].lensY()
        if self.selected == 'block':
            board.tiles[31].block()
        self.update_images(board)
    def clickC9(self):
        if self.selected == 'm1':
            board.tiles[32].mirror1()
        if self.selected == 'm2':
            board.tiles[32].mirror2()
        if self.selected == 'm3':
            board.tiles[32].mirror3()
        if self.selected == 'm4':
            board.tiles[32].mirror4()
        if self.selected == 'lensX':
            board.tiles[32].lensX()
        if self.selected == 'lensY':
            board.tiles[32].lensY()
        if self.selected == 'block':
            board.tiles[32].block()
        self.update_images(board)
    def clickC10(self):
        if self.selected == 'm1':
            board.tiles[33].mirror1()
        if self.selected == 'm2':
            board.tiles[33].mirror2()
        if self.selected == 'm3':
            board.tiles[33].mirror3()
        if self.selected == 'm4':
            board.tiles[33].mirror4()
        if self.selected == 'lensX':
            board.tiles[33].lensX()
        if self.selected == 'lensY':
            board.tiles[33].lensY()
        if self.selected == 'block':
            board.tiles[33].block()
        self.update_images(board)
    def clickC11(self):
        if self.selected == 'm1':
            board.tiles[34].mirror1()
        if self.selected == 'm2':
            board.tiles[34].mirror2()
        if self.selected == 'm3':
            board.tiles[34].mirror3()
        if self.selected == 'm4':
            board.tiles[34].mirror4()
        if self.selected == 'lensX':
            board.tiles[34].lensX()
        if self.selected == 'lensY':
            board.tiles[34].lensY()
        if self.selected == 'block':
            board.tiles[34].block()
        self.update_images(board)
    def clickC12(self):
        if self.selected == 'm1':
            board.tiles[35].mirror1()
        if self.selected == 'm2':
            board.tiles[35].mirror2()
        if self.selected == 'm3':
            board.tiles[35].mirror3()
        if self.selected == 'm4':
            board.tiles[35].mirror4()
        if self.selected == 'lensX':
            board.tiles[35].lensX()
        if self.selected == 'lensY':
            board.tiles[35].lensY()
        if self.selected == 'block':
            board.tiles[35].block()
        self.update_images(board)
    def clickD1(self):
        if self.selected == 'm1':
            board.tiles[36].mirror1()
        if self.selected == 'm2':
            board.tiles[36].mirror2()
        if self.selected == 'm3':
            board.tiles[36].mirror3()
        if self.selected == 'm4':
            board.tiles[36].mirror4()
        if self.selected == 'lensX':
            board.tiles[36].lensX()
        if self.selected == 'lensY':
            board.tiles[36].lensY()
        if self.selected == 'block':
            board.tiles[36].block()
        self.update_images(board)
    def clickD2(self):
        if self.selected == 'm1':
            board.tiles[37].mirror1()
        if self.selected == 'm2':
            board.tiles[37].mirror2()
        if self.selected == 'm3':
            board.tiles[37].mirror3()
        if self.selected == 'm4':
            board.tiles[37].mirror4()
        if self.selected == 'lensX':
            board.tiles[37].lensX()
        if self.selected == 'lensY':
            board.tiles[37].lensY()
        if self.selected == 'block':
            board.tiles[37].block()
        self.update_images(board)
    def clickD3(self):
        if self.selected == 'm1':
            board.tiles[38].mirror1()
        if self.selected == 'm2':
            board.tiles[38].mirror2()
        if self.selected == 'm3':
            board.tiles[38].mirror3()
        if self.selected == 'm4':
            board.tiles[38].mirror4()
        if self.selected == 'lensX':
            board.tiles[38].lensX()
        if self.selected == 'lensY':
            board.tiles[38].lensY()
        if self.selected == 'block':
            board.tiles[38].block()
        self.update_images(board)
    def clickD4(self):
        if self.selected == 'm1':
            board.tiles[39].mirror1()
        if self.selected == 'm2':
            board.tiles[39].mirror2()
        if self.selected == 'm3':
            board.tiles[39].mirror3()
        if self.selected == 'm4':
            board.tiles[39].mirror4()
        if self.selected == 'lensX':
            board.tiles[39].lensX()
        if self.selected == 'lensY':
            board.tiles[39].lensY()
        if self.selected == 'block':
            board.tiles[39].block()
        self.update_images(board)
    def clickD5(self):
        if self.selected == 'm1':
            board.tiles[40].mirror1()
        if self.selected == 'm2':
            board.tiles[40].mirror2()
        if self.selected == 'm3':
            board.tiles[40].mirror3()
        if self.selected == 'm4':
            board.tiles[40].mirror4()
        if self.selected == 'lensX':
            board.tiles[40].lensX()
        if self.selected == 'lensY':
            board.tiles[40].lensY()
        if self.selected == 'block':
            board.tiles[40].block()
        self.update_images(board)
    def clickD6(self):
        if self.selected == 'm1':
            board.tiles[41].mirror1()
        if self.selected == 'm2':
            board.tiles[41].mirror2()
        if self.selected == 'm3':
            board.tiles[41].mirror3()
        if self.selected == 'm4':
            board.tiles[41].mirror4()
        if self.selected == 'lensX':
            board.tiles[41].lensX()
        if self.selected == 'lensY':
            board.tiles[41].lensY()
        if self.selected == 'block':
            board.tiles[41].block()
        self.update_images(board)
    def clickD7(self):
        if self.selected == 'm1':
            board.tiles[42].mirror1()
        if self.selected == 'm2':
            board.tiles[42].mirror2()
        if self.selected == 'm3':
            board.tiles[42].mirror3()
        if self.selected == 'm4':
            board.tiles[42].mirror4()
        if self.selected == 'lensX':
            board.tiles[42].lensX()
        if self.selected == 'lensY':
            board.tiles[42].lensY()
        if self.selected == 'block':
            board.tiles[42].block()
        self.update_images(board)
    def clickD8(self):
        if self.selected == 'm1':
            board.tiles[43].mirror1()
        if self.selected == 'm2':
            board.tiles[43].mirror2()
        if self.selected == 'm3':
            board.tiles[43].mirror3()
        if self.selected == 'm4':
            board.tiles[43].mirror4()
        if self.selected == 'lensX':
            board.tiles[43].lensX()
        if self.selected == 'lensY':
            board.tiles[43].lensY()
        if self.selected == 'block':
            board.tiles[43].block()
        self.update_images(board)
    def clickD9(self):
        if self.selected == 'm1':
            board.tiles[44].mirror1()
        if self.selected == 'm2':
            board.tiles[44].mirror2()
        if self.selected == 'm3':
            board.tiles[44].mirror3()
        if self.selected == 'm4':
            board.tiles[44].mirror4()
        if self.selected == 'lensX':
            board.tiles[44].lensX()
        if self.selected == 'lensY':
            board.tiles[44].lensY()
        if self.selected == 'block':
            board.tiles[44].block()
        self.update_images(board)
    def clickD10(self):
        if self.selected == 'm1':
            board.tiles[45].mirror1()
        if self.selected == 'm2':
            board.tiles[45].mirror2()
        if self.selected == 'm3':
            board.tiles[45].mirror3()
        if self.selected == 'm4':
            board.tiles[45].mirror4()
        if self.selected == 'lensX':
            board.tiles[45].lensX()
        if self.selected == 'lensY':
            board.tiles[45].lensY()
        if self.selected == 'block':
            board.tiles[45].block()
        self.update_images(board)
    def clickD11(self):
        if self.selected == 'm1':
            board.tiles[46].mirror1()
        if self.selected == 'm2':
            board.tiles[46].mirror2()
        if self.selected == 'm3':
            board.tiles[46].mirror3()
        if self.selected == 'm4':
            board.tiles[46].mirror4()
        if self.selected == 'lensX':
            board.tiles[46].lensX()
        if self.selected == 'lensY':
            board.tiles[46].lensY()
        if self.selected == 'block':
            board.tiles[46].block()
        self.update_images(board)
    def clickD12(self):
        if self.selected == 'm1':
            board.tiles[47].mirror1()
        if self.selected == 'm2':
            board.tiles[47].mirror2()
        if self.selected == 'm3':
            board.tiles[47].mirror3()
        if self.selected == 'm4':
            board.tiles[47].mirror4()
        if self.selected == 'lensX':
            board.tiles[47].lensX()
        if self.selected == 'lensY':
            board.tiles[47].lensY()
        if self.selected == 'block':
            board.tiles[47].block()
        self.update_images(board)
    def clickE1(self):
        if self.selected == 'm1':
            board.tiles[48].mirror1()
        if self.selected == 'm2':
            board.tiles[48].mirror2()
        if self.selected == 'm3':
            board.tiles[48].mirror3()
        if self.selected == 'm4':
            board.tiles[48].mirror4()
        if self.selected == 'lensX':
            board.tiles[48].lensX()
        if self.selected == 'lensY':
            board.tiles[48].lensY()
        if self.selected == 'block':
            board.tiles[48].block()
        self.update_images(board)
    def clickE2(self):
        if self.selected == 'm1':
            board.tiles[49].mirror1()
        if self.selected == 'm2':
            board.tiles[49].mirror2()
        if self.selected == 'm3':
            board.tiles[49].mirror3()
        if self.selected == 'm4':
            board.tiles[49].mirror4()
        if self.selected == 'lensX':
            board.tiles[49].lensX()
        if self.selected == 'lensY':
            board.tiles[49].lensY()
        if self.selected == 'block':
            board.tiles[49].block()
        self.update_images(board)
    def clickE3(self):
        if self.selected == 'm1':
            board.tiles[50].mirror1()
        if self.selected == 'm2':
            board.tiles[50].mirror2()
        if self.selected == 'm3':
            board.tiles[50].mirror3()
        if self.selected == 'm4':
            board.tiles[50].mirror4()
        if self.selected == 'lensX':
            board.tiles[50].lensX()
        if self.selected == 'lensY':
            board.tiles[50].lensY()
        if self.selected == 'block':
            board.tiles[50].block()
        self.update_images(board)
    def clickE4(self):
        if self.selected == 'm1':
            board.tiles[51].mirror1()
        if self.selected == 'm2':
            board.tiles[51].mirror2()
        if self.selected == 'm3':
            board.tiles[51].mirror3()
        if self.selected == 'm4':
            board.tiles[51].mirror4()
        if self.selected == 'lensX':
            board.tiles[51].lensX()
        if self.selected == 'lensY':
            board.tiles[51].lensY()
        if self.selected == 'block':
            board.tiles[51].block()
        self.update_images(board)
    def clickE5(self):
        if self.selected == 'm1':
            board.tiles[52].mirror1()
        if self.selected == 'm2':
            board.tiles[52].mirror2()
        if self.selected == 'm3':
            board.tiles[52].mirror3()
        if self.selected == 'm4':
            board.tiles[52].mirror4()
        if self.selected == 'lensX':
            board.tiles[52].lensX()
        if self.selected == 'lensY':
            board.tiles[52].lensY()
        if self.selected == 'block':
            board.tiles[52].block()
        self.update_images(board)
    def clickE6(self):
        if self.selected == 'm1':
            board.tiles[53].mirror1()
        if self.selected == 'm2':
            board.tiles[53].mirror2()
        if self.selected == 'm3':
            board.tiles[53].mirror3()
        if self.selected == 'm4':
            board.tiles[53].mirror4()
        if self.selected == 'lensX':
            board.tiles[53].lensX()
        if self.selected == 'lensY':
            board.tiles[53].lensY()
        if self.selected == 'block':
            board.tiles[53].block()
        self.update_images(board)
    def clickE7(self):
        if self.selected == 'm1':
            board.tiles[54].mirror1()
        if self.selected == 'm2':
            board.tiles[54].mirror2()
        if self.selected == 'm3':
            board.tiles[54].mirror3()
        if self.selected == 'm4':
            board.tiles[54].mirror4()
        if self.selected == 'lensX':
            board.tiles[54].lensX()
        if self.selected == 'lensY':
            board.tiles[54].lensY()
        if self.selected == 'block':
            board.tiles[54].block()
        self.update_images(board)
    def clickE8(self):
        if self.selected == 'm1':
            board.tiles[55].mirror1()
        if self.selected == 'm2':
            board.tiles[55].mirror2()
        if self.selected == 'm3':
            board.tiles[55].mirror3()
        if self.selected == 'm4':
            board.tiles[55].mirror4()
        if self.selected == 'lensX':
            board.tiles[55].lensX()
        if self.selected == 'lensY':
            board.tiles[55].lensY()
        if self.selected == 'block':
            board.tiles[55].block()
        self.update_images(board)
    def clickE9(self):
        if self.selected == 'm1':
            board.tiles[56].mirror1()
        if self.selected == 'm2':
            board.tiles[56].mirror2()
        if self.selected == 'm3':
            board.tiles[56].mirror3()
        if self.selected == 'm4':
            board.tiles[56].mirror4()
        if self.selected == 'lensX':
            board.tiles[56].lensX()
        if self.selected == 'lensY':
            board.tiles[56].lensY()
        if self.selected == 'block':
            board.tiles[56].block()
        self.update_images(board)
    def clickE10(self):
        if self.selected == 'm1':
            board.tiles[57].mirror1()
        if self.selected == 'm2':
            board.tiles[57].mirror2()
        if self.selected == 'm3':
            board.tiles[57].mirror3()
        if self.selected == 'm4':
            board.tiles[57].mirror4()
        if self.selected == 'lensX':
            board.tiles[57].lensX()
        if self.selected == 'lensY':
            board.tiles[57].lensY()
        if self.selected == 'block':
            board.tiles[57].block()
        self.update_images(board)
    def clickE11(self):
        if self.selected == 'm1':
            board.tiles[58].mirror1()
        if self.selected == 'm2':
            board.tiles[58].mirror2()
        if self.selected == 'm3':
            board.tiles[58].mirror3()
        if self.selected == 'm4':
            board.tiles[58].mirror4()
        if self.selected == 'lensX':
            board.tiles[58].lensX()
        if self.selected == 'lensY':
            board.tiles[58].lensY()
        if self.selected == 'block':
            board.tiles[58].block()
        self.update_images(board)
    def clickE12(self):
        if self.selected == 'm1':
            board.tiles[59].mirror1()
        if self.selected == 'm2':
            board.tiles[59].mirror2()
        if self.selected == 'm3':
            board.tiles[59].mirror3()
        if self.selected == 'm4':
            board.tiles[59].mirror4()
        if self.selected == 'lensX':
            board.tiles[59].lensX()
        if self.selected == 'lensY':
            board.tiles[59].lensY()
        if self.selected == 'block':
            board.tiles[59].block()
        self.update_images(board)
    def clickF1(self):
        if self.selected == 'm1':
            board.tiles[60].mirror1()
        if self.selected == 'm2':
            board.tiles[60].mirror2()
        if self.selected == 'm3':
            board.tiles[60].mirror3()
        if self.selected == 'm4':
            board.tiles[60].mirror4()
        if self.selected == 'lensX':
            board.tiles[60].lensX()
        if self.selected == 'lensY':
            board.tiles[60].lensY()
        if self.selected == 'block':
            board.tiles[60].block()
        self.update_images(board)
    def clickF2(self):
        if self.selected == 'm1':
            board.tiles[61].mirror1()
        if self.selected == 'm2':
            board.tiles[61].mirror2()
        if self.selected == 'm3':
            board.tiles[61].mirror3()
        if self.selected == 'm4':
            board.tiles[61].mirror4()
        if self.selected == 'lensX':
            board.tiles[61].lensX()
        if self.selected == 'lensY':
            board.tiles[61].lensY()
        if self.selected == 'block':
            board.tiles[61].block()
        self.update_images(board)
    def clickF3(self):
        if self.selected == 'm1':
            board.tiles[62].mirror1()
        if self.selected == 'm2':
            board.tiles[62].mirror2()
        if self.selected == 'm3':
            board.tiles[62].mirror3()
        if self.selected == 'm4':
            board.tiles[62].mirror4()
        if self.selected == 'lensX':
            board.tiles[62].lensX()
        if self.selected == 'lensY':
            board.tiles[62].lensY()
        if self.selected == 'block':
            board.tiles[62].block()
        self.update_images(board)
    def clickF4(self):
        if self.selected == 'm1':
            board.tiles[63].mirror1()
        if self.selected == 'm2':
            board.tiles[63].mirror2()
        if self.selected == 'm3':
            board.tiles[63].mirror3()
        if self.selected == 'm4':
            board.tiles[63].mirror4()
        if self.selected == 'lensX':
            board.tiles[63].lensX()
        if self.selected == 'lensY':
            board.tiles[63].lensY()
        if self.selected == 'block':
            board.tiles[63].block()
        self.update_images(board)
    def clickF5(self):
        if self.selected == 'm1':
            board.tiles[64].mirror1()
        if self.selected == 'm2':
            board.tiles[64].mirror2()
        if self.selected == 'm3':
            board.tiles[64].mirror3()
        if self.selected == 'm4':
            board.tiles[64].mirror4()
        if self.selected == 'lensX':
            board.tiles[64].lensX()
        if self.selected == 'lensY':
            board.tiles[64].lensY()
        if self.selected == 'block':
            board.tiles[64].block()
        self.update_images(board)
    def clickF6(self):
        if self.selected == 'm1':
            board.tiles[65].mirror1()
        if self.selected == 'm2':
            board.tiles[65].mirror2()
        if self.selected == 'm3':
            board.tiles[65].mirror3()
        if self.selected == 'm4':
            board.tiles[65].mirror4()
        if self.selected == 'lensX':
            board.tiles[65].lensX()
        if self.selected == 'lensY':
            board.tiles[65].lensY()
        if self.selected == 'block':
            board.tiles[65].block()
        self.update_images(board)
    def clickF7(self):
        if self.selected == 'm1':
            board.tiles[66].mirror1()
        if self.selected == 'm2':
            board.tiles[66].mirror2()
        if self.selected == 'm3':
            board.tiles[66].mirror3()
        if self.selected == 'm4':
            board.tiles[66].mirror4()
        if self.selected == 'lensX':
            board.tiles[66].lensX()
        if self.selected == 'lensY':
            board.tiles[66].lensY()
        if self.selected == 'block':
            board.tiles[66].block()
        self.update_images(board)
    def clickF8(self):
        if self.selected == 'm1':
            board.tiles[67].mirror1()
        if self.selected == 'm2':
            board.tiles[67].mirror2()
        if self.selected == 'm3':
            board.tiles[67].mirror3()
        if self.selected == 'm4':
            board.tiles[67].mirror4()
        if self.selected == 'lensX':
            board.tiles[67].lensX()
        if self.selected == 'lensY':
            board.tiles[67].lensY()
        if self.selected == 'block':
            board.tiles[67].block()
        self.update_images(board)
    def clickF9(self):
        if self.selected == 'm1':
            board.tiles[68].mirror1()
        if self.selected == 'm2':
            board.tiles[68].mirror2()
        if self.selected == 'm3':
            board.tiles[68].mirror3()
        if self.selected == 'm4':
            board.tiles[68].mirror4()
        if self.selected == 'lensX':
            board.tiles[68].lensX()
        if self.selected == 'lensY':
            board.tiles[68].lensY()
        if self.selected == 'block':
            board.tiles[68].block()
        self.update_images(board)
    def clickF10(self):
        if self.selected == 'm1':
            board.tiles[69].mirror1()
        if self.selected == 'm2':
            board.tiles[69].mirror2()
        if self.selected == 'm3':
            board.tiles[69].mirror3()
        if self.selected == 'm4':
            board.tiles[69].mirror4()
        if self.selected == 'lensX':
            board.tiles[69].lensX()
        if self.selected == 'lensY':
            board.tiles[69].lensY()
        if self.selected == 'block':
            board.tiles[69].block()
        self.update_images(board)
    def clickF11(self):
        if self.selected == 'm1':
            board.tiles[70].mirror1()
        if self.selected == 'm2':
            board.tiles[70].mirror2()
        if self.selected == 'm3':
            board.tiles[70].mirror3()
        if self.selected == 'm4':
            board.tiles[70].mirror4()
        if self.selected == 'lensX':
            board.tiles[70].lensX()
        if self.selected == 'lensY':
            board.tiles[70].lensY()
        if self.selected == 'block':
            board.tiles[70].block()
        self.update_images(board)
    def clickF12(self):
        if self.selected == 'm1':
            board.tiles[71].mirror1()
        if self.selected == 'm2':
            board.tiles[71].mirror2()
        if self.selected == 'm3':
            board.tiles[71].mirror3()
        if self.selected == 'm4':
            board.tiles[71].mirror4()
        if self.selected == 'lensX':
            board.tiles[71].lensX()
        if self.selected == 'lensY':
            board.tiles[71].lensY()
        if self.selected == 'block':
            board.tiles[71].block()
        self.update_images(board)
    def clickG1(self):
        if self.selected == 'm1':
            board.tiles[72].mirror1()
        if self.selected == 'm2':
            board.tiles[72].mirror2()
        if self.selected == 'm3':
            board.tiles[72].mirror3()
        if self.selected == 'm4':
            board.tiles[72].mirror4()
        if self.selected == 'lensX':
            board.tiles[72].lensX()
        if self.selected == 'lensY':
            board.tiles[72].lensY()
        if self.selected == 'block':
            board.tiles[72].block()
        self.update_images(board)
    def clickG2(self):
        if self.selected == 'm1':
            board.tiles[73].mirror1()
        if self.selected == 'm2':
            board.tiles[73].mirror2()
        if self.selected == 'm3':
            board.tiles[73].mirror3()
        if self.selected == 'm4':
            board.tiles[73].mirror4()
        if self.selected == 'lensX':
            board.tiles[73].lensX()
        if self.selected == 'lensY':
            board.tiles[73].lensY()
        if self.selected == 'block':
            board.tiles[73].block()
        self.update_images(board)
    def clickG3(self):
        if self.selected == 'm1':
            board.tiles[74].mirror1()
        if self.selected == 'm2':
            board.tiles[74].mirror2()
        if self.selected == 'm3':
            board.tiles[74].mirror3()
        if self.selected == 'm4':
            board.tiles[74].mirror4()
        if self.selected == 'lensX':
            board.tiles[74].lensX()
        if self.selected == 'lensY':
            board.tiles[74].lensY()
        if self.selected == 'block':
            board.tiles[74].block()
        self.update_images(board)
    def clickG4(self):
        if self.selected == 'm1':
            board.tiles[75].mirror1()
        if self.selected == 'm2':
            board.tiles[75].mirror2()
        if self.selected == 'm3':
            board.tiles[75].mirror3()
        if self.selected == 'm4':
            board.tiles[75].mirror4()
        if self.selected == 'lensX':
            board.tiles[75].lensX()
        if self.selected == 'lensY':
            board.tiles[75].lensY()
        if self.selected == 'block':
            board.tiles[75].block()
        self.update_images(board)
    def clickG5(self):
        if self.selected == 'm1':
            board.tiles[76].mirror1()
        if self.selected == 'm2':
            board.tiles[76].mirror2()
        if self.selected == 'm3':
            board.tiles[76].mirror3()
        if self.selected == 'm4':
            board.tiles[76].mirror4()
        if self.selected == 'lensX':
            board.tiles[76].lensX()
        if self.selected == 'lensY':
            board.tiles[76].lensY()
        if self.selected == 'block':
            board.tiles[76].block()
        self.update_images(board)
    def clickG6(self):
        if self.selected == 'm1':
            board.tiles[77].mirror1()
        if self.selected == 'm2':
            board.tiles[77].mirror2()
        if self.selected == 'm3':
            board.tiles[77].mirror3()
        if self.selected == 'm4':
            board.tiles[77].mirror4()
        if self.selected == 'lensX':
            board.tiles[77].lensX()
        if self.selected == 'lensY':
            board.tiles[77].lensY()
        if self.selected == 'block':
            board.tiles[77].block()
        self.update_images(board)
    def clickG7(self):
        if self.selected == 'm1':
            board.tiles[78].mirror1()
        if self.selected == 'm2':
            board.tiles[78].mirror2()
        if self.selected == 'm3':
            board.tiles[78].mirror3()
        if self.selected == 'm4':
            board.tiles[78].mirror4()
        if self.selected == 'lensX':
            board.tiles[78].lensX()
        if self.selected == 'lensY':
            board.tiles[78].lensY()
        if self.selected == 'block':
            board.tiles[78].block()
        self.update_images(board)
    def clickG8(self):
        if self.selected == 'm1':
            board.tiles[79].mirror1()
        if self.selected == 'm2':
            board.tiles[79].mirror2()
        if self.selected == 'm3':
            board.tiles[79].mirror3()
        if self.selected == 'm4':
            board.tiles[79].mirror4()
        if self.selected == 'lensX':
            board.tiles[79].lensX()
        if self.selected == 'lensY':
            board.tiles[79].lensY()
        if self.selected == 'block':
            board.tiles[79].block()
        self.update_images(board)
    def clickG9(self):
        if self.selected == 'm1':
            board.tiles[80].mirror1()
        if self.selected == 'm2':
            board.tiles[80].mirror2()
        if self.selected == 'm3':
            board.tiles[80].mirror3()
        if self.selected == 'm4':
            board.tiles[80].mirror4()
        if self.selected == 'lensX':
            board.tiles[80].lensX()
        if self.selected == 'lensY':
            board.tiles[80].lensY()
        if self.selected == 'block':
            board.tiles[80].block()
        self.update_images(board)
    def clickG10(self):
        if self.selected == 'm1':
            board.tiles[81].mirror1()
        if self.selected == 'm2':
            board.tiles[81].mirror2()
        if self.selected == 'm3':
            board.tiles[81].mirror3()
        if self.selected == 'm4':
            board.tiles[81].mirror4()
        if self.selected == 'lensX':
            board.tiles[81].lensX()
        if self.selected == 'lensY':
            board.tiles[81].lensY()
        if self.selected == 'block':
            board.tiles[81].block()
        self.update_images(board)
    def clickG11(self):
        if self.selected == 'm1':
            board.tiles[82].mirror1()
        if self.selected == 'm2':
            board.tiles[82].mirror2()
        if self.selected == 'm3':
            board.tiles[82].mirror3()
        if self.selected == 'm4':
            board.tiles[82].mirror4()
        if self.selected == 'lensX':
            board.tiles[82].lensX()
        if self.selected == 'lensY':
            board.tiles[82].lensY()
        if self.selected == 'block':
            board.tiles[82].block()
        self.update_images(board)
    def clickG12(self):
        if self.selected == 'm1':
            board.tiles[83].mirror1()
        if self.selected == 'm2':
            board.tiles[83].mirror2()
        if self.selected == 'm3':
            board.tiles[83].mirror3()
        if self.selected == 'm4':
            board.tiles[83].mirror4()
        if self.selected == 'lensX':
            board.tiles[83].lensX()
        if self.selected == 'lensY':
            board.tiles[83].lensY()
        if self.selected == 'block':
            board.tiles[83].block()
        self.update_images(board)
    def clickH1(self):
        if self.selected == 'm1':
            board.tiles[84].mirror1()
        if self.selected == 'm2':
            board.tiles[84].mirror2()
        if self.selected == 'm3':
            board.tiles[84].mirror3()
        if self.selected == 'm4':
            board.tiles[84].mirror4()
        if self.selected == 'lensX':
            board.tiles[84].lensX()
        if self.selected == 'lensY':
            board.tiles[84].lensY()
        if self.selected == 'block':
            board.tiles[84].block()
        self.update_images(board)
    def clickH2(self):
        if self.selected == 'm1':
            board.tiles[85].mirror1()
        if self.selected == 'm2':
            board.tiles[85].mirror2()
        if self.selected == 'm3':
            board.tiles[85].mirror3()
        if self.selected == 'm4':
            board.tiles[85].mirror4()
        if self.selected == 'lensX':
            board.tiles[85].lensX()
        if self.selected == 'lensY':
            board.tiles[85].lensY()
        if self.selected == 'block':
            board.tiles[85].block()
        self.update_images(board)
    def clickH3(self):
        if self.selected == 'm1':
            board.tiles[86].mirror1()
        if self.selected == 'm2':
            board.tiles[86].mirror2()
        if self.selected == 'm3':
            board.tiles[86].mirror3()
        if self.selected == 'm4':
            board.tiles[86].mirror4()
        if self.selected == 'lensX':
            board.tiles[86].lensX()
        if self.selected == 'lensY':
            board.tiles[86].lensY()
        if self.selected == 'block':
            board.tiles[86].block()
        self.update_images(board)
    def clickH4(self):
        if self.selected == 'm1':
            board.tiles[87].mirror1()
        if self.selected == 'm2':
            board.tiles[87].mirror2()
        if self.selected == 'm3':
            board.tiles[87].mirror3()
        if self.selected == 'm4':
            board.tiles[87].mirror4()
        if self.selected == 'lensX':
            board.tiles[87].lensX()
        if self.selected == 'lensY':
            board.tiles[87].lensY()
        if self.selected == 'block':
            board.tiles[87].block()
        self.update_images(board)
    def clickH5(self):
        if self.selected == 'm1':
            board.tiles[88].mirror1()
        if self.selected == 'm2':
            board.tiles[88].mirror2()
        if self.selected == 'm3':
            board.tiles[88].mirror3()
        if self.selected == 'm4':
            board.tiles[88].mirror4()
        if self.selected == 'lensX':
            board.tiles[88].lensX()
        if self.selected == 'lensY':
            board.tiles[88].lensY()
        if self.selected == 'block':
            board.tiles[88].block()
        self.update_images(board)
    def clickH6(self):
        if self.selected == 'm1':
            board.tiles[89].mirror1()
        if self.selected == 'm2':
            board.tiles[89].mirror2()
        if self.selected == 'm3':
            board.tiles[89].mirror3()
        if self.selected == 'm4':
            board.tiles[89].mirror4()
        if self.selected == 'lensX':
            board.tiles[89].lensX()
        if self.selected == 'lensY':
            board.tiles[89].lensY()
        if self.selected == 'block':
            board.tiles[89].block()
        self.update_images(board)
    def clickH7(self):
        if self.selected == 'm1':
            board.tiles[90].mirror1()
        if self.selected == 'm2':
            board.tiles[90].mirror2()
        if self.selected == 'm3':
            board.tiles[90].mirror3()
        if self.selected == 'm4':
            board.tiles[90].mirror4()
        if self.selected == 'lensX':
            board.tiles[90].lensX()
        if self.selected == 'lensY':
            board.tiles[90].lensY()
        if self.selected == 'block':
            board.tiles[90].block()
        self.update_images(board)
    def clickH8(self):
        if self.selected == 'm1':
            board.tiles[91].mirror1()
        if self.selected == 'm2':
            board.tiles[91].mirror2()
        if self.selected == 'm3':
            board.tiles[91].mirror3()
        if self.selected == 'm4':
            board.tiles[91].mirror4()
        if self.selected == 'lensX':
            board.tiles[91].lensX()
        if self.selected == 'lensY':
            board.tiles[91].lensY()
        if self.selected == 'block':
            board.tiles[91].block()
        self.update_images(board)
    def clickH9(self):
        if self.selected == 'm1':
            board.tiles[92].mirror1()
        if self.selected == 'm2':
            board.tiles[92].mirror2()
        if self.selected == 'm3':
            board.tiles[92].mirror3()
        if self.selected == 'm4':
            board.tiles[92].mirror4()
        if self.selected == 'lensX':
            board.tiles[92].lensX()
        if self.selected == 'lensY':
            board.tiles[92].lensY()
        if self.selected == 'block':
            board.tiles[92].block()
        self.update_images(board)
    def clickH10(self):
        if self.selected == 'm1':
            board.tiles[93].mirror1()
        if self.selected == 'm2':
            board.tiles[93].mirror2()
        if self.selected == 'm3':
            board.tiles[93].mirror3()
        if self.selected == 'm4':
            board.tiles[93].mirror4()
        if self.selected == 'lensX':
            board.tiles[93].lensX()
        if self.selected == 'lensY':
            board.tiles[93].lensY()
        if self.selected == 'block':
            board.tiles[93].block()
        self.update_images(board)
    def clickH11(self):
        if self.selected == 'm1':
            board.tiles[94].mirror1()
        if self.selected == 'm2':
            board.tiles[94].mirror2()
        if self.selected == 'm3':
            board.tiles[94].mirror3()
        if self.selected == 'm4':
            board.tiles[94].mirror4()
        if self.selected == 'lensX':
            board.tiles[94].lensX()
        if self.selected == 'lensY':
            board.tiles[94].lensY()
        if self.selected == 'block':
            board.tiles[94].block()
        self.update_images(board)
    def clickH12(self):
        if self.selected == 'm1':
            board.tiles[95].mirror1()
        if self.selected == 'm2':
            board.tiles[95].mirror2()
        if self.selected == 'm3':
            board.tiles[95].mirror3()
        if self.selected == 'm4':
            board.tiles[95].mirror4()
        if self.selected == 'lensX':
            board.tiles[95].lensX()
        if self.selected == 'lensY':
            board.tiles[95].lensY()
        if self.selected == 'block':
            board.tiles[95].block()
        self.update_images(board)
    def clickI1(self):
        if self.selected == 'm1':
            board.tiles[96].mirror1()
        if self.selected == 'm2':
            board.tiles[96].mirror2()
        if self.selected == 'm3':
            board.tiles[96].mirror3()
        if self.selected == 'm4':
            board.tiles[96].mirror4()
        if self.selected == 'lensX':
            board.tiles[96].lensX()
        if self.selected == 'lensY':
            board.tiles[96].lensY()
        if self.selected == 'block':
            board.tiles[96].block()
        self.update_images(board)
    def clickI2(self):
        if self.selected == 'm1':
            board.tiles[97].mirror1()
        if self.selected == 'm2':
            board.tiles[97].mirror2()
        if self.selected == 'm3':
            board.tiles[97].mirror3()
        if self.selected == 'm4':
            board.tiles[97].mirror4()
        if self.selected == 'lensX':
            board.tiles[97].lensX()
        if self.selected == 'lensY':
            board.tiles[97].lensY()
        if self.selected == 'block':
            board.tiles[97].block()
        self.update_images(board)
    def clickI3(self):
        if self.selected == 'm1':
            board.tiles[98].mirror1()
        if self.selected == 'm2':
            board.tiles[98].mirror2()
        if self.selected == 'm3':
            board.tiles[98].mirror3()
        if self.selected == 'm4':
            board.tiles[98].mirror4()
        if self.selected == 'lensX':
            board.tiles[98].lensX()
        if self.selected == 'lensY':
            board.tiles[98].lensY()
        if self.selected == 'block':
            board.tiles[98].block()
        self.update_images(board)
    def clickI4(self):
        if self.selected == 'm1':
            board.tiles[99].mirror1()
        if self.selected == 'm2':
            board.tiles[99].mirror2()
        if self.selected == 'm3':
            board.tiles[99].mirror3()
        if self.selected == 'm4':
            board.tiles[99].mirror4()
        if self.selected == 'lensX':
            board.tiles[99].lensX()
        if self.selected == 'lensY':
            board.tiles[99].lensY()
        if self.selected == 'block':
            board.tiles[99].block()
        self.update_images(board)
    def clickI5(self):
        if self.selected == 'm1':
            board.tiles[100].mirror1()
        if self.selected == 'm2':
            board.tiles[100].mirror2()
        if self.selected == 'm3':
            board.tiles[100].mirror3()
        if self.selected == 'm4':
            board.tiles[100].mirror4()
        if self.selected == 'lensX':
            board.tiles[100].lensX()
        if self.selected == 'lensY':
            board.tiles[100].lensY()
        if self.selected == 'block':
            board.tiles[100].block()
        self.update_images(board)
    def clickI6(self):
        if self.selected == 'm1':
            board.tiles[101].mirror1()
        if self.selected == 'm2':
            board.tiles[101].mirror2()
        if self.selected == 'm3':
            board.tiles[101].mirror3()
        if self.selected == 'm4':
            board.tiles[101].mirror4()
        if self.selected == 'lensX':
            board.tiles[101].lensX()
        if self.selected == 'lensY':
            board.tiles[101].lensY()
        if self.selected == 'block':
            board.tiles[101].block()
        self.update_images(board)
    def clickI7(self):
        if self.selected == 'm1':
            board.tiles[102].mirror1()
        if self.selected == 'm2':
            board.tiles[102].mirror2()
        if self.selected == 'm3':
            board.tiles[102].mirror3()
        if self.selected == 'm4':
            board.tiles[102].mirror4()
        if self.selected == 'lensX':
            board.tiles[102].lensX()
        if self.selected == 'lensY':
            board.tiles[102].lensY()
        if self.selected == 'block':
            board.tiles[102].block()
        self.update_images(board)
    def clickI8(self):
        if self.selected == 'm1':
            board.tiles[103].mirror1()
        if self.selected == 'm2':
            board.tiles[103].mirror2()
        if self.selected == 'm3':
            board.tiles[103].mirror3()
        if self.selected == 'm4':
            board.tiles[103].mirror4()
        if self.selected == 'lensX':
            board.tiles[103].lensX()
        if self.selected == 'lensY':
            board.tiles[103].lensY()
        if self.selected == 'block':
            board.tiles[103].block()
        self.update_images(board)
    def clickI9(self):
        if self.selected == 'm1':
            board.tiles[104].mirror1()
        if self.selected == 'm2':
            board.tiles[104].mirror2()
        if self.selected == 'm3':
            board.tiles[104].mirror3()
        if self.selected == 'm4':
            board.tiles[104].mirror4()
        if self.selected == 'lensX':
            board.tiles[104].lensX()
        if self.selected == 'lensY':
            board.tiles[104].lensY()
        if self.selected == 'block':
            board.tiles[104].block()
        self.update_images(board)
    def clickI10(self):
        if self.selected == 'm1':
            board.tiles[105].mirror1()
        if self.selected == 'm2':
            board.tiles[105].mirror2()
        if self.selected == 'm3':
            board.tiles[105].mirror3()
        if self.selected == 'm4':
            board.tiles[105].mirror4()
        if self.selected == 'lensX':
            board.tiles[105].lensX()
        if self.selected == 'lensY':
            board.tiles[105].lensY()
        if self.selected == 'block':
            board.tiles[105].block()
        self.update_images(board)
    def clickI11(self):
        if self.selected == 'm1':
            board.tiles[106].mirror1()
        if self.selected == 'm2':
            board.tiles[106].mirror2()
        if self.selected == 'm3':
            board.tiles[106].mirror3()
        if self.selected == 'm4':
            board.tiles[106].mirror4()
        if self.selected == 'lensX':
            board.tiles[106].lensX()
        if self.selected == 'lensY':
            board.tiles[106].lensY()
        if self.selected == 'block':
            board.tiles[106].block()
        self.update_images(board)
    def clickI12(self):
        if self.selected == 'm1':
            board.tiles[107].mirror1()
        if self.selected == 'm2':
            board.tiles[107].mirror2()
        if self.selected == 'm3':
            board.tiles[107].mirror3()
        if self.selected == 'm4':
            board.tiles[107].mirror4()
        if self.selected == 'lensX':
            board.tiles[107].lensX()
        if self.selected == 'lensY':
            board.tiles[107].lensY()
        if self.selected == 'block':
            board.tiles[107].block()
        self.update_images(board)
    def clickJ1(self):
        if self.selected == 'm1':
            board.tiles[108].mirror1()
        if self.selected == 'm2':
            board.tiles[108].mirror2()
        if self.selected == 'm3':
            board.tiles[108].mirror3()
        if self.selected == 'm4':
            board.tiles[108].mirror4()
        if self.selected == 'lensX':
            board.tiles[108].lensX()
        if self.selected == 'lensY':
            board.tiles[108].lensY()
        if self.selected == 'block':
            board.tiles[108].block()
        self.update_images(board)
    def clickJ2(self):
        if self.selected == 'm1':
            board.tiles[109].mirror1()
        if self.selected == 'm2':
            board.tiles[109].mirror2()
        if self.selected == 'm3':
            board.tiles[109].mirror3()
        if self.selected == 'm4':
            board.tiles[109].mirror4()
        if self.selected == 'lensX':
            board.tiles[109].lensX()
        if self.selected == 'lensY':
            board.tiles[109].lensY()
        if self.selected == 'block':
            board.tiles[109].block()
        self.update_images(board)
    def clickJ3(self):
        if self.selected == 'm1':
            board.tiles[110].mirror1()
        if self.selected == 'm2':
            board.tiles[110].mirror2()
        if self.selected == 'm3':
            board.tiles[110].mirror3()
        if self.selected == 'm4':
            board.tiles[110].mirror4()
        if self.selected == 'lensX':
            board.tiles[110].lensX()
        if self.selected == 'lensY':
            board.tiles[110].lensY()
        if self.selected == 'block':
            board.tiles[110].block()
        self.update_images(board)
    def clickJ4(self):
        if self.selected == 'm1':
            board.tiles[111].mirror1()
        if self.selected == 'm2':
            board.tiles[111].mirror2()
        if self.selected == 'm3':
            board.tiles[111].mirror3()
        if self.selected == 'm4':
            board.tiles[111].mirror4()
        if self.selected == 'lensX':
            board.tiles[111].lensX()
        if self.selected == 'lensY':
            board.tiles[111].lensY()
        if self.selected == 'block':
            board.tiles[111].block()
        self.update_images(board)
    def clickJ5(self):
        if self.selected == 'm1':
            board.tiles[112].mirror1()
        if self.selected == 'm2':
            board.tiles[112].mirror2()
        if self.selected == 'm3':
            board.tiles[112].mirror3()
        if self.selected == 'm4':
            board.tiles[112].mirror4()
        if self.selected == 'lensX':
            board.tiles[112].lensX()
        if self.selected == 'lensY':
            board.tiles[112].lensY()
        if self.selected == 'block':
            board.tiles[112].block()
        self.update_images(board)
    def clickJ6(self):
        if self.selected == 'm1':
            board.tiles[113].mirror1()
        if self.selected == 'm2':
            board.tiles[113].mirror2()
        if self.selected == 'm3':
            board.tiles[113].mirror3()
        if self.selected == 'm4':
            board.tiles[113].mirror4()
        if self.selected == 'lensX':
            board.tiles[113].lensX()
        if self.selected == 'lensY':
            board.tiles[113].lensY()
        if self.selected == 'block':
            board.tiles[113].block()
        self.update_images(board)
    def clickJ7(self):
        if self.selected == 'm1':
            board.tiles[114].mirror1()
        if self.selected == 'm2':
            board.tiles[114].mirror2()
        if self.selected == 'm3':
            board.tiles[114].mirror3()
        if self.selected == 'm4':
            board.tiles[114].mirror4()
        if self.selected == 'lensX':
            board.tiles[114].lensX()
        if self.selected == 'lensY':
            board.tiles[114].lensY()
        if self.selected == 'block':
            board.tiles[114].block()
        self.update_images(board)
    def clickJ8(self):
        if self.selected == 'm1':
            board.tiles[115].mirror1()
        if self.selected == 'm2':
            board.tiles[115].mirror2()
        if self.selected == 'm3':
            board.tiles[115].mirror3()
        if self.selected == 'm4':
            board.tiles[115].mirror4()
        if self.selected == 'lensX':
            board.tiles[115].lensX()
        if self.selected == 'lensY':
            board.tiles[115].lensY()
        if self.selected == 'block':
            board.tiles[115].block()
        self.update_images(board)
    def clickJ9(self):
        if self.selected == 'm1':
            board.tiles[116].mirror1()
        if self.selected == 'm2':
            board.tiles[116].mirror2()
        if self.selected == 'm3':
            board.tiles[116].mirror3()
        if self.selected == 'm4':
            board.tiles[116].mirror4()
        if self.selected == 'lensX':
            board.tiles[116].lensX()
        if self.selected == 'lensY':
            board.tiles[116].lensY()
        if self.selected == 'block':
            board.tiles[116].block()
        self.update_images(board)
    def clickJ10(self):
        if self.selected == 'm1':
            board.tiles[117].mirror1()
        if self.selected == 'm2':
            board.tiles[117].mirror2()
        if self.selected == 'm3':
            board.tiles[117].mirror3()
        if self.selected == 'm4':
            board.tiles[117].mirror4()
        if self.selected == 'lensX':
            board.tiles[117].lensX()
        if self.selected == 'lensY':
            board.tiles[117].lensY()
        if self.selected == 'block':
            board.tiles[117].block()
        self.update_images(board)
    def clickJ11(self):
        if self.selected == 'm1':
            board.tiles[118].mirror1()
        if self.selected == 'm2':
            board.tiles[118].mirror2()
        if self.selected == 'm3':
            board.tiles[118].mirror3()
        if self.selected == 'm4':
            board.tiles[118].mirror4()
        if self.selected == 'lensX':
            board.tiles[118].lensX()
        if self.selected == 'lensY':
            board.tiles[118].lensY()
        if self.selected == 'block':
            board.tiles[118].block()
        self.update_images(board)
    def clickJ12(self):
        if self.selected == 'm1':
            board.tiles[119].mirror1()
        if self.selected == 'm2':
            board.tiles[119].mirror2()
        if self.selected == 'm3':
            board.tiles[119].mirror3()
        if self.selected == 'm4':
            board.tiles[119].mirror4()
        if self.selected == 'lensX':
            board.tiles[119].lensX()
        if self.selected == 'lensY':
            board.tiles[119].lensY()
        if self.selected == 'block':
            board.tiles[119].block()
        self.update_images(board)
    def clickK1(self):
        if self.selected == 'm1':
            board.tiles[120].mirror1()
        if self.selected == 'm2':
            board.tiles[120].mirror2()
        if self.selected == 'm3':
            board.tiles[120].mirror3()
        if self.selected == 'm4':
            board.tiles[120].mirror4()
        if self.selected == 'lensX':
            board.tiles[120].lensX()
        if self.selected == 'lensY':
            board.tiles[120].lensY()
        if self.selected == 'block':
            board.tiles[120].block()
        self.update_images(board)
    def clickK2(self):
        if self.selected == 'm1':
            board.tiles[121].mirror1()
        if self.selected == 'm2':
            board.tiles[121].mirror2()
        if self.selected == 'm3':
            board.tiles[121].mirror3()
        if self.selected == 'm4':
            board.tiles[121].mirror4()
        if self.selected == 'lensX':
            board.tiles[121].lensX()
        if self.selected == 'lensY':
            board.tiles[121].lensY()
        if self.selected == 'block':
            board.tiles[121].block()
        self.update_images(board)
    def clickK3(self):
        if self.selected == 'm1':
            board.tiles[122].mirror1()
        if self.selected == 'm2':
            board.tiles[122].mirror2()
        if self.selected == 'm3':
            board.tiles[122].mirror3()
        if self.selected == 'm4':
            board.tiles[122].mirror4()
        if self.selected == 'lensX':
            board.tiles[122].lensX()
        if self.selected == 'lensY':
            board.tiles[122].lensY()
        if self.selected == 'block':
            board.tiles[122].block()
        self.update_images(board)
    def clickK4(self):
        if self.selected == 'm1':
            board.tiles[123].mirror1()
        if self.selected == 'm2':
            board.tiles[123].mirror2()
        if self.selected == 'm3':
            board.tiles[123].mirror3()
        if self.selected == 'm4':
            board.tiles[123].mirror4()
        if self.selected == 'lensX':
            board.tiles[123].lensX()
        if self.selected == 'lensY':
            board.tiles[123].lensY()
        if self.selected == 'block':
            board.tiles[123].block()
        self.update_images(board)
    def clickK5(self):
        if self.selected == 'm1':
            board.tiles[124].mirror1()
        if self.selected == 'm2':
            board.tiles[124].mirror2()
        if self.selected == 'm3':
            board.tiles[124].mirror3()
        if self.selected == 'm4':
            board.tiles[124].mirror4()
        if self.selected == 'lensX':
            board.tiles[124].lensX()
        if self.selected == 'lensY':
            board.tiles[124].lensY()
        if self.selected == 'block':
            board.tiles[124].block()
        self.update_images(board)
    def clickK6(self):
        if self.selected == 'm1':
            board.tiles[125].mirror1()
        if self.selected == 'm2':
            board.tiles[125].mirror2()
        if self.selected == 'm3':
            board.tiles[125].mirror3()
        if self.selected == 'm4':
            board.tiles[125].mirror4()
        if self.selected == 'lensX':
            board.tiles[125].lensX()
        if self.selected == 'lensY':
            board.tiles[125].lensY()
        if self.selected == 'block':
            board.tiles[125].block()
        self.update_images(board)
    def clickK7(self):
        if self.selected == 'm1':
            board.tiles[126].mirror1()
        if self.selected == 'm2':
            board.tiles[126].mirror2()
        if self.selected == 'm3':
            board.tiles[126].mirror3()
        if self.selected == 'm4':
            board.tiles[126].mirror4()
        if self.selected == 'lensX':
            board.tiles[126].lensX()
        if self.selected == 'lensY':
            board.tiles[126].lensY()
        if self.selected == 'block':
            board.tiles[126].block()
        self.update_images(board)
    def clickK8(self):
        if self.selected == 'm1':
            board.tiles[127].mirror1()
        if self.selected == 'm2':
            board.tiles[127].mirror2()
        if self.selected == 'm3':
            board.tiles[127].mirror3()
        if self.selected == 'm4':
            board.tiles[127].mirror4()
        if self.selected == 'lensX':
            board.tiles[127].lensX()
        if self.selected == 'lensY':
            board.tiles[127].lensY()
        if self.selected == 'block':
            board.tiles[127].block()
        self.update_images(board)
    def clickK9(self):
        if self.selected == 'm1':
            board.tiles[128].mirror1()
        if self.selected == 'm2':
            board.tiles[128].mirror2()
        if self.selected == 'm3':
            board.tiles[128].mirror3()
        if self.selected == 'm4':
            board.tiles[128].mirror4()
        if self.selected == 'lensX':
            board.tiles[128].lensX()
        if self.selected == 'lensY':
            board.tiles[128].lensY()
        if self.selected == 'block':
            board.tiles[128].block()
        self.update_images(board)
    def clickK10(self):
        if self.selected == 'm1':
            board.tiles[129].mirror1()
        if self.selected == 'm2':
            board.tiles[129].mirror2()
        if self.selected == 'm3':
            board.tiles[129].mirror3()
        if self.selected == 'm4':
            board.tiles[129].mirror4()
        if self.selected == 'lensX':
            board.tiles[129].lensX()
        if self.selected == 'lensY':
            board.tiles[129].lensY()
        if self.selected == 'block':
            board.tiles[129].block()
        self.update_images(board)
    def clickK11(self):
        if self.selected == 'm1':
            board.tiles[130].mirror1()
        if self.selected == 'm2':
            board.tiles[130].mirror2()
        if self.selected == 'm3':
            board.tiles[130].mirror3()
        if self.selected == 'm4':
            board.tiles[130].mirror4()
        if self.selected == 'lensX':
            board.tiles[130].lensX()
        if self.selected == 'lensY':
            board.tiles[130].lensY()
        if self.selected == 'block':
            board.tiles[130].block()
        self.update_images(board)
    def clickK12(self):
        if self.selected == 'm1':
            board.tiles[131].mirror1()
        if self.selected == 'm2':
            board.tiles[131].mirror2()
        if self.selected == 'm3':
            board.tiles[131].mirror3()
        if self.selected == 'm4':
            board.tiles[131].mirror4()
        if self.selected == 'lensX':
            board.tiles[131].lensX()
        if self.selected == 'lensY':
            board.tiles[131].lensY()
        if self.selected == 'block':
            board.tiles[131].block()
        self.update_images(board)
    def clickL1(self):
        if self.selected == 'm1':
            board.tiles[132].mirror1()
        if self.selected == 'm2':
            board.tiles[132].mirror2()
        if self.selected == 'm3':
            board.tiles[132].mirror3()
        if self.selected == 'm4':
            board.tiles[132].mirror4()
        if self.selected == 'lensX':
            board.tiles[132].lensX()
        if self.selected == 'lensY':
            board.tiles[132].lensY()
        if self.selected == 'block':
            board.tiles[132].block()
        self.update_images(board)
    def clickL2(self):
        if self.selected == 'm1':
            board.tiles[133].mirror1()
        if self.selected == 'm2':
            board.tiles[133].mirror2()
        if self.selected == 'm3':
            board.tiles[133].mirror3()
        if self.selected == 'm4':
            board.tiles[133].mirror4()
        if self.selected == 'lensX':
            board.tiles[133].lensX()
        if self.selected == 'lensY':
            board.tiles[133].lensY()
        if self.selected == 'block':
            board.tiles[133].block()
        self.update_images(board)
    def clickL3(self):
        if self.selected == 'm1':
            board.tiles[134].mirror1()
        if self.selected == 'm2':
            board.tiles[134].mirror2()
        if self.selected == 'm3':
            board.tiles[134].mirror3()
        if self.selected == 'm4':
            board.tiles[134].mirror4()
        if self.selected == 'lensX':
            board.tiles[134].lensX()
        if self.selected == 'lensY':
            board.tiles[134].lensY()
        if self.selected == 'block':
            board.tiles[134].block()
        self.update_images(board)
    def clickL4(self):
        if self.selected == 'm1':
            board.tiles[135].mirror1()
        if self.selected == 'm2':
            board.tiles[135].mirror2()
        if self.selected == 'm3':
            board.tiles[135].mirror3()
        if self.selected == 'm4':
            board.tiles[135].mirror4()
        if self.selected == 'lensX':
            board.tiles[135].lensX()
        if self.selected == 'lensY':
            board.tiles[135].lensY()
        if self.selected == 'block':
            board.tiles[135].block()
        self.update_images(board)
    def clickL5(self):
        if self.selected == 'm1':
            board.tiles[136].mirror1()
        if self.selected == 'm2':
            board.tiles[136].mirror2()
        if self.selected == 'm3':
            board.tiles[136].mirror3()
        if self.selected == 'm4':
            board.tiles[136].mirror4()
        if self.selected == 'lensX':
            board.tiles[136].lensX()
        if self.selected == 'lensY':
            board.tiles[136].lensY()
        if self.selected == 'block':
            board.tiles[136].block()
        self.update_images(board)
    def clickL6(self):
        if self.selected == 'm1':
            board.tiles[137].mirror1()
        if self.selected == 'm2':
            board.tiles[137].mirror2()
        if self.selected == 'm3':
            board.tiles[137].mirror3()
        if self.selected == 'm4':
            board.tiles[137].mirror4()
        if self.selected == 'lensX':
            board.tiles[137].lensX()
        if self.selected == 'lensY':
            board.tiles[137].lensY()
        if self.selected == 'block':
            board.tiles[137].block()
        self.update_images(board)
    def clickL7(self):
        if self.selected == 'm1':
            board.tiles[138].mirror1()
        if self.selected == 'm2':
            board.tiles[138].mirror2()
        if self.selected == 'm3':
            board.tiles[138].mirror3()
        if self.selected == 'm4':
            board.tiles[138].mirror4()
        if self.selected == 'lensX':
            board.tiles[138].lensX()
        if self.selected == 'lensY':
            board.tiles[138].lensY()
        if self.selected == 'block':
            board.tiles[138].block()
        self.update_images(board)
    def clickL8(self):
        if self.selected == 'm1':
            board.tiles[139].mirror1()
        if self.selected == 'm2':
            board.tiles[139].mirror2()
        if self.selected == 'm3':
            board.tiles[139].mirror3()
        if self.selected == 'm4':
            board.tiles[139].mirror4()
        if self.selected == 'lensX':
            board.tiles[139].lensX()
        if self.selected == 'lensY':
            board.tiles[139].lensY()
        if self.selected == 'block':
            board.tiles[139].block()
        self.update_images(board)
    def clickL9(self):
        if self.selected == 'm1':
            board.tiles[140].mirror1()
        if self.selected == 'm2':
            board.tiles[140].mirror2()
        if self.selected == 'm3':
            board.tiles[140].mirror3()
        if self.selected == 'm4':
            board.tiles[140].mirror4()
        if self.selected == 'lensX':
            board.tiles[140].lensX()
        if self.selected == 'lensY':
            board.tiles[140].lensY()
        if self.selected == 'block':
            board.tiles[140].block()
        self.update_images(board)
    def clickL10(self):
        if self.selected == 'm1':
            board.tiles[141].mirror1()
        if self.selected == 'm2':
            board.tiles[141].mirror2()
        if self.selected == 'm3':
            board.tiles[141].mirror3()
        if self.selected == 'm4':
            board.tiles[141].mirror4()
        if self.selected == 'lensX':
            board.tiles[141].lensX()
        if self.selected == 'lensY':
            board.tiles[141].lensY()
        if self.selected == 'block':
            board.tiles[141].block()
        self.update_images(board)
    def clickL11(self):
        if self.selected == 'm1':
            board.tiles[142].mirror1()
        if self.selected == 'm2':
            board.tiles[142].mirror2()
        if self.selected == 'm3':
            board.tiles[142].mirror3()
        if self.selected == 'm4':
            board.tiles[142].mirror4()
        if self.selected == 'lensX':
            board.tiles[142].lensX()
        if self.selected == 'lensY':
            board.tiles[142].lensY()
        if self.selected == 'block':
            board.tiles[142].block()
        self.update_images(board)
    def clickL12(self):
        if self.selected == 'm1':
            board.tiles[143].mirror1()
        if self.selected == 'm2':
            board.tiles[143].mirror2()
        if self.selected == 'm3':
            board.tiles[143].mirror3()
        if self.selected == 'm4':
            board.tiles[143].mirror4()
        if self.selected == 'lensX':
            board.tiles[143].lensX()
        if self.selected == 'lensY':
            board.tiles[143].lensY()
        if self.selected == 'block':
            board.tiles[143].block()
        self.update_images(board)


board = GameBoard()
app = Application(root)
root.mainloop()
