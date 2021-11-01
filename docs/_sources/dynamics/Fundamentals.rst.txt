Fundamentals
============

Frame
-----

A frame consists of

* 3 coordinate vectors: :math:`\hat{x},\hat{y},\hat{z}`
* An origin :math:`O`
  
which satisfies

* :math:`\hat{x},\hat{y},\hat{z}` mutually orthogonal
* Right-handed i.e., :math:`\hat{x}\times\hat{y} = \hat{z}`

Variable-Frame Notation
-----------------------

Consider two distinct frames A and B:

.. math::

  &Variable\ X\ represented\ in\ frame\ A:\ ^{A}X 

  &Coordinate\ vector\ \hat{x}\ of\ frame\ A:\ \hat{x}_{A}
  
  &Coordinate\ vector\ \hat{x}\ of\ frame\ A\ represented\ in\ frame\ A:\ ^{A}\hat{x}_{A}

  &Coordinate\ vector\ \hat{x}\ of\ frame\ A\ represented\ in\ frame\ B:\ ^{B}\hat{x}_{A}

  &Spatial\ velocity\ for\ a\ rigid\ body,\ Body,\ sampled\ at\ point\ P:\ v_{Body[P]} 

.. \tensor[^B]{\hat{x}}{_x}

Rotation
--------

We will use rotation matrices. A rotation matrix specifies orientation of 
one frame relative to another.

.. .. topic:: Example

Consider 2 frames, A and B:

.. math::

  ^{A}R_{B} = [^{A}\hat{x}_{B}\ ^{A}\hat{y}_{B}\ ^{A}\hat{z}_{B}] \in \mathbb{R}^{3\times3}

Properties
^^^^^^^^^^

* :math:`R^\mathsf{T}R=I`
* :math:`det(R)=1`

Change of Basis
^^^^^^^^^^^^^^^

To express vector r in frame A:

.. math::
  ^{A}r=\ ^{A}R_B\ ^{B}r

Vector Space
------------

Operations
^^^^^^^^^^

* Vector addition: :math:`\forall{v_1, v_2} \in V, v_1 + v_2 \in V`
* Scalar multiplication: :math:`\forall{v} \in V, \alpha \in \mathbb{R}; \alpha \cdot v \in V`

Vector Field
^^^^^^^^^^^^

Define :math:`\Phi^n` as a vector field over :math:`\mathbb{R}^n`.

Dimensions
^^^^^^^^^^

* V is of dimension n if a basis exists for V
* V is an infinite dimensional vector space if no finite basis exists

.. topic:: Example

  * :math:`\mathbb{R}^3` is a 3-dim vector space, with a sample basis such as
    
    :math:`\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}`
    :math:`\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}`
    :math:`\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}`

  * Vector field :math:`\Phi^3` is an :math:`\infty`-dim vector space.

    It requires 3 quantities to describe a vector in :math:`\Phi^3`; however, a vector field consists
    of infinite number of vectors.

Plücker Coordinates
-------------------

Velocity
^^^^^^^^

For a given `Frame`_, say Frame A, we can define following 6 basis vector fields:

  * :math:`e_1`: Pure rotation about :math:`\hat{x}_A`
  * :math:`e_2`: Pure rotation about :math:`\hat{y}_A`
  * :math:`e_3`: Pure rotation about :math:`\hat{z}_A`
  * :math:`e_4`: Pure translation about :math:`\hat{x}_A`
  * :math:`e_5`: Pure translation about :math:`\hat{y}_A`
  * :math:`e_6`: Pure translation about :math:`\hat{z}_A`

Such that 

.. math:: 

  M = Span(\begin{bmatrix} e_1 \\ e_2 \\ e_3 \\ e_4 \\ e_5 \\ e_6 \end{bmatrix}) \subseteq \Phi^3

Cross product
-------------


