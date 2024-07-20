#!/usr/bin/env python

import sys

from sdl2app import SDL2App




class Test (SDL2App):
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
        
    def on_start(self):
        super().on_start()

        

if __name__ == "__main__":
    argv = sys.argv
    args = len (argv[1:])

    test_app = Test ("./res")
    test_app.start()

