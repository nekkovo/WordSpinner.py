from graphics import *
from Dice import *


class Horse:
    def __init__(self, speednumber, y_position, image, win):
        self.speednumber = speednumber
        self.y_position = y_position
        self.x_position = 50
        self.image = image
        self.win = win

    def move(self):
        speed = Dice(self.speednumber).roll()
        self.x_position += speed

    def draw(self):
        self.image.draw_at_pos(self.win, self.x_position, self.y_position)

    def crossed_finish_line(self, finishline):
        if self.x_position >= finishline:
            return True
        else:
            return False


def main():
    win = GraphWin('racing_field', 700, 400, autoflush=False)
    win.setBackground('black')
    finish_line = Line(Point(650, 0), Point(650, 400))
    finish_line.setFill('white')
    finish_line.draw(win)
    finish_lineX = finish_line.getP1().getX()
    knight_image = Image(Point(0, 0), 'Knight.gif')
    wizard_image = Image(Point(0, 0), 'Wizard.gif')
    knight_horse = Horse(10, 100, knight_image, win)
    wizard_horse = Horse(10, 200, wizard_image, win)
    knight_horse.draw()
    wizard_horse.draw()
    win.getMouse()

    while not knight_horse.crossed_finish_line(finish_lineX) and not wizard_horse.crossed_finish_line(finish_lineX):
        win.clear_win()
        finish_line.draw(win)
        knight_horse.move()
        wizard_horse.move()
        knight_horse.draw()
        wizard_horse.draw()
        update(30)

    if knight_horse.x_position == wizard_horse.x_position:
        print('Tie')
    elif knight_horse.x_position > wizard_horse.x_position:
        print('YAY!! Horse Knight is the winner!!')
    elif knight_horse.x_position < wizard_horse.x_position:
        print('YAY!! Horse Wizard is the winner!!')

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
