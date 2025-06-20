# Notes about Scalable Vector Graphics (svg) 
![svg basic](../exp/svgs/cat.svg)

The SVG describing the picture above is located in ../exp/svgs/cat.svg.
It showcases a few basic elements of SVGS:
- lines
- polylines
- circles
- paths
- text

There's also an example of a mirror and shift transform
### Coordinates, Viewbox
Coordinates can be specified as
- *px* Pixels (the default if omitted)
- *pt* Points (1/72 inch)
- *pc* Pica (12 points)
- *cm* Centimeters
- *mm* Millimeters
- *in* Inches

When a unit is omitted, it defaults to *px* or to the *user coordinates* of the enclosing viewbox (described later)

![svg coordinate units](../exp/svgs/coordinates.svg)

Notice that mm, cm, in retain their expected ratios even if the exact dimensions on screen are not as measured.

The *width* and *height* parameters in the svg tag refer to the viewport or space on the screen.
The svg itself can be described on a separate rectangle by a *viewBox* with its own coordinates. If omitted, the viewbox is identical to the viewport.
### Viewport
The picture below illustrates use of the viewBox with the *meet* qualifier in the *preserveAspectRatio* viewBox mapping attribute.
The first three SVGs show the effect of yMid, yMin and yMax respectively in vertical alignent of the square viewBox to a rectangular viewPort.
The last three SVGs show the same thing with horizontal alignment

![svg viewport](../exp/svgs/viewport.svg)

Rather than scale to fit, we can truncate the square viewBox to fit the rectangular viewPort. The next picture shows the use of the 
*slice* modifier to the *preserveAspectRatio* attribute to do that. The first three SVGs use yMid, yMin and yMax and the last three SVGs use xMid, xMin and xMax to define which edge of the viewBox matches the edge of the SVG.

![svg viewport slicing](../exp/svgs/viewport2.svg)

### Transforms
Transforms are a way to take a shape and apply translation, rotation and scaling operations. In the picture below, the grey and blue rectangles are translated (shifted) in the x and y dimension respectively. The red rectangle is rotated by 15 degrees and scaled by 2 as well. The transform attribute for the red rectangle is `transform="translate(80,40) rotate(15) scale(2)"`.

![svg transform](../exp/svgs/transform.svg)

The Transform implementations seem to have a bug that is now universal. Transforms specified in the *transform* attribute are applied in reverse order despite the spec saying the opposite. See [this thread](https://stackoverflow.com/questions/18582935/the-applying-order-of-svg-transforms) for the gory details.


### References
- [tavmjong's guide](http://tavmjong.free.fr/INKSCAPE/MANUAL/html/Web-SVG-Positioning.html)
- Chapter 3 of *SVG Essentials* by J. David Eisenberg
