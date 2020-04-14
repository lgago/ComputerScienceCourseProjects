"""
File: bookgui.py
Project 3
User is presented with a UI to work with the bookproj.py functionality.
"""

import random
from breezypythongui import EasyFrame
from bookproj import *


class bookGui(EasyFrame):
    """Allows the user to enter in reader information."""

    def __init__(self):
        """Sets up the window,widgets, and data."""
        EasyFrame.__init__(self, title = "Book Recommendations")
        self.lowerBound = 1
        self.upperBound = 100
        self.count = 0
        self.friendsbtn = self.addButton(text = "Friends", row = 1,
                                    column = 1, command=self.friends)
        self.recommendbtn = self.addButton(text = "Recommend", row = 1,
                                        column = 2, command=self.recommend)
        self.reportbtn = self.addButton(text = "Report", row = 1,
                                        column = 3,
                                        command = self.report)

    def friends(self):
        """This option displays a dialog box prompting for a reader name and a number of 
        friends (nfriends, the readers with the highest affinity scores to the user of interest; 
        display 2 as the default value in the number field), and displays the nfriends friends, 
        one per line, in a message box. This calls your modified friends function."""
        name = self.prompterBox(title="Friends - Reader Name", promptString="Reader Name")
        nfriends = self.prompterBox(title="Friends - # of friends", inputText=2, promptString="# of friends")
        nfriends = int(nfriends)

        if nfriends < 0:
            self.messageBox(title="Error", message=" # of friends must be positive")
            return
        try:
            friendsList = friends(name, nfriends)
            friendsList = "\n".join(friendsList)
            self.messageBox(title="Friends", message=friendsList, width=100, height=100)
        except:
            self.messageBox(title="Error", message=name + " is not a valid reader name")
        

        
    def recommend(self):
        """This displays a dialog box prompting for a reader name and number of friends, 
        and then displays recommendations for that user in a message box, using the number 
        of top friends requested. Validate that the reader exists in the system. This calls 
        your recommend function from Project 1."""
        name = self.prompterBox(title="Friends - User Name", promptString="Reader Name")
        nfriends = self.prompterBox(title="Friends - # of friends requested", inputText=2, promptString="# of friends")
        nfriends = int(nfriends)

        if nfriends < 0:
            self.messageBox(title="Error", message=" # of friends must be positive")
            return

        try:
            self.messageBox(title="Recommend", message=recommend(name, nfriends), width=100, height=100)
        except:
            self.messageBox(title="Error", message=name + " is not a valid reader name")

    def report(self):
        """This option displays the same output from bookrecs.main() as you did in Project 1, 
        but in a message box. For this option, just use the default of nfriends=2. This calls 
        your report function from Project 2."""
        self.messageBox(title = "Report", message = report(), width=100, height=100)

def main():
    """Instantiate and pop up the window."""
    bookGui().mainloop()

if __name__ == "__main__":
    main()
