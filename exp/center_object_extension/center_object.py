import inkex

class CenterObject(inkex.Effect):
    """
    Center the second selected object over the first selected object.
    """
    def __init__(self):
        super().__init__()

    def effect(self):
        if len(self.options.ids) != 2:
            inkex.errormsg("Please select exactly two objects.")
            return

        id1, id2 = self.options.ids
        obj1 = self.svg.getElementById(id1)
        obj2 = self.svg.getElementById(id2)

        if obj1 is None:
            inkex.errormsg(f"Object with id {id1} not found.")
            return
        if obj2 is None:
            inkex.errormsg(f"Object with id {id2} not found.")
            return

        center1 = obj1.bounding_box().center
        center2 = obj2.bounding_box().center

        if center1 is None or center2 is None:
            inkex.errormsg("Could not determine the center of one or both objects. Make sure they are not empty groups.")
            return

        dx = center1[0] - center2[0]
        dy = center1[1] - center2[1]

        obj2.transform.add_translate(dx, dy)

if __name__ == '__main__':
    CenterObject().run()
