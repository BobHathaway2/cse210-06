from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        rackets = []
        rackets = cast.get_actors(RACKET_GROUP)
        for racket in rackets:
            if self._keyboard_service.is_key_down(LEFT): 
                racket.swing_left()
            elif self._keyboard_service.is_key_down(RIGHT): 
                racket.swing_right()  
            else: 
                racket.stop_moving()        