#!/usr/bin/env python

import rvo2

sim = rvo2.PyRVOSimulator(1/60., 1.5, 5, 1.5, 2, 0.4, 2)
# https://gamma.cs.unc.edu/RVO2/documentation/2.0/class_r_v_o_1_1_r_v_o_simulator.html#ab9bd4b4412c7107bdd8bd57d980947b2

# Pass either just the position (the other parameters then use
# the default values passed to the PyRVOSimulator constructor),
# or pass all available parameters.
a0 = sim.addAgent((0, 0))
a1 = sim.addAgent((1, 0))
a2 = sim.addAgent((1, 1))
a3 = sim.addAgent((0, 1), 1.5, 5, 1.5, 2, 0.4, 2, (0, 0))

print('a0: ')
print(a3)

# Obstacles are also supported.
o1 = sim.addObstacle([(0.1, 0.1), (-0.1, 0.1), (-0.1, -0.1)])
sim.processObstacles()

sim.setAgentPrefVelocity(a0, (1, 1))
sim.setAgentPrefVelocity(a1, (-1, 1))
sim.setAgentPrefVelocity(a2, (-1, -1))
sim.setAgentPrefVelocity(a3, (1, -1))

# print('Simulation has %i agents and %i obstacle vertices in it.' %
#       (sim.getNumAgents(), sim.getNumObstacleVertices()))

# print('Running simulation')
positions = 0

for step in range(10):
	sim.doStep()

	positions = ['%5.3f\t%5.3f\t' % sim.getAgentPosition(agent_no)
	             for agent_no in (a0, a1, a2, a3)]
	print('%2i\t%.3f\t%s' % (step, sim.getGlobalTime(), '  '.join(positions)))
	# print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))
	# pox, poy = sim.getAgentPosition(a1)
	# print('%5.3f %5.3f' % (pox, poy))

# print("%s" %''.join(positions))
