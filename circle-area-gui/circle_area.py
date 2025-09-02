"""
Created by: Swikriti
File: circleArea.py

Description:
This program creates a GUI application using Tkinter that:
- Takes the user's name
- Inputs the radius of a circle
- Computes and displays the area of the circle
- Shows a thank-you message with the user's name
"""

from tkinter import *
import math

class CircleArea(Frame):
    """GUI application class to calculate the area of a circle."""

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Circle Area")
        self.grid()

        # ------------------ Name Input ------------------ #
        self._nameLabel = Label(self, text='Name')
        self._nameLabel.grid(row=0, column=0)
        self._nameVar = StringVar()
        self._nameEntry = Entry(self, textvariable=self._nameVar)
        self._nameEntry.grid(row=0, column=1)

        # ------------------ Radius Input ------------------ #
        self._radiusLabel = Label(self, text="Radius")
        self._radiusLabel.grid(row=1, column=0)
        self._radiusVar = DoubleVar()
        self._radiusEntry = Entry(self, textvariable=self._radiusVar)
        self._radiusEntry.grid(row=1, column=1)

        # ------------------ Area Output ------------------ #
        self._areaLabel = Label(self, text="Area")
        self._areaLabel.grid(row=2, column=0)
        self._areaVar = DoubleVar()
        self._areaEntry = Entry(self, textvariable=self._areaVar)
        self._areaEntry.grid(row=2, column=1)

        # ------------------ Compute Button ------------------ #
        self._button = Button(self,
                              text="Compute",
                              command=self._area)
        self._button.grid(row=4, column=1, columnspan=2)

    def _area(self):
        """
        Event handler for the Compute button.
        Calculates the area of the circle using the radius,
        displays it in the area field, and shows a thank-you message.
        """
        radius = self._radiusVar.get()
        area = radius ** 2 * math.pi  # Area formula: πr²
        self._areaVar.set(area)

        name = self._nameVar.get()
        self._msgLabel = Label(self,
                               text=f"Thank you {name} for using the program")
        self._msgLabel.grid(row=5, column=0, columnspan=2)

def main():
    """Instantiate and display the CircleArea window."""
    CircleArea().mainloop()

# Run the program
if __name__ == "__main__":
    main()
