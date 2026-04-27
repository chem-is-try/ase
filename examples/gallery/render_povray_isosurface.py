"""

Isosurface with povray
======================

"""

import numpy as np

from ase.build import bulk
from ase.io import write

spin_cut_off = 0.4
density_cut_off = 0.15

rotation = '24x, 34y, 14z'

atoms = bulk('Au', cubic=True) * (2, 2, 2)

# generate dummy volumetric data
axis = np.linspace(-1, 1, 100)
X, Y, Z = np.meshgrid(axis, axis, axis)
isodata = np.exp(-0.5 * (X**2 + 2 * Y**2 + 3 * Z**2))

# Make a gaussian cube file.
# write('test.cube', atoms)

povray_settings = {
    # For povray files only
    'pause': False,  # Pause when done rendering (only if display)
    'transparent': False,  # Transparent background
    'canvas_width': None,  # Width of canvas in pixels
    'canvas_height': 1024,  # Height of canvas in pixels
    'camera_dist': 25.0,  # Distance from camera to front atom
    'camera_type': 'orthographic angle 35',  # 'perspective angle 20'
    'textures': len(atoms) * ['ase3'],
}

# some more options:
# 'image_plane'  : None,  # Distance from front atom to image plane
#                         # (focal depth for perspective)
# 'camera_type'  : 'perspective', # perspective, ultra_wide_angle
# 'point_lights' : [],             # [[loc1, color1], [loc2, color2],...]
# 'area_light'   : [(2., 3., 40.) ,# location
#                   'White',       # color
#                   .7, .7, 3, 3], # width, height, Nlamps_x, Nlamps_y
# 'background'   : 'White',        # color
# 'textures'     : tex, # Length of atoms list of texture names
# 'celllinewidth': 0.05, # Radius of the cylinders representing the cell

generic_projection_settings = {
    'rotation': rotation,
    'radii': atoms.positions.shape[0] * [0.3],
    'show_unit_cell': 1,
}

# write returns a renderer object which needs to have the render method called

write(
    'NiO_marching_cubes1.pov',
    atoms,
    **generic_projection_settings,
    povray_settings=povray_settings,
    isosurface_data=dict(density_grid=isodata, cut_off=density_cut_off),
).render()
