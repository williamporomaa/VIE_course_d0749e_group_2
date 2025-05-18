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
        self.folder_path = r"chessGame/images"
        image_path = os.path.join(self.folder_path, "background.jpg")
        print(image_path)
        main_surface.fill('white')
        self.background = pg.image.load(image_path).convert()
        self.screen = main_surface
        self.popup = None  # Placeholder for the popup menu
        pg.font.init()
        self.font = pg.font.Font('freesansbold.ttf', 24)


    def render_Scene(self):
        self.background = pg.transform.scale(self.background, (self.scene_width, self.scene_width))
        self.screen.blit(self.background, (0,0))

        for entity in self.entities_to_render:
            if entity.image_path:
                path = os.path.join(entity.image_path)
                image = pg.image.load(path).convert_alpha()
                image = pg.transform.scale(image, (entity.width, entity.height))
                self.screen.blit(image, (entity.x, entity.y))
        if self.popup:
             self.render_menu()
                
        pg.display.update()
    
    def render_menu(self,):
        i = 0
        for text in self.popup.buttons:
                pg.draw.rect(self.screen, 'light gray', [self.popup.x, self.popup.y + self.popup.button_height*i, self.popup.button_width, self.popup.button_height], 0, 5)
                pg.draw.rect(self.screen, 'dark gray', [self.popup.x, self.popup.y + self.popup.button_height*i, self.popup.button_width, self.popup.button_height], 5, 5)
                text2 = self.font.render(text, True, 'black')
                self.screen.blit(text2, (self.popup.x + 15, self.popup.y + self.popup.button_height*i + 7))
                i+=1