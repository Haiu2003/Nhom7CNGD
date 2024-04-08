import enum
from typing import Tuple
import pygame 

def scale_image(image: pygame.Surface, scale: float) -> pygame.Surface:
    """Resize image by a factor of input arg `scale`."""
    new_dimension: Tuple[int, int] = (
        int(image.get_width() * scale),
        int(image.get_height() * scale),
    )
    return pygame.transform.scale(image, new_dimension)

DIAMOND_BLUE_SPRITE = scale_image (pygame.image.load("assets/items/diamond_blue.png"))
DIAMOND_RED_SPRITE = scale_image (pygame.image.load("assets/items/diamond_red.png"))

class ItemType(enum.Enum):
    DIAMOND_BLUE = 0
    DIAMOND_RED = 1

class Item:
    def __init__ (self, x, y):
        self.x=x, 
        self.y=y,
        self.image: pygame.Surface

        if type == ItemType.DIAMOND_BLUE:
            self.image = DIAMOND_BLUE_SPRITE
        elif type == ItemType.DIAMOND_RED:
            self.image = DIAMOND_RED_SPRITE

  