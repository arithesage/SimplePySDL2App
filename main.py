#!/usr/bin/env python

import sys

from sdl2app import *
from entity2d import Entity2D



class Test (SDL2App):
    sprite = None

    def __init__(self,
                 resources_path: str = SDL2App.DEFAULTS.RESOURCES_PATH, 
                 app_name: str = SDL2App.DEFAULTS.WINDOW_TITLE,
                 window_size = SDL2App.DEFAULTS.WINDOW_SIZE, 
                 system_flags = SDL2App.DEFAULTS.SYSTEMS_FLAGS,
                 window_flags = SDL2App.DEFAULTS.WINDOW_FLAGS,
                 renderer_flags = SDL2App.DEFAULTS.RENDERER_FLAGS) -> None:
        
        super().__init__(resources_path, 
                         app_name, 
                         window_size, 
                         system_flags, 
                         window_flags, 
                         renderer_flags)
        
        self.graphic = self.load_graphic ("graphics/sprite.jpg")
        self.sprite = None
        
    def on_start(self):
        super().on_start()        
        
        if (self.graphic != None):
            self.sprite = Entity2D (self.graphic)

    def on_render(self) -> None:
        super().on_render()    
        self.render_entity2d (self.sprite)

        
        

if __name__ == "__main__":
    argv = sys.argv
    args = len (argv[1:])

    test_app = Test ("./res")
    test_app.start()

