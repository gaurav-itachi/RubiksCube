'''
This module provides the base classes for basic 
model-view-controller architecture.

author : Gaurav Sharma
handle : gaurav_itachi
email : gaurav.itachi@gmail.com

last edited : 17 Jun 2018

'''


from abc import ABC,abstractmethod

class Model(ABC):
	#########################
	# 
	#
	#########################

	def __init__(self):
		self._counter = 0
		self._observers = set([])
		print("model")
		super().__init__()

	def attach(self,observer):
		self._observers.add(observer)
		
	def dettach(self,observer):
		self._observers.remove(observer)
		
	def notify(self):
		#notify all observers of the change
		for obs in list(self._observers):
			obs.update()


class Observer(ABC):
	def __init__(self):
		super().__init__()
		pass

	@abstractmethod
	def update(self):
		pass

class View(Observer):
	def __init__(self,model):
		self.model = model
		
		print("view")
		super().__init__()
		pass

	@abstractmethod
	def draw(self):
		pass

	@abstractmethod
	def initialise(self):
		pass
	


class Controller(Observer):
	def __init__(self,model,view):
		self.model = model
		self.view = view
		print("controller")
		super().__init__()
		pass
