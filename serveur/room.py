import random
import map1

class Room:
    def __init__(self, client1, client2):
        # self.questions, self.answers = self.generate_questions()
        # self.indexs = {client1: 0, client2: 0}
        self.map = self.init_map()
        self.wall_position = self.generate_wall()
        self.finished = False
    
    def init_map(self):
        MAP=[]
        for i in range(7):
            row=[]
            for a in range(7):
                tile = random.choice(['l','a','t'])
                rand=random.choice([0,90,180,270])
                if (i == 0 and a == 0):
                    tile = 'a'
                    rand=180
                if (i == 0 and a == 6):
                    tile = 'a'
                    rand=270
                if (i == 6 and a == 0):
                    tile = 'a'
                    rand = 90
                if (i==6 and a == 6):
                    tile = 'a'
                    rand=0
                row.append(map1.Map(tile, rand))
            MAP.append(row)
            self.map=MAP
        return MAP
    
    def generate_wall(self):
        wall_position=[]
        for b in range(len(self.map)):
            for c in range(len(self.map[b])):
                self.map[b][c] = self.map[b][c].get_object(c,b)
                for i in self.map[b][c].get_wall():
                        wall_position.append(i)
            self.wall_position= wall_position
        return wall_position
            
