class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('У ручек пилот самые красивые чернила')


class Pensil(Stationary):
    def draw(self):
        print('Карандаши бывают разные по плотности')


class Handle(Stationary):
    def draw(self):
        print('Выделения маркером по тексту помогают структурировать информацию')





a = Pen('pilot')
b = Pensil('soft')
c = Handle('ErichKrause')
a.draw()
b.draw()
c.draw()