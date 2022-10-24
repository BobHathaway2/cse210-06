from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):
    """ handles collisions with each border, top, bottom, left and right"""
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        if x < FIELD_LEFT:
            stats = cast.get_actors(STATS_GROUP)
            callback.on_next(GAME_OVER) 
            self._audio_service.play_sound(over_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            callback.on_next(GAME_OVER) 
            self._audio_service.play_sound(over_sound)

        if y <= (FIELD_TOP):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
  