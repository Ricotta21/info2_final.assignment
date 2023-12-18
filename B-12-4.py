import pyxel

class Ball: 
    r = 10
    color = 6
    speed = 1

    def __init__(self):
        self.restart()

    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed
        if (self.x < 0 and self.vx < 0) or (self.x > 200 and self.vx > 0):
            self.vx *= -1

    def restart(self):
        self.x = pyxel.rndi(0, 199)    #0から画面の横幅-1の間
        self.y = 0
        angle = pyxel.rndi(30, 150)    #30度から150度の間
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)
        self.score_flag = True
        


class Pad:
    def __init__(self):
        self.x = 100

    def catch(self, ball):
        return ball.y >= 195 and self.x-20 <= ball.x <= self.x+20 and ball.score_flag

class App:
    def __init__(self):
        pyxel.init(200,200)
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='77', effects='NN', speed=10)
        pyxel.sound(1).set(notes='G2G2', tones='NN', volumes='77', effects='NN', speed=10)

        self.balls = [Ball()]
        self.pad = Pad()
        self.score = 0
        self.miss = 0
        self.gameover_flag = False

        pyxel.run(self.update, self.draw)

    def update(self):

        if self.gameover_flag:
            return

        self.pad.x = pyxel.mouse_x
    
        for b in self.balls:
            b.move()

            if self.pad.catch(b):
                pyxel.play(0, 0)
                self.score += 1
                b.score_flag = False

                if self.score >= len(self.balls) * 3:
                    balls.append(Ball())
                    Ball.speed = 1
        
            if b.y >= 200:

                if b.score_flag:
                    pyxel.play(0,1)
                    self.miss += 1
                    if self.miss >= 10:
                        self.gameover_flag = True
            
                b.restart() 
                Ball.speed += 1          
        
            

    def draw(self):
        if self.gameover_flag:
            pyxel.text(80,100,"-GAME OVER-",5)
        else:
            pyxel.cls(7)
            for b in self.balls:
                pyxel.circ(b.x,b.y,Ball.r,Ball.color)
            pyxel.rect(self.pad.x-20, 195, 40, 5, 14)
            pyxel.text(0,0,"SCORE:"+str(self.score),0)

App()