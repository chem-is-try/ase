=====
Tools
=====

.. _gui-tools graphs:
Graphs
------

For graphing different quantities for a given trajectory. ASE uses
matplotlib as a backend, allowing some manipulation of the generated plot
and for the plot to be saved to a file.

The :guilabel:`Graphs` window requires an instruction string that controls
what is plotted. The following expressions can be used to create the 
instructions:

================ ==================================================
 Symbol          Interpretation
================ ==================================================
e                total energy
epot             potential energy
ekin             kinetic energy
fmax             maximum force
fave             average force
d(n1,n2)         distance between two atoms
R[n,0-2]         position of atom number n
i                current image number
E[i]             energy of image number i
F[n,0-2]         force on atom number n
M[n]             magnetic moment of atom number n
A[0-2,0-2]       unit-cell basis vectors
s                path length
a(n1,n2,n3)      angle between atoms n1, n2 and n3, centered on n2
dih(n1,n2,n3,n4) dihedral angle between n1, n2, n3, and n4
T                temperature (requires velocity)
================ ==================================================

Variables should be separated by commas. The window presents two
:guilabel:`Plot` buttons. The first (``x, y1, y2, ...``) places the first
variable in the list as the x-axis. The other (``y1, y2, ...``) plots all
variables on the y-axis and uses the current image number as the x-axis.

This example plots the energy and the maximal force for each image i (e.g.
to help in investigating the convergence properties for geometry
relaxations):

::

  i, e-min(E), fmax


Movie
-----

Allows to play the current trajectory as a movie using a number of
different settings. Default duration is 5 s.


Constraints
-----------

Allows to set (or remove) constraints based on the currently selected atoms.


Render scene
------------

(Currently disabled)

Graphical interface to the ASE povray interface, ideally it requires
that povray is installed on your computer to function, but it also can
be used just to export the complete set of povray files.

The texture of each atom is adjustable: The default texture is applied
to all atoms, but then additional textures can be defined based on
selections (``Create new texture from current selection``). These can
be obtained either from selecting atoms by hand or by defining a
selection with a boolean expression, for example ``Z==6 and x>5 and
y<0`` will select all carbons with coordinates x>5 and y<0. The
available commands are listed in the ``Help on textures`` window.

A movie-making mode (``render all N frames``) is also available. After
rendering, the frames can be stitched together using the ``convert``
unix program e.g.

::

    localhost:doc hanke$ convert -delay 4.17 temp.*.png temp.gif

For this particular application it might be a good idea to use a white
background instead of the default transparent option.


Move atoms
----------

Allows selected atoms to be moved using the arrow keys. The direction
is always parallel to the plane of the screen. Two possible movements
are available: Just pressing the arrow keys will move by 0.1
Angstrom, ``shift`` + arrow keys will move by 0.01 Angstrom.


NEB plot
--------

Assuming you have opened a series of images corresponding to a NEB
trajectory, use :menuselection:`Tools --> NEB` to plot the energy barrier.

.. ::

..   $ ase gui --interpolate 3 initial.xyz final.xyz -o interpolated_path.traj
