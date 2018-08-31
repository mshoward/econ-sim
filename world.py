"""
defines the world in which agents act.
location described as cells on a sphere
x_ang is [0-359], y_ang is the same

assume spheres aren't spherical and thus curvature doesn't exist.
todo: stop assuming that.

"""

from cell import cell


class world:
    worldmap = {}
    
    def __init__(self):
        world.worldmap
