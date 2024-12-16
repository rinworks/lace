# Intersection and Closeness Testing

Objects in a design will often need to be laid out without overlapping with other objects. They may
in fact need to be separated by some distance. Some generative algorithms may need to control rate of
growth based on how close they are to other objects.

We need to decide what kinds of functions will help us achieve this and how to implement them.

**Possible closeness functions**
- `get_closest_object(this_object) -> (other_object, intersects:bool)` - returns the closest object
and whether or not it intersects. From there we could get it's relative position of the closest
object if that is needed for growing the current object.
- `get_closest_neighboring_point(this_object) -> (x, y, distance))` - returns the point of the object that is closest to the current object and the distance between that that point and the boundary of the current object. The impementation of this version of the capability potentially does not require all objects to be iterated - but (in principle) could be obtained by a rasterized version of the current state of the design. See implementation possibilities below.


## Implementation possibilities
Intersection is a difficult problem and needs to be performed efficiently to enable iterative
pattern generation. If at all possible, we should not reinvent the wheel. There may be functions we can
use within InkEx or 3rd party libraries.

Some possibilities:
- Maintain a raster (perhaps 1 bit per pixel at
some resolution), and intersection tests involve bit testing against that raster, which can be done
efficiently. This has its own challenges, such as how to leave out the current object when using a
previously rendered bitmap.
- Perhaps we maintain an invariant that objects never intersect. Then we can keep a list of
  individual object bitmaps and the collective one. To check for intersection with a new version of
 an object we can can check if the intersection area is outside the previous version of the current object.
- Speed things up by considering bounding boxes or multi-resolution bitmaps.

Further thoughts:
- Design for hundreds, possibly thousands of objects.
