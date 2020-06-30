
import time
from itertools import cycle

class TrafficLight:
    __color = 'red'

    def running(self):
        count = 0
        for __color in cycle(['red', 'yellow', 'green']):
            if count > 7:
                break
            print(__color)
            count += 1
            if __color == 'red':
                time.sleep(7)
            elif __color == 'yellow':
                time.sleep(2)
            else:
                time.sleep(15)

a = TrafficLight()
a.running()
