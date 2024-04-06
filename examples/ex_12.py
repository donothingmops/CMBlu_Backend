import sys
import numpy as np
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from fastStruct.fem.system import SystemElements

ss = SystemElements()
ss.add_element([[0, 0], [2, 0]])
ss.add_element([4, 0])
ss.add_element([6, 0])
ss.add_support_fixed([1, 4])

ss.moment_load([2, 3], [20, -20])

if __name__ == "__main__":
    ss.solve()
    print()
    ss.show_structure()
"""     ss.show_displacement()
    ss.show_bending_moment()
    ss.show_shear_force() """

    #ss.post_processor.report_max_bending_moments()  # Assuming postprocess is an instance of SystemLevel in SystemElements
"""     ss.post_processor.report_max_shear_forces()
    ss.post_processor.report_max_displacements()
    ss.post_processor.report_max_axial_forces() """
    

