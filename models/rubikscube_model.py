'''
This module provides the model for the sytem in which entities 
interact with environment and evolve .

author : Gaurav Sharma
handle : gaurav_itachi
email : gaurav.itachi@gmail.com

last edited : 19 Jun 2018

'''

from math import *

from PIL import Image

import numpy as np
import cv2
import matplotlib.pyplot as plt
import json 
import io


from mvc.mvc import Model


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
ORANGE = (255,166,0)
MAGENTA = (255,0,255)


FACE_WIDTH = 100
FACE_HEIGTH = 100
MARGIN = 10

class model(Model):
	def __init__(self):
		super().__init__()
		self.rubikscube = RubiksCube()
		pass

	def get_draw_content(self):
		return self.rubikscube.get_draw_content()
		pass

	def make_move(self,move):
		self.rubikscube.make_move(move)

	def update(self,time_passed):
		
		pass

class RubiksCube():
	def __init__(self):
		self.faces = [
			CubeFace(ORANGE,0,FACE_WIDTH,0,FACE_WIDTH,FACE_HEIGTH),
			CubeFace(BLUE,1,0,FACE_HEIGTH,FACE_WIDTH,FACE_HEIGTH),
			CubeFace(GREEN,2,FACE_WIDTH,FACE_HEIGTH,FACE_WIDTH,FACE_HEIGTH),
			CubeFace(MAGENTA,3,FACE_WIDTH*2,FACE_HEIGTH,FACE_WIDTH,FACE_HEIGTH),
			CubeFace(RED,4,FACE_WIDTH,FACE_HEIGTH*2,FACE_WIDTH,FACE_HEIGTH),
			CubeFace(YELLOW,5,FACE_WIDTH,FACE_HEIGTH*3,FACE_WIDTH,FACE_HEIGTH),
		]
		
	def get_draw_content(self):
		draw_content=[]
		for face in self.faces:
			draw_content.extend(face.get_draw_content())
		return draw_content

	def make_move(self,move):
		switcher = {
			'Left':self.Left,
			'LeftReverse':self.LeftReverse,
			'Right':self.Right,
			'RightReverse':self.RightReverse,
			'Top':self.Top,
			'TopReverse':self.TopReverse,
			'Bottom':self.Bottom,
			'BottomReverse':self.BottomReverse,
			'Front':self.Front,
			'FrontReverse':self.FrontReverse,
			'Back':self.Back,
			'BackReverse':self.BackReverse
		}
		switcher.get(move,lambda : print("Invalid Move"))()




	def Left(self):
		tmp = self.faces[0].cubelets[:,0].copy()
		self.faces[0].cubelets[:,0] = self.faces[2].cubelets[:,0]
		self.faces[2].cubelets[:,0] = self.faces[4].cubelets[:,0]
		self.faces[4].cubelets[:,0] = self.faces[5].cubelets[:,0]
		self.faces[5].cubelets[:,0] = tmp

		
	def LeftReverse(self):
		tmp = self.faces[0].cubelets[:,0].copy()
		self.faces[0].cubelets[:,0] = self.faces[5].cubelets[:,0]
		self.faces[5].cubelets[:,0] = self.faces[4].cubelets[:,0]
		self.faces[4].cubelets[:,0] = self.faces[2].cubelets[:,0]
		self.faces[2].cubelets[:,0] = tmp
		pass
	def Right(self):
		tmp = self.faces[0].cubelets[:,2].copy()
		self.faces[0].cubelets[:,2] = self.faces[2].cubelets[:,2]
		self.faces[2].cubelets[:,2] = self.faces[4].cubelets[:,2]
		self.faces[4].cubelets[:,2] = self.faces[5].cubelets[:,2]
		self.faces[5].cubelets[:,2] = tmp
		pass
	def RightReverse(self):
		tmp = self.faces[0].cubelets[:,2].copy()
		self.faces[0].cubelets[:,2] = self.faces[5].cubelets[:,2]
		self.faces[5].cubelets[:,2] = self.faces[4].cubelets[:,2]
		self.faces[4].cubelets[:,2] = self.faces[2].cubelets[:,2]
		self.faces[2].cubelets[:,2] = tmp
		pass
	def Top(self):
		tmp = self.faces[0].cubelets[2,:].reshape(self.faces[3].cubelets[:,0].shape).copy()
		self.faces[0].cubelets[2,:] = self.faces[1].cubelets[:,2].reshape(self.faces[0].cubelets[2,:].shape)
		self.faces[1].cubelets[:,2] = self.faces[4].cubelets[0,:].reshape(self.faces[1].cubelets[:,2].shape)
		self.faces[4].cubelets[0,:] = self.faces[3].cubelets[:,0].reshape(self.faces[4].cubelets[0,:].shape)
		self.faces[3].cubelets[:,0] = tmp
		pass
	def TopReverse(self):
		tmp = self.faces[0].cubelets[2,:].reshape(self.faces[1].cubelets[:,2].shape).copy()
		self.faces[0].cubelets[2,:] = self.faces[3].cubelets[:,0].reshape(self.faces[0].cubelets[2,:].shape)
		self.faces[3].cubelets[:,0] = self.faces[4].cubelets[0,:].reshape(self.faces[3].cubelets[:,0].shape)
		self.faces[4].cubelets[0,:] = self.faces[1].cubelets[:,2].reshape(self.faces[4].cubelets[0,:].shape)
		self.faces[1].cubelets[:,2] = tmp
		pass
	def Bottom(self):
		tmp = self.faces[1].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape).copy()
		self.faces[1].cubelets[2,:] = self.faces[5].cubelets[0,:].reshape(self.faces[1].cubelets[2,:].shape)
		self.faces[5].cubelets[0,:] = self.faces[3].cubelets[2,:].reshape(self.faces[5].cubelets[0,:].shape)
		self.faces[3].cubelets[2,:] = self.faces[2].cubelets[2,:].reshape(self.faces[3].cubelets[2,:].shape)
		self.faces[2].cubelets[2,:] = tmp
		# tmp = self.faces[0].cubelets[0,:].reshape(self.faces[1].cubelets[:,0].shape).copy()
		# self.faces[0].cubelets[0,:] = self.faces[3].cubelets[:,2].reshape(self.faces[0].cubelets[0,:].shape)
		# self.faces[3].cubelets[:,2] = self.faces[4].cubelets[2,:].reshape(self.faces[3].cubelets[:,2].shape)
		# self.faces[4].cubelets[2,:] = self.faces[1].cubelets[:,0].reshape(self.faces[4].cubelets[2,:].shape)
		# self.faces[1].cubelets[:,0] = tmp
		pass
	def BottomReverse(self):
		tmp = self.faces[1].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape).copy()
		self.faces[1].cubelets[2,:] = self.faces[2].cubelets[2,:].reshape(self.faces[1].cubelets[2,:].shape)
		self.faces[2].cubelets[2,:] = self.faces[3].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape)
		self.faces[3].cubelets[2,:] = self.faces[5].cubelets[0,:].reshape(self.faces[3].cubelets[2,:].shape)	
		self.faces[5].cubelets[0,:] =  tmp
		# tmp = self.faces[0].cubelets[0,:].reshape(self.faces[3].cubelets[:,2].shape).copy()
		# self.faces[0].cubelets[0,:] = self.faces[1].cubelets[:,0].reshape(self.faces[0].cubelets[0,:].shape)
		# self.faces[1].cubelets[:,0] = self.faces[4].cubelets[2,:].reshape(self.faces[1].cubelets[:,0].shape)
		# self.faces[4].cubelets[2,:] = self.faces[3].cubelets[:,2].reshape(self.faces[4].cubelets[2,:].shape)
		# self.faces[3].cubelets[:,2] = tmp
		pass
	def Front(self):
		tmp = self.faces[0].cubelets[0,:].reshape(self.faces[1].cubelets[:,0].shape).copy()
		self.faces[0].cubelets[0,:] = self.faces[3].cubelets[:,2].reshape(self.faces[0].cubelets[0,:].shape)
		self.faces[3].cubelets[:,2] = self.faces[4].cubelets[2,:].reshape(self.faces[3].cubelets[:,2].shape)
		self.faces[4].cubelets[2,:] = self.faces[1].cubelets[:,0].reshape(self.faces[4].cubelets[2,:].shape)
		self.faces[1].cubelets[:,0] = tmp
		# tmp = self.faces[1].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape).copy()
		# self.faces[1].cubelets[2,:] = self.faces[5].cubelets[0,:].reshape(self.faces[1].cubelets[2,:].shape)
		# self.faces[5].cubelets[0,:] = self.faces[3].cubelets[2,:].reshape(self.faces[5].cubelets[0,:].shape)
		# self.faces[3].cubelets[2,:] = self.faces[2].cubelets[2,:].reshape(self.faces[3].cubelets[2,:].shape)
		# self.faces[2].cubelets[2,:] = tmp
		pass
	def FrontReverse(self):
		tmp = self.faces[0].cubelets[0,:].reshape(self.faces[3].cubelets[:,2].shape).copy()
		self.faces[0].cubelets[0,:] = self.faces[1].cubelets[:,0].reshape(self.faces[0].cubelets[0,:].shape)
		self.faces[1].cubelets[:,0] = self.faces[4].cubelets[2,:].reshape(self.faces[1].cubelets[:,0].shape)
		self.faces[4].cubelets[2,:] = self.faces[3].cubelets[:,2].reshape(self.faces[4].cubelets[2,:].shape)
		self.faces[3].cubelets[:,2] = tmp
		# tmp = self.faces[1].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape).copy()
		# self.faces[1].cubelets[2,:] = self.faces[2].cubelets[2,:].reshape(self.faces[1].cubelets[2,:].shape)
		# self.faces[2].cubelets[2,:] = self.faces[3].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape)
		# self.faces[3].cubelets[2,:] = self.faces[5].cubelets[0,:].reshape(self.faces[3].cubelets[2,:].shape)	
		# self.faces[5].cubelets[0,:] =  tmp
		pass
	def Back(self):
		tmp = self.faces[1].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape).copy()
		self.faces[1].cubelets[2,:] = self.faces[2].cubelets[2,:].reshape(self.faces[1].cubelets[2,:].shape)
		self.faces[2].cubelets[2,:] = self.faces[3].cubelets[2,:].reshape(self.faces[2].cubelets[2,:].shape)
		self.faces[3].cubelets[2,:] = self.faces[5].cubelets[0,:].reshape(self.faces[3].cubelets[2,:].shape)	
		self.faces[5].cubelets[0,:] =  tmp
		pass
	def BackReverse(self):
		pass

class CubeletColor():
	def __init__(self,color):
		self.color = color

	def get_color(self):
		return self.color
	def __str__(self):
		return str(self.color)
	def __repr__(self):
		return str(self.color)

class CubeFace():
	def __init__(self,color,id=-1,x=0,y=0,width=100,height=100):
		self.id = id
		self.set_default_pos(x+MARGIN,y+MARGIN,width,height)
		a = [[ CubeletColor(color) ]*3]*3
		self.cubelets = np.matrix(a)
		pass

	def set_default_pos(self,x=0,y=0,width=100,height=100):
		self.posx=x
		self.posy=y
		self.width = width
		self.height = height

	def get_draw_content(self):
		return self.get_box_view(self.posx,self.posy,self.width,self.height)

	def get_box_view(self,x=0,y=0,width=100,height=100):
		draw_cubelets= []
		cubelet_x = x
		cubelet_y = y
		cubelet_width = int(width / 3)
		cubelet_height = int(height / 3)
		outline_boundary = max(1,int(min(cubelet_height,cubelet_width) / 10))

		for i in range(0,self.cubelets.shape[0]) :
			for j in range(0,self.cubelets.shape[1])  :
				draw_cubelets.append({
					'type':'rect',
					'x':cubelet_x,
					'y':cubelet_y,
					'width':cubelet_width,
					'height':cubelet_height,
					'outline':True,
					'outline_color':BLACK,
					'outline_boundary':outline_boundary,
					'boundary':0,
					'color':self.cubelets[i,j].get_color()
				})
				cubelet_x = cubelet_x + cubelet_width
			cubelet_x = x
			cubelet_y = cubelet_y + cubelet_height
		return draw_cubelets

