import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class CalculatorWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculator")
        self.set_border_width(10)

        grid = Gtk.Grid()
        self.add(grid)

        # Create the widget to display the stored value
        displayFrame = Gtk.Frame()
        displayBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        # Assign the widget as an attribute of the window so the label text can be changed
        self.displayLabel = Gtk.Label(label="")
        displayBox.pack_start(self.displayLabel, True, True, 0)
        displayFrame.add(displayBox)

        # Create all the number buttons
        numButton1 = Gtk.Button.new_with_label("7")
        numButton1.connect("clicked", self.number7Clicked)
        numButton2 = Gtk.Button.new_with_label("8")
        numButton2.connect("clicked", self.number8Clicked)
        numButton3 = Gtk.Button.new_with_label("9")
        numButton3.connect("clicked", self.number9Clicked)
        numButton4 = Gtk.Button.new_with_label("4")
        numButton4.connect("clicked", self.number4Clicked)
        numButton5 = Gtk.Button.new_with_label("5")
        numButton5.connect("clicked", self.number5Clicked)
        numButton6 = Gtk.Button.new_with_label("6")
        numButton6.connect("clicked", self.number6Clicked)
        numButton7 = Gtk.Button.new_with_label("1")
        numButton7.connect("clicked", self.number1Clicked)
        numButton8 = Gtk.Button.new_with_label("2")
        numButton8.connect("clicked", self.number2Clicked)
        numButton9 = Gtk.Button.new_with_label("3")
        numButton9.connect("clicked", self.number3Clicked)
        numButton10 = Gtk.Button.new_with_label("0")
        numButton10.connect("clicked", self.number0Clicked)

        # Create all the operation buttons
        operationButton1 = Gtk.Button.new_with_label("+")
        operationButton2 = Gtk.Button.new_with_label("-")
        operationButton3 = Gtk.Button.new_with_label(chr(247))
        operationButton4 = Gtk.Button.new_with_label("*")
        operationButton5 = Gtk.Button.new_with_label("=")
        operationButton6 = Gtk.Button.new_with_label("CLEAR")

        # Add the number display to the grid, set to column and row 0. Width of 3 and height of 1
        grid.attach(displayFrame, 0, 0, 3, 1)
        # Add the buttons to the grid
        grid.attach_next_to(numButton1, displayFrame, Gtk.PositionType.BOTTOM, 1, 1)
        # Arguments child, sibling, side, width, height
        grid.attach_next_to(numButton2, numButton1, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(numButton3, numButton2, Gtk.PositionType.RIGHT, 1, 1)   
        # Sets the buttons to be positioned directly below their number's value + 3
        grid.attach_next_to(numButton4, numButton1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(numButton5, numButton2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(numButton6, numButton3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(numButton7, numButton4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(numButton8, numButton5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(numButton9, numButton6, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(numButton10, numButton7, Gtk.PositionType.BOTTOM, 1, 1)
        # Sets the operation buttons to the intended positions
        grid.attach_next_to(operationButton1, numButton8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(operationButton5, numButton9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(operationButton4, numButton10, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(operationButton2, operationButton1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(operationButton3, operationButton5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(operationButton6, operationButton2, Gtk.PositionType.BOTTOM, 1, 1)

    # Signals for each number button. When clicked it will show the correct number in the display
    # label. This label will then be used as a number to perform an operation.
    def number7Clicked(self, numButton1):
        print(7)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "7")

    def number8Clicked(self, numButton2):
        print(8)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "8")

    def number9Clicked(self, numButton3):
        print(9)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "9")

    def number4Clicked(self, numButton4):
        print(4)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "4")

    def number5Clicked(self, numButton5):
        print(5)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "5")

    def number6Clicked(self, numButton6):
        print(6)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "6")

    def number1Clicked(self, numButton7):
        print(1)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "1")

    def number2Clicked(self, numButton8):
        print(2)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "2")

    def number3Clicked(self, numButton9):
        print(3)
        currentText = self.displayLabel.get_text()
        print(currentText)
        self.displayLabel.set_text(currentText + "3")

    def number0Clicked(self, numButton10):
        print(0)
        currentText = self.displayLabel.get_text()
        print(currentText)
        if (currentText != ""):
            self.displayLabel.set_text(currentText + "0")

win = CalculatorWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()