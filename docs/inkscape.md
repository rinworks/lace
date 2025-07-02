# Inkscape Application notes
This document contains observations and references about behavior of the Inkscape Application itself, as opposed to the Inkscape extension ecosystem.
## Inkscape xml attributes
In addition to the svg namespace attributes and other standard attributes like xlink, Inkscape adds attributes to some of the XML elements for its own customizations. Two namespaces that you are likely to see are _sodipodi_ and _inkscape_. The former refers to the original Inkscape codebase. Newer attributes are defined under the _inkscape_ namespace.

[This wiki](https://wiki.inkscape.org/wiki/Inkscape-specific_XML_attributes) lists the _sodipodi_ and _inkscape_ attributes but only describes a few of them.
### sodipodi attributes
#### docname
This attribute is attached to the root svg element of the file by Inkscape. Its value is the file name, without path.
#### cx, cy
These are used with _sodipodi:type_ elements like _arc_ and _star_ to reflect the x,y coordinates of the center in the same way svg uses them with the _ellipse_ and _circle_ shapes.
#### rx, ry
These are used with  _sodipodi:type_ elements like _arc_ to reflect the x and y radius in the same way as _ellipse_ shapes.
#### r1, r2
These are used to denote the radii of the two control points in a star/polygon Inkscape shape.For a polygon only _r1_ is used.
#### type
Extends the svg elements to represent Inkscape object types. Two such types are:
- __star__ , which extends the _path_ with the following sodipodi attributes: _sides_, _cx_, _cy_, _r1_, _r2_, _arg1_, _arg2_ and inkscape attributes _flatsided_ and _rounded_.
- __arc__, which extends the _path_ attribute to represent an elliptical arc with the following sodipodi attributes: _cx_, _cy_, _rx_, _ry_ , _arc-type_, _start_, _end_ and _open_.
- __spiral__, which extends the _path_ attributes to represent a spiral Inkscape object with the following sodipodi attributes: _cx_, _cy_, _argument_, _radius_, _revolution_, _expansion_
#### arc-type
Choice of _slice_, _chord_ and _arc_ for the __arc__ Inkscape object type produced by the Ellipse/Arc tool

#### sides
Number of sides of a Inkscape polygon object or points of a star object
#### start, end
The beginning and ending angle of an arc in radians. 0 to 2*pi will draw a semi-circle
#### arg1, arg2
Used to parameterize polygon. Unclear exact behavior.

#### namedview
This is an element name, not an attribute. It appears to be added one level inside the top level svg node and contains a number of Inkscape view properties: inkscape:document-units, inkscape:deskcolor, inkscape:pagecheckerboard, inkscape:pageopacity, pagecolor, bordercolor and others. These affect the default page layout in Inkscape when the document is loaded, allowing different documents to presumably have different views.
#### guide
This is an element name, not an attribute. It represents a guide line. The guide element is created inside the namedview and contains the following attributes: _orientation_, _position_ and _inkscape:locked_. Since guide is a sodipodi element, the guide line will not show up outside Inkscape.

### inkscape attributes
#### version
This attribute, attached to the root level svg element is the version of Inkscape used to create the svg document.
#### rounded
Number denoting how rounded the corners of the polygon/star are. 0 implies sharp corners
#### flatsided
Whether polygon (true) or star (false)
#### groupmode
Attribute attached to svg group <g> node to describe the Inkscape semantic. Possible values:
- __layer__, group represents an Inkscape Layer

#### label
User visible label on object, such as a layer name
#### grid
This is an element name, not an attribute. It represents a grid. The grid element is created inside the namedview and has a number of attributes.



