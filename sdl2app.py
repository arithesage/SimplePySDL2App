from ctypes import byref
from typing import Tuple

# SDL2 Classes
from sdl2 import SDL_Color as Color
from sdl2 import SDL_Event as Event
from sdl2 import SDL_Window as Window
from sdl2 import SDL_Renderer as Renderer

# SDL2 functions
from sdl2 import SDL_CreateRenderer, SDL_CreateTextureFromSurface,\
                 SDL_CreateWindow, SDL_DestroyRenderer, SDL_DestroyTexture, \
                 SDL_DestroyWindow, SDL_GetError, SDL_ShowWindow, SDL_Init, \
                 SDL_PollEvent, SDL_Quit, SDL_Rect, SDL_FRect, SDL_RenderClear, \
                 SDL_RenderPresent, SDL_Surface, SDL_Texture


# SDL2 drawing functions
from sdl2 import SDL_RenderCopy, SDL_RenderCopyF, SDL_RenderDrawLine, \
                 SDL_RenderDrawLineF, SDL_RenderDrawRect, SDL_SetRenderDrawColor

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

from entity2d import Entity2D
from graphic import Graphic




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
        self.__texture_cache = {}

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


    def __cache_texture (self,
                         graphic: SDL_Surface,
                         graphic_path: str) -> bool:
        """
        Caches a texture if it wasn't already cached.

        'Caching' really means 'uploading to GPU'.

        The idea is, when a sprite is instanced,
        check if it has been cached and only upload texture if
        it wasn't uploaded before.
        """

        if self.__has_cached_texture (graphic_path):
            print_va ("Already cached texture for '$[0]'.", graphic_path)
            return True
                
        texture = SDL_CreateTextureFromSurface (self.__renderer, graphic)
        
        if (texture == None):
            print_va ("ERROR: Failed caching texture for '$[0]'.",
                        graphic_path)
            
            return False
        
        else:
            self.__texture_cache[graphic_path] = texture
            print_va ("Cached texture for '$[0]'.", graphic_path)
            return True    


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


    def __has_cached_texture (self, image_path: str) -> bool:
        return image_path in self.__texture_cache.keys()


    def load_graphic (self, image_path: str) -> Graphic:
        image_path = make_path (self.__resources, image_path)

        if file_exists (image_path):            
            image_data = IMG_Load (image_path.encode())
            
            if (image_data != None):
                loaded_graphic = Graphic (image_path, image_data)
                return loaded_graphic
            
        return None


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

        SDL_DestroyRenderer (self.__renderer)
        SDL_DestroyWindow (self.__window)
        
        IMG_Quit ()
        SDL_Quit ()


    def update (self) -> None:
        pass


    def render_entity2d (self, 
                         entity: Entity2D,
                         width: int = None,
                         height: int = None) -> None:
        """
        Call for rendering 2D entities.

        Width and height are used for rendering only a portion
        of the entity.
        """
        if (entity != None):
            if not entity.sprite().is_cached():
                img_path = entity.sprite().graphic().path()
                surface = entity.sprite().graphic().graphic_data()                                        

                if self.__cache_texture (surface, img_path):
                    entity.sprite().__cached__()

            if entity.sprite().is_cached():                
                entity_x = entity.position().x()
                entity_y = entity.position().y()
                texture = self.__texture_cache[entity.sprite().graphic().path()]
                sprite_width = entity.sprite().width()
                sprite_height = entity.sprite().height()

                if (width == None) or (height == None):
                    src_rect = SDL_Rect (int (entity_x),
                                         int (entity_y),
                                         int (sprite_width),
                                         int (sprite_height))
                else:
                    src_rect = SDL_FRect (entity_x,
                                          entity_y,
                                          width,
                                          height)
                    
                dest_rect = SDL_FRect (entity_x,
                                       entity_y,
                                       sprite_width,
                                       sprite_height)
                
                SDL_RenderCopyF (self.__renderer,
                                 texture,
                                 src_rect,
                                 dest_rect)


    def render (self) -> None:
        SDL_RenderClear (self.__renderer)

        self.on_render ()

        SDL_RenderPresent (self.__renderer)

    