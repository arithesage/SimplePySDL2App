from ctypes import byref

# SDL2 Classes
from sdl2 import SDL_Color as Color
from sdl2 import SDL_Event as Event
from sdl2 import SDL_Window as Window
from sdl2 import SDL_Renderer as Renderer

# SDL2 functions
from sdl2 import SDL_CreateRenderer, SDL_CreateTextureFromSurface,\
                 SDL_CreateWindow, SDL_DestroyRenderer, SDL_DestroyTexture, \
                 SDL_DestroyWindow, SDL_GetError, SDL_ShowWindow, SDL_Init, \
                 SDL_PollEvent, SDL_Quit, SDL_Rect, SDL_RenderClear, \
                 SDL_RenderPresent, SDL_Surface, SDL_Texture


# SDL2 drawing functions
from sdl2 import SDL_RenderCopy, SDL_RenderDrawLine, SDL_RenderDrawLineF, \
                 SDL_RenderDrawRect, SDL_SetRenderDrawColor

# SDL2 constants
# Systems
from sdl2 import SDL_INIT_AUDIO, SDL_INIT_GAMECONTROLLER, \
                 SDL_INIT_VIDEO

# Window flags    
from sdl2 import SDL_WINDOW_SHOWN, SDL_WINDOW_OPENGL, SDL_WINDOW_RESIZABLE, \
                 SDL_WINDOW_VULKAN, SDL_WINDOWPOS_CENTERED
                 

# Renderer flags
from sdl2 import SDL_RENDERER_ACCELERATED, SDL_RENDERER_PRESENTVSYNC, \
                 SDL_RENDERER_SOFTWARE

# SD2L Events
from sdl2.events import SDL_QUIT as SDL_QUIT_EVENT

# SDL_Image functions
from sdl2.sdlimage import IMG_GetError, IMG_Init, IMG_Load, IMG_LoadTexture, \
                          IMG_Quit

# SDL_Image constants
from sdl2.sdlimage import IMG_INIT_JPG, IMG_INIT_PNG


from utils import type_of
from utils import file_exists, make_path
from utils import print_va
from utils import str_empty



class SDL2App:
    class DEFAULTS:
        CLEAR_COLOR = Color (0, 0, 0, 255)
        IMAGE_FORMATS = IMG_INIT_JPG | IMG_INIT_PNG

        RENDERER_FLAGS = SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC

        SYSTEMS_FLAGS =  SDL_INIT_VIDEO | SDL_INIT_AUDIO | \
                         SDL_INIT_GAMECONTROLLER
        
        WINDOW_FLAGS = SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE

        ALL_FLAGS = SYSTEMS_FLAGS | WINDOW_FLAGS | \
                    RENDERER_FLAGS
        
        RESOURCES_PATH = make_path ("./res")
        WINDOW_TITLE = "Hello world!"
        WINDOW_SIZE = (640, 480)
        WINDOW_POSITION = (SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED)

        def __init__(self) -> None:
            pass


    def __init__(self, resources_path: str = DEFAULTS.RESOURCES_PATH,
                 app_name: str = DEFAULTS.WINDOW_TITLE,
                 window_size = DEFAULTS.WINDOW_SIZE,
                 system_flags = DEFAULTS.SYSTEMS_FLAGS,
                 window_flags = DEFAULTS.WINDOW_FLAGS,
                 renderer_flags = DEFAULTS.RENDERER_FLAGS) -> None:
        
        """
        Creates the SDL application and window.

        You can pass any extra flag you want to the ones set by default.        

        ATTENTION: The app already makes use of hardware acceleration
                   (and has VSYNC enabled).

                   Add the SDL_WINDOW_OPENGL flag ONLY if you want to
                   manipulate the OpenGL context.
        """

        self.__resources = resources_path
        self.__running = False        

        if not self.__sdl_init (system_flags):
            print ("ERROR: Failed initializing SDL.")
            return None
        
        self.__create_window (app_name,
                              SDL2App.DEFAULTS.WINDOW_POSITION[0],
                              SDL2App.DEFAULTS.WINDOW_POSITION[1],
                              window_size[0],
                              window_size[1],
                              window_flags,
                              renderer_flags)
        
        self.on_init ()


    def __create_window (self, title: str, x: int, y: int, width: int,\
                         height: int, window_flags, renderer_flags) -> None:
        
        self.__window = SDL_CreateWindow (title.encode(), x, y, 
                                          width, height, 
                                          window_flags)

        self.__renderer = SDL_CreateRenderer (self.__window,
                                              -1,
                                              renderer_flags)
        
        self.__renderer.color = SDL2App.DEFAULTS.CLEAR_COLOR
        
        SDL_ShowWindow (self.__window)


    def on_init (self) -> None:
        pass


    def on_render (self) -> None:
        pass


    def on_start (self) -> None:
        pass


    def on_quit (self) -> None:
        pass    


    def resources (self) -> str:
        return self.__resources
    

    def running (self) -> bool:
        return self.__running
    

    def __sdl_init (self, system_flags) -> bool:
        SDL_Init (system_flags)

        error = SDL_GetError().decode()

        if not str_empty (error):
            print (error)
            return False

        IMG_Init (SDL2App.DEFAULTS.IMAGE_FORMATS)

        if (IMG_Init (0) != SDL2App.DEFAULTS.IMAGE_FORMATS):
            error = IMG_GetError ()
            print (error)
            return False        
        
        return True


    def start (self) -> None:
        self.__running = True
        self.on_start ()
        
        event = Event ()

        while self.running ():
            SDL_PollEvent (byref (event))
            
            if (event != None):
                if (event.type == SDL_QUIT_EVENT):
                    self.__running = False
                    break

            self.update ()
            self.render ()

        self.__shutdown ()


    def __shutdown (self) -> None:
        self.on_quit ()

        self.__asset_store.destroy ()

        SDL_DestroyRenderer (self.__renderer)
        SDL_DestroyWindow (self.__window)
        
        IMG_Quit ()
        SDL_Quit ()


    def update (self) -> None:
        pass


    def render (self) -> None:
        SDL_RenderClear (self.__renderer)

        self.on_render ()

        SDL_RenderPresent (self.__renderer)

    