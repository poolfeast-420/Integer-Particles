from multiprocessing import Process, Pipe
from Physics import World, Particle
from Output import Terminal_Output
from random import randint as random_integer

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Make up some shit to simulate
particle_amount = 100
random_plane = [Particle(X_position=random_integer(10, 999), Y_position=random_integer(10, 999), X_velocity=random_integer(-10, 10), Y_velocity=random_integer(-10, 10)) for count in range(particle_amount)]
logger.info('Created plane with %s particles', particle_amount)

# Make some pipe thing
recieving, sending = Pipe(duplex=False)

Jacks_sweet_thread = World(random_plane, sending)
some_grahics_crap = Terminal_Output(recieving)
input('Press enter to start/stop')
Jacks_sweet_thread.start()
some_grahics_crap.start()
input()
Jacks_sweet_thread.terminate()
some_grahics_crap.terminate()