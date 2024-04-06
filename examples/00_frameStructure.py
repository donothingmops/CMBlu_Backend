import sys, math
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from fastStruct.fem.system import SystemElements
import numpy as np



ss = SystemElements(EA=5000)
ss.add_truss_element(location=[[0, 0], [0, 5]])
ss.add_truss_element(location=[[0, 5], [5, 5]])
ss.add_truss_element(location=[[5, 5], [5, 0]])
ss.add_truss_element(location=[[0, 0], [5, 5]], EA=5000 * math.sqrt(2))
ss.add_truss_element(location=[[5, 0], [0, 5]], EA=5000 * math.sqrt(2))

""" ss.add_support_hinged(node_id=1)
ss.add_support_hinged(node_id=4) """
ss.add_support_fixed(node_id=1)
ss.add_support_fixed(node_id=4)

ss.point_load(Fx=10, node_id=2)

ss.solve()


ss.show_results()
ss.show_structure()
ss.show_reaction_force()
ss.show_axial_force()
ss.show_displacement(factor=10)
print(np.argmin(ss.get_element_result_range('moment')))