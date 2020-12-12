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
        displayLabel = Gtk.Label(label="")
        displayBox.pack_start(displayLabel, True, True, 0)
        displayFrame.add(displayBox)

        # Create all the number buttons
        numButton1 = Gtk.Button.new_with_label("7")
        numButton2 = Gtk.Button.new_with_label("8")
        numButton3 = Gtk.Button.new_with_label("9")
        numButton4 = Gtk.Button.new_with_label("4")
        numButton5 = Gtk.Button.new_with_label("5")
        numButton6 = Gtk.Button.new_with_label("6")
        numButton7 = Gtk.Button.new_with_label("1")
        numButton8 = Gtk.Button.new_with_label("2")
        numButton9 = Gtk.Button.new_with_label("3")
        numButton10 = Gtk.Button.new_with_label("0")

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
        grid.attach_next_to(numButton10, numButton9, Gtk.PositionType.BOTTOM, 1, 1)

win = CalculatorWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()