
class Agent:

    def __init__(self, id: int, value: float, src: int, dest: int, speed: float, pos: str):

        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.loc = pos.split(',')
        self.pos = (float(self.loc[0]), float(self.loc[1]), float(self.loc[2]))
        self.path = []
        self.tag = 0

    def get_id(self):
        return self.id

    def get_tag(self):
        return self.tag

    def set_tag(self):
        self.tag = 1

    def get_value(self):
        return self.value

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_speed(self):
        return self.speed

    def get_pos(self):
        return self.pos
