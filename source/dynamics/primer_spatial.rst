Primer on Spatial Dynamics
===========================

.. note::
  This section is a rough summary of 
  "Roy Featherstone, 2010, A Beginner's Guide to 6-D Vectors (Part 1)"

Definitons
----------

Spatial Velocity (Twist)
^^^^^^^^^^^^^^^^^^^^^^^^

As a motion vector, velocity :math:`v \in M^{6}`.

.. math::
  v =\
  \begin{bmatrix}
    w \\
    \rule[.5ex]{1.5em}{0.4pt} \\
    v_B
  \end{bmatrix}
  =\
  \begin{bmatrix}
    w_x \\
    w_y \\
    w_z \\
    \rule[.5ex]{1.5em}{0.4pt} \\
    v_x \\
    v_y \\
    v_z \\
  \end{bmatrix}


Spatial Acceleration
^^^^^^^^^^^^^^^^^^^^

As a motion vector, acceleration :math:`a \in M^{6}`.

.. math::
  a = \dv{v}{t} = \dfrac{d}{dt}\ \begin{bmatrix} w \\ v \end{bmatrix}
  = \begin{bmatrix} \dot{w} \\ \ddot{r} - w \times \dot{r} \end{bmatrix}

where :math:`r = \vec{OO'}`. O is a fixed point in space. :math:`O'` is 
the body-fixed point that momentarily coincides with O. Thus, :math:`r=0` initially,
but it is non-zero in general.

Spatial Force (Wrench)
^^^^^^^^^^^^^^^^^^^^^^

Force vector :math:`f \in F^{6}`. Combines a moment (denoted with n) and a force in a 6-dim vector.

.. math:: 
  \hat{f} =\
  \begin{bmatrix}
    n \\
    \rule[.5ex]{1.5em}{0.4pt} \\
    f
  \end{bmatrix}
  =\
  \begin{bmatrix}
    n_x \\
    n_y \\
    n_z \\
    \rule[.5ex]{1.5em}{0.4pt} \\
    f_x \\
    f_y \\
    f_z \\
  \end{bmatrix}

Spatial Inertia
^^^^^^^^^^^^^^^

.. math::
  I = 
  \begin{bmatrix}
    \overline{I}_c + m c \times c\times^{T} & m c \times \\
    m c\times^{T} & m 1 
  \end{bmatrix}

where

* m is the body's mass
* c is a 3-D vector locating the body's CoM
* :math:`\overline{I}_c` is the body's rotational inertia about its CoM

Or equivalently :ref:`dynamics/single_body:Spatial Momentum`.

**Coordinate-Transformation**

.. math::
  ^{B}I = ^{B}X^{*}_A\ ^{A}I\ ^{A}X_B


Spatial Momentum
^^^^^^^^^^^^^^^^

.. math::
  h = Iv

Spatial Equation of Motion
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::
  f = \dv{h}{t} = \dv{Iv}{t} = Ia + v \times^{*} Iv

See `Force Vector Cross Product`_.

Coordinate Transforms
^^^^^^^^^^^^^^^^^^^^^

6-dim spatial vectors use :ref:`dynamics/Fundamentals:Plücker Coordinates`.
For coordinate :ref:`frames <dynamics/Fundamentals:Frame>` A and B.

Spatial Motion Transform
""""""""""""""""""""""""""

.. math::
  ^{B}m =\ ^{B}X_A\ ^{A}m

  ^{B}X_A = \begin{bmatrix} ^{B}R_A & 0 \\ 0 & ^{B}R_A \end{bmatrix}
  \begin{bmatrix} 1 & 0 \\ S(-r) & 1 \end{bmatrix}

Or equivalently :ref:`dynamics/single_body:Transforming Spatial Velocity`.

Spatial Force/Momentum Transform
"""""""""""""""""""""""""""""""""

.. math::
  ^{B}f =\ ^{B}X^{*}_A\ ^{A}f

  ^{B}X_A = \begin{bmatrix} ^{B}R_A & 0 \\ 0 & ^{B}R_A \end{bmatrix}
  \begin{bmatrix} 1 & S(-r) \\ 0 & 1 \end{bmatrix}

Or equivalently :ref:`dynamics/single_body:Spatial Forces`.

.. note::
  .. math::
    ^{B}X^{*}_A = (\ ^{B}X_A)^{-T}

Spatial Cross Product
^^^^^^^^^^^^^^^^^^^^^

Motion Vector Cross Product
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defined for motion vector with motion vector, i.e. :math:`m \times m`

.. math::
  Spatial\ velocity/acceleration :\ &V = \begin{bmatrix} w \\ \rule[.5ex]{1.5em}{0.4pt} \\ v \end{bmatrix}

  Spatial\ cross\ product:\ &V \times = \begin{bmatrix} S(w) & 0 \\ S(v) & S(w) \end{bmatrix}

where S(.) is the :ref:`dynamics/Fundamentals:Cross product`.

Force Vector Cross Product
^^^^^^^^^^^^^^^^^^^^^^^^^^

Defined for motion vector with force vector, i.e. :math:`m \times^{*} f`

.. math::
  Spatial\ velocity/acceleration:\ &V = \begin{bmatrix} w \\ \rule[.5ex]{1.5em}{0.4pt} \\ v \end{bmatrix}

  Spatial\ force\ cross\ product:\ &V \times^{*} = \begin{bmatrix} S(w) & S(v) \\ 0 & S(w) \end{bmatrix}

where S(.) is the :ref:`dynamics/Fundamentals:Cross product`.

.. note::
  .. math::
    v \times^{*} = -v \times^{T}

Using Spatial Vectors
---------------------

Relative Velocity
^^^^^^^^^^^^^^^^^

.. math::
  v_{rel} = v_2 - v_1

Relative Acceleration
^^^^^^^^^^^^^^^^^^^^^

.. math::
  a_{rel} = \dv{v_{rel}}{t} = a_2 - a_1

.. attention::
  Simpler than conventional acceleration.

Summation of Forces
^^^^^^^^^^^^^^^^^^^

.. math::
  f_{tot} = f_1 + f_2

Action and Reaction
^^^^^^^^^^^^^^^^^^^

If body :math:`B_1` exerts a force f on body :math:`B_2`, then :math:`B_2` exerts
a force of -f as reaction to :math:`B_1`.

Scalar product
^^^^^^^^^^^^^^

.. math::
  Power = f \cdot v

Scalar multiplication
^^^^^^^^^^^^^^^^^^^^^

Spatial vector, motion or force, s has magnitudes :math:`m_1, m_2` and line l.

Then :math:`\alpha` s has magnitudes :math:`\alpha m_1, \alpha m_2` and line l.

Differentiation
^^^^^^^^^^^^^^^

For a motion vector, :math:`m \in M^{6}` and a force vector, :math:`f \in F^{6}`
that are fixed in a body having a velocity of v, then

.. math::
  \dot{m} = v \times m

  \dot{f} = v \times^{*} f

See `Spatial Cross Product`_.

Summation of Inertias
^^^^^^^^^^^^^^^^^^^^^

For rigidly connected bodies: :math:`I_{tot} = I_1 + I_2`

Motion Constraints
^^^^^^^^^^^^^^^^^^

A statement of D'Alembert's principle of virtual work for spatial vectors:

  If the relative velocity of two rigid bodies is constrained to lie in a subspace
  :math:`S \subseteq M^{6}`, then the motion constraint is implemented by a constraint
  force lying in the subspace:

  .. math::
    T = f \in F^{6}\ |\ f \cdot v=0\ \forall v \in S.