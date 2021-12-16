from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector # for 2D vectors
from kivy.clock import Clock # for scheduling updates on an interval

class PongBall(Widget):
    ''' the ball has a velocity and a position. the method you can do on the ball is moving it'''
    velocity_x = NumericProperty(0) # you declare properties in kivy class. its going to validate data is the type you declared it as; also allows implementation of observer pattern, better memory management
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongPaddle(Widget):
    score = NumericProperty(0) # declare score as 0

    def bounce_ball(self, ball):
        if self.collide_widget(ball): # collide widget looks like a really useful method
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2) # the ball has a shape. we want to collide with the edge of the ball so objects don't overlap
            bounced = Vector(-1 * vx, vy) #when one collides with paddle, switch the X direction
            vel = bounced * 1.1 #and speed up
            ball.velocity = vel.x, vel.y + offset # update the velocity

class PongGame(Widget): # the ponggame inherits from widget
    ball = ObjectProperty(None) # initalize a ball
    player1 = ObjectProperty(None) #initialize the two player paddles as well
    player2 = ObjectProperty(None)

    def serve_ball(self, vel = (4,0)):
        self.ball.center = self.center  # the pongname starts with the ball in dead center
        self.ball.velocity = vel # initialize a random velocity vector when you serve

    def update(self, dt): # this is called by clock interval
        self.ball.move()  # make the ball move

        # bounce of paddles
        self.player1.bounce_ball(self.ball) # this will call bounce all the time, but it will only implement it if there is a collison
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < self.y) or (self.ball.top > self.top): # if the ball hits bottom or top
            self.ball.velocity_y *= -1  # change the y velocity

        # bounce off left and right, score points
        if self.ball.x < self.x: # if it goes past player 1 paddle
            self.player2.score += 1
            self.serve_ball(vel = (4,0))
        if self.ball.x > self.width: # if it goes past player 2 paddle
            self.player1.score += 1
            self.serve_ball(vel=(-4,0))

    def on_touch_move(self, touch): #interesting touch object might be useful
        if touch.x < self.width / 3: # see if touching far end of screen
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y



class PongApp(App): # the main app inherets from App
    def build(self): # the main app class just has build
        game = PongGame() #initalize ponggame
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0) # control game mvoment on the screen. on an interval schedule game update
        return game

if __name__ == '__main__':
    PongApp().run()
