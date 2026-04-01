===================================
GUI basics and command line options
===================================

ASE has a built-in graphical user interface (GUI) which can be invoked
from a terminal with the ``ase gui`` subcommand and can read all the
same file formats that the ASE's :func:`~ase.io.read` function
understands, e.g.:

::

  $ ase gui N2Fe110-path.traj

The :ref:`ase-gui` can also be launched directly from a Python
script or interactive session using :func:`ase.visualize.view`.

>>> from ase.visualize import view
>>> atoms = ...
>>> view(atoms)

or

>>> view(atoms, repeat=(3, 3, 2))

The methods above open and modify a copy of the Atoms object. In order
to make direct changes to your atoms, use:

>>> atoms.edit()


Basic controls
--------------

Visualizing a system with ASE's GUI is straight-forward using a regular
mouse. The scroll function allows to change the magnification, the
left mouse button selects atoms, the right mouse button allows to
rotate, and the middle button allows to translate the system on the
screen.

Depending on how many atoms are selected, :ref:`ase-gui` automatically
measures one of several quantities:

================================= ======================================
Selection                         measurement
================================= ======================================
single atom                       position (x,y,z) and chemical symbol
                                  of the atom
two atoms                         interatomic distance and chemical
                                  symbols
three atoms                       internal angles between the atoms and
                                  chemical symbols
four atoms                        dihedral angle, i.e. the angle between
                                  bonds 1-2 and 3-4, and chemical
                                  symbols
more than four atoms              chemical composition (formula) of
                                  selection
================================= ======================================


Selecting a part of a trajectory
--------------------------------

A Python-like syntax for selecting a subset of configurations can be
used.  Instead of the Python syntax ``list[start:stop:step]``, you use
:file:`filename@start:stop:step`::

  $ ase gui x.traj@0:10:1  # first 10 images
  $ ase gui x.traj@0:10    # first 10 images
  $ ase gui x.traj@:10     # first 10 images
  $ ase gui x.traj@-10:    # last 10 images
  $ ase gui x.traj@0       # first image
  $ ase gui x.traj@-1      # last image
  $ ase gui x.traj@::2     # every second image

If you want to select the same range from many files, the you can use
the ``-n`` or ``--image-number`` option::

  $ ase gui -n -1 *.traj   # last image from all files
  $ ase gui -n 0 *.traj    # first image from all files

.. tip::

  Type :command:`ase gui -h` for a description of all command line options.


NEB calculations
----------------

Use :menuselection:`Tools --> NEB` to plot energy barrier.

::

  $ ase gui --interpolate 3 initial.xyz final.xyz -o interpolated_path.traj


Plotting data from the command line
-----------------------------------
Plot the energy relative to the energy of the first image as a
function of the distance between atom 0 and 5::

  $ ase gui -g "d(0,5),e-E[0]" x.traj
  $ ase gui -t -g "d(0,5),e-E[0]" x.traj > x.dat  # No GUI, write data to stdout

The symbols are the same as used in the plotting data function.


.. _gui configuration:

Configuring the GUI
-------------------

Certain defaults for the GUI can be set using a file ``~/.ase/gui.py``.
If the file exists, it is executed after initializing the variables and
colors normally used in ASE.

For example, one can change the default graphs that are plotted, and the
default radii for displaying specific atoms. The following will change the
default graph in the GUI to display the energy evolution and the maximal
force and also display Cu atoms (Z=29) with a radius of 1.6 Angstrom. The
``covalent_radii`` setting also accepts key-value pairs in the form of a
dictionary, and atoms can be referred to using atomic symbols.

::

  gui_default_settings['gui_graphs_string'] = "i, e - min(E), fmax"
  gui_default_settings['covalent_radii'] = [[29,1.6]]  # or {29: 1.6}

To see a list of all settings that can be changed, along with their
default values, do:

::

  from ase.gui.defaults import gui_default_settings
  print(gui_default_settings)


.. _high contrast:

High contrast settings
----------------------

It is possible to change the foreground and background colors used to draw the
atoms, for instance to draw white graphics on a black background. This can be
done in ``~/.ase/gui.py``:

::

  gui_default_settings['gui_foreground_color'] = '#ffffff' #white
  gui_default_settings['gui_background_color'] = '#000000' #black

The color scheme of the windows themselves (i.e. menus, buttons
and text etc.) can be changed by choosing a different desktop theme. In
Ubuntu it is possible to get white on a dark background by selecting the
theme HighContrastInverse under Appearances in the system settings dialog.

To change the color scheme of graphs, configure the default behaviour of
Matplotlib in a similar way by using a file ``~/.matplotlib/matplotlibrc``.
For example:

::

  patch.edgecolor  : white
  text.color       : white
  axes.facecolor   : black
  axes.edgecolor   : white
  axes.labelcolor  : white
  axes.color_cycle : b, g, r, c, m, y, w
  xtick.color      : white
  ytick.color      : white
  grid.color       : white
  figure.facecolor : 0.1
  figure.edgecolor : black


Polling the GUI
---------------

Use :meth:`ase.gui.gui.GUI.repeat_poll` to interact programmatically
with the GUI, for example to monitor an ongoing calculation
and update the display on the fly.

.. automethod:: ase.gui.gui.GUI.repeat_poll
