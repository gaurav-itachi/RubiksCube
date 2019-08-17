'''
driver progam for a particular mvc architecture

author : Gaurav Sharma
handle : gaurav_itachi
email : gaurav.itachi@gmail.com

last edited : 19 Jun 2018
'''

from mvc.pygame_rubikscube_controller import controller as Controller
from mvc.pygame_rubikscube_view import view as View
from models.rubikscube_model import model as Model

def run():
	model = Model()
	view = View(model)
	controller = Controller(model,view)

	controller.initialise()
	while(True):
		is_terminated = controller.run()

		if(is_terminated):
			break

if __name__ == "__main__":
	run() 

