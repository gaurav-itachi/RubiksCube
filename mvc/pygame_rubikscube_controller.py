

from mvc.pygame_mvc import pygame_controller as Controller
import math
import pygame
from pygame.locals import *
from PIL import Image


class controller(Controller):
	def __init__(self,model,view):
		super().__init__(model,view)
		pass


	def update(self):
		super().update()
		self.handle_events()
		pass

	def handle_events(self):
		if(self.pressed_key_history.get(K_UP,False)):
			print("Key UP pressed")
			self.model.make_move('Left')
			self.view.update()
			self.pressed_key_history.update({K_UP:False})
	
		if(self.pressed_key_history.get(K_DOWN,False)):
			print("Key DOWN pressed")
			self.model.make_move('LeftReverse')
			self.view.update()
			self.pressed_key_history.update({K_DOWN:False})
		
		if(self.pressed_key_history.get(K_LEFT,False)):
			print("Key K_LEFT pressed")
			self.model.make_move('Right')
			self.view.update()
			self.pressed_key_history.update({K_LEFT:False})
		
		if(self.pressed_key_history.get(K_RIGHT,False)):
			print("Key K_RIGHT pressed")
			self.model.make_move('RightReverse')
			self.view.update()
			self.pressed_key_history.update({K_RIGHT:False})
	
		if(self.pressed_key_history.get('LEFT_MOUSE_CLICK',False)):
			print("LeftMouse click pressed")
			pos = self.dict.get('mouse_pos',None)
			if(pos != None):
				self.model.check_click(pos)
				self.view.update()
			self.pressed_key_history.update({'LEFT_MOUSE_CLICK':False})
			

