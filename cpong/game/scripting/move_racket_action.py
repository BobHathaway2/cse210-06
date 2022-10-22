from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        rackets = []
        rackets = cast.get_actors(RACKET_GROUP)
        for racket in rackets:
            body = racket.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            y = position.get_y()
            
            position = position.add(velocity)

            if y < 0:
                position = Point(position.get_x(), 0)
            elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
                position = Point( position.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
                
            body.set_position(position)
        