"""
videostore.py
author - will - 07/18/23
chpt 8 gui based demo of a video store POS UI 
"""
#imports
####MUST HAVE BREEZYPYTHONGUI IN SAME WORKING DIRECTORY#####
from breezypythongui import EasyFrame
from tkinter.font import Font


#Main Class - Store POS 
class VideoStore(EasyFrame):
    #class constructor method
    
    def __init__(self):
        #bg - #274029
        #text - #55342D
        #font size - info - 13 // totals 15
        #dark - #25A18E
        #med - #7AE582
        #light - #9FFFCB
        #Window
        EasyFrame.__init__(self, title="Video Store", width=400, height=350, background="#9FFFCB")
        
        #Heading
        self.infoFont =Font (family="Monospace",size= 13)
        self.totalFont =Font (family="Monospace",size= 15)
        self.addLabel(text="Welcome to Five Star Video", row=0, column=0, columnspan=2, sticky="news",font=Font(family="Monospace",size= 15),background="#25A18E",foreground="#55342D")

        #UI
        #new vids
        self.addLabel(text="# of New Rentals ($3.00):", row=1, column=0,foreground="#55342D", background="#25A18E", sticky="ne", font= self.infoFont)
        self.newvid = self.addIntegerField(row=1,column=1,value=0, width=4, sticky="nw")
        #old vids
        self.addLabel(text="# of Old Rentals ($2.00):", row=2, column=0,foreground="#55342D", background="#25A18E", sticky="ne", font= self.infoFont)
        self.oldvid = self.addIntegerField(row=2,column=1,value=0, width=4, sticky="nw")
        #button
        self.totalBtn = self.addButton(text="Total", row=3, column=0, columnspan=2,command=self.calculate)
        #result display
        self.addLabel(text="Total for the order is: ", row=4, column=0, columnspan=2, sticky="nw", background="#9FFFCB",foreground="#55342D", font=self.totalFont)
        self.total = self.addFloatField(row=4,column=1,value=0, width=10, sticky="ne", precision=2, state="readonly")
    
    #main calculations
    def calculate(self):
        new = self.newvid.getNumber()
        old = self.oldvid.getNumber()

        result = (new * 3.00) + (old * 2.00)
        self.total.setNumber(result)

def main():
    #main run funcition
    VideoStore().mainloop()

if __name__ == "__main__":
    main()
