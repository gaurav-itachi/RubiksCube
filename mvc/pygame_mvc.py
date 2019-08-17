'''
This module provides the view and controller based on pygame.

author : Gaurav Sharma
handle : gaurav_itachi
email : gaurav.itachi@gmail.com

last edited : 19 Jun 2018

'''





from mvc.mvc import View,Controller
import math
import pygame
from pygame.locals import *
from PIL import Image


class pygame_controller(Controller):
	def __init__(self,model,view):
		super().__init__(model,view)
		self.model.attach(self)
		self.time_passed = 0
		self.pressed_key_history = {}
		pass

	def initialise(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.view.initialise()
		self.view.update()
		
	def run(self):
		##### most imp event detections #######################################
		for event in pygame.event.get():
			if event.type == QUIT:
				return True

		self.handle_key_events()
		self.handle_mouse_events()


		self.time_passed = self.time_passed + self.get_time_passed()
		if(self.time_passed>0.8):
			self.update()
			self.time_passed = 0 

		return False

	def update(self):
		self.model.update(self.time_passed)			
		# self.view.update()
		pass



	def handle_key_events(self):
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_UP]:
			self.pressed_key_history.update({K_UP:True})
			pass
		elif pressed_keys[K_DOWN]:
			self.pressed_key_history.update({K_DOWN:True})
			pass
		
		if pressed_keys[K_LEFT]:
			self.pressed_key_history.update({K_LEFT:True})
			pass
		elif pressed_keys[K_RIGHT]:
			self.pressed_key_history.update({K_RIGHT:True})
			pass

		if pressed_keys[K_q]:
			
			pass
		if pressed_keys[K_a]:
			
			pass
		elif pressed_keys[K_d]:
			
			pass

		if pressed_keys[K_w]:
			
			pass
		elif pressed_keys[K_s]:
			
			pass

		if pressed_keys[K_e]:
			pass
		elif pressed_keys[K_r]:
			pass
		elif pressed_keys[K_f]:
			pass

		if pressed_keys[K_p]:
			pass
		elif pressed_keys[K_o]:
			pass

		
		if pressed_keys[K_KP_PLUS] :
			pass
		elif pressed_keys[K_KP_MINUS]:
			pass

		if pressed_keys[K_KP0]:
			pass
		elif pressed_keys[K_KP1]:
			pass
		elif pressed_keys[K_KP2]:
			pass
		elif pressed_keys[K_KP3]:
			pass
		elif pressed_keys[K_KP4]:
			pass
		elif pressed_keys[K_KP5]:
			pass
		elif pressed_keys[K_KP6]:
			pass
		elif pressed_keys[K_KP7]:
			pass
		elif pressed_keys[K_KP8]:			
			pass
		elif pressed_keys[K_KP9]:
			pass
		
	def handle_mouse_events(self):

		left_m , middle_m, right_m = pygame.mouse.get_pressed()

		if(left_m):
			
			pass

		if(middle_m):
			
			pass
		else :

			pass

		if (right_m):

			pass


	def get_time_passed(self):
		#return time passed in seconds
		time_passed = self.clock.tick()
		time_passed_seconds = time_passed / 1000.
		return time_passed_seconds



class pygame_view(View):
	def __init__(self,model):
		super().__init__(model)
		self.model.attach(self)
		pass

	def initialise(self):
		self.set_screen_size()
		self.screen = pygame.display.set_mode(self.SCREEN_SIZE, 0)
		
	def set_screen_size():
		self.SCREEN_SIZE = (1000,700)

	def update(self):
		self.draw_content = self.model.get_draw_content()
		self.pre_draw()
		self.draw()
		self.post_draw()


	def clear_screen(self):
		self.screen.fill((255, 255, 255))
		pass

	def pre_draw(self):
		self.clear_screen()
		pass

	def draw(self): 
		pass

	def post_draw(self):

		pygame.display.flip()
		pygame.display.update()
		pass

	