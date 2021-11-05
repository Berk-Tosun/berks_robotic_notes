Contact Dynamics
================

Equation of Motion
------------------

By including the additional external force term, we generalize the EoM to full.

.. figure:: ../images/contact_mapping_eom.png

Contact Modes
-------------

.. figure:: ../images/contact_modes_intro.png

Which Contact Model to Choose?
------------------------------

.. figure:: ../images/contact_models_overview.png

Compliant Contact
^^^^^^^^^^^^^^^^^

* Requires use of flight coordinates all the time.
* Commonly used model is assuming a damper and a spring at contact point in
  all directions. This approach which assumes linearity is not very realistic.
* Thus, contact force increases based on the amount of deformation.
* **Better** approach is to project onto a friction cone.
* For hard terrain, equations become stiff, numerically unstable. Thus, requiring
  small time steps.

.. note::
  For numerical integration, ode45 assumes differentiability; whereas regular Euler
  integration which is 1st order does not. That means Euler will work better with
  contact, since it is discontinuous.

Minimal Coordinates
^^^^^^^^^^^^^^^^^^^
  
* Use minimal coordinates when in contact. Its joint angles form the minimal
  coordinates.
* Can be solved as a regular, fixed-base system. Simplifies everything.
* However, that simplification is also a big disadvantage. The contact is not
  rigidly pinned, we do not consider the limitations.
* Another disadvantage, for every contact configuration it requires new coordinates.
* Useful for analytical work, e.g. proves.

.. note::
  We can run into multiple contact cases leading to closed chains.
  In that case, EoM requires some modification.

  .. figure:: ../images/contact_eom_closed_chain.png

Excess Coordinates
^^^^^^^^^^^^^^^^^^

* Use flight coordinates all the time.
* Connect body and ground through a virtual 6-dof joint.
* Split coordinates into base and joint. (In other words, into actuated and unactuated)

.. figure:: ../images/contact_eom_excess_cord.png