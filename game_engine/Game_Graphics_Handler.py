import sys
import pygame as pg
import os

#surface = pygame.image.load('foo.png'), adds a surface
#display.flip() re-renders the scene
#rectangle = Rect(10, 20, 30, 30)
#pygame.mouse.get_pos(), checks mouse pos at the moment you call the function

class GraphicsHandler():
    def __init__(self, entities_to_render, main_surface):
        self.entities_to_render = entities_to_render        
        self.scene_width = main_surface.get_width()
        self.scene_height = main_surface.get_height()
        image_path = os.path.join("game_engine", "images", "background.jpg")
        main_surface.fill('white')
        self.background = pg.image.load(image_path).convert()
        self.screen = main_surface


    def render_Scene(self):
        self.background = pg.transform.scale(self.background, (self.scene_width, self.scene_width))
        self.screen.blit(self.background, (0,0))

        for entity in self.entities_to_render:
            if entity.image_path:
                path = os.path.join("game_engine", "images", entity.image_path)
                image = pg.image.load(path).convert_alpha()
                image = pg.transform.scale(image, (entity.width, entity.height))
                self.screen.blit(image, (entity.x, entity.y))
            else:
                if entity.type == 5: #entity = menu
                    for button in entity.buttons:
                        button.draw()
                else: 
                    pg.draw.rect(self.screen, (0, 0, 0), (entity.x, entity.y, entity.width, entity.height))
                
        pg.display.update()
    
    def render_menu(entity):
        for button in entity.buttons:
            button.draw()