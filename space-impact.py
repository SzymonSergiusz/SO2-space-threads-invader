import curses
import time
import threading


COLUMNS = 50
ROWS = 25

class Player:
    def __init__(self, lifes):
        self.lifes = lifes
        self.sprite = '🚀'
        self.x = 10
        self.y = 10




class Timer:
    start_time = time.perf_counter()
    actual_time = "0:0"
    def refresh(self):
        now = time.perf_counter() - self.start_time
        minutes = int(now // 60)
        seconds = int(now % 60)
        self.actual_time = f"{minutes:02d}:{seconds:02d}"
    def __str__(self):
        return self.actual_time
class Space:
    def __init__(self):
        self.timer = Timer()
        self.player = Player(3)
        self.game_over = False

    def refresh(self):
        self.timer.refresh()
        self.game_over = self.player.lifes == 0

    def __str__(self):
        area = f'Czas gry: {self.timer}'
        area += f'Pozostałe życia: {self.player.lifes*'💜'}'
        # area = "#" * COLUMNS + str(self.timer) + "\n"

        return area


def start(window):
    space = Space()

    # control = threading.Thread(target=controller, args=(window, board))
    # control.start()
    #
    # waiter = threading.Thread(target=spawn_food, args=(board, ))
    # waiter.start()
    #
    # waiter2 = threading.Thread(target=spawn_food, args=(board, ")"))
    # waiter2.start()

    while not space.game_over:
        window.clear()
        window.insstr(0, 0, str(space))
        window.refresh()
        time.sleep(0.2)

        # board.move()
        space.refresh()

    # control.join()
    # waiter.join()
    # waiter2.join()


if __name__ == "__main__":
    curses.wrapper(start)