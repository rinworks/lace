# Parameter Fields 
These are fields that extend over the surface. The provide a vector of parameters
at any point on the surface. They can be used by generative algorithms to determine localized
parameters. We do not place any constraint on how these fields are themselves generated or what
parameters they contain.

**Examples:**
- *Symmetry fields*exhibits different kinds of 2D symmetry groups tiled over the surface. One
  example of this is a checkerboard pattern that dictates the preferred orientation of objects within
  each square).
- *Random fields* provide a vector of probability values. One example is a field that directs that
  objects are spawned with greater concentrations near the borders of the enclosing shape.


## Use 
Specific generative algorithms will look up parameters at a particular point and use that to
spawn "seeds" of a graphic element. One technique to organically grow such designs is to
incrementally grow the designs, each time visiting each element and growing it in size, using other
elements of the field to control rate of growth and orientation of growth. Growing stops if there is
any element gets "too close" to another element.

APIs for creating and accessing parameter fields are TBD.
