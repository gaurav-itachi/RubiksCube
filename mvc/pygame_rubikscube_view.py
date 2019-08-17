
from mvc.pygame_mvc import pygame_view as View
import math
import pygame
from pygame.locals import *
from PIL import Image



class view(View):
	def __init__(self,model):
		super().__init__(model)
		pygame.font.init()
		pass

	def set_screen_size(self):
		self.SCREEN_SIZE = (1200,600)


	# draws the content from self.draw_content
	def draw(self):
		for draw_object in self.draw_content:
			if(draw_object['type']=='rect'):
				self.draw_rect(draw_object)
			elif (draw_object['type']=='button'):
				self.draw_button(draw_object)
			# print(draw_object)
		pass

	def draw_rect(self,draw_object):
		pygame.draw.rect(self.screen,draw_object['color'],Rect(draw_object['x'],draw_object['y'],draw_object['width'],draw_object['height']),draw_object['boundary'])
		if(draw_object['outline']):
			pygame.draw.rect(self.screen,draw_object['outline_color'],Rect(draw_object['x'],draw_object['y'],draw_object['width'],draw_object['height']),draw_object['outline_boundary'])
		pass

	def draw_button(self,draw_object):
		pygame.draw.rect(self.screen,draw_object['color'],Rect(draw_object['x'],draw_object['y'],draw_object['width'],draw_object['height']),draw_object['boundary'])
		font = pygame.font.SysFont('arial',18)
		text_surface = font.render(draw_object['text'],False,(0,0,0))
		self.screen.blit(text_surface,(draw_object['x']+3,draw_object['y']))
		# print(pygame.font.get_fonts())