from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

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
            stats[1].add_points
            callback.on_next(TRY_AGAIN) 

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            stats = cast.get_actors(STATS_GROUP)
            stats[0].add_points(1)
            callback.on_next(TRY_AGAIN) 

        if y <= (FIELD_TOP):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
  