import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from fastStruct.fem.system import SystemElements

ss = SystemElements(EI=5e3, EA=1e5)

ss.add_element([0, 10])

ss.add_support_hinged(1)
ss.add_support_roll(2, 1)

ss.point_load(2, Fy=-1)

if __name__ == "__main__":
    ss.solve(geometrical_non_linear=True, discretize_kwargs={"n": 15})
    print(ss.buckling_factor)
    ss.show_displacement()
    ss.show_bending_moment()
    ss.post_processor.report_max_bending_moments()
