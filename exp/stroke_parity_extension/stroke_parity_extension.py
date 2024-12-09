#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) [YEAR] [YOUR NAME], [YOUR EMAIL]
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
This extension changes the fill of all selected elements to red.
"""

import inkex

class StrokeParityExtension(inkex.EffectExtension):
    """EffectExtension to fill selected objects red"""
    def add_arguments(self, pars):
        pars.add_argument("--even_color", type=inkex.Color, default=inkex.Color("red"))
        pars.add_argument("--odd_color", type=inkex.Color, default=inkex.Color("blue"))       
        pars.add_argument("--remove_fill", type=inkex.Boolean, default=False)
        pars.add_argument("--tab", type=str, default="stroke")

    def effect(self):
        for elem in self.svg.selection.filter(inkex.PathElement):
            elem.set('inkscape:modified_by_tutorial', 'Yes')
            elem.style['stroke-width'] = 2.0
            if len(elem.path) % 2: # odd
                elem.style.set_color(self.options.odd_color, 'stroke')
            else:
                elem.style.set_color(self.options.even_color, 'stroke')

            if self.options.remove_fill:
                elem.style["fill"] = None

if __name__ == '__main__':
    StrokeParityExtension().run()
