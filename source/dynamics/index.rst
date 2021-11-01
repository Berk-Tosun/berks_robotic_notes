
Dynamics
========

Following section assumes you have an understanding of conventional 3-D
dynamics. In addition, it is assumed that you are familiar with assigning 
coordinate frames and their transformations. Basically, an introductory 
robotics course is strongly recommended as a prerequisite.

We will utilize the modern robotics approach to dynamics which is popularized
by `Roy Featherstone <http://royfeatherstone.org/>`_. This is called as spatial
vectors or screw theory. This notation/formulation combines angular and linear 
motion into 6-D vectors; allowing the equations to be
simpler analytically and enables clean, efficient software implementations.
Featherstone also points out how they help to think of dynamics in a higher abstraction level.

.. toctree::
    :maxdepth: 2
    :numbered:

    Fundamentals
    Single Body <single_body>
    Multi Body <multi_body>