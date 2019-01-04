#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 Pradeep.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
#from scipy.interpolate import interpolate.interp1d
from gnuradio import gr
from scipy.interpolate.interpolate import interp1d

class spline_interpolator(gr.interp_block):
    """
    docstring for block spline_interpolator
    """
    def __init__(self, interpolation):
        gr.interp_block.__init__(self,
            name="spline_interpolator",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32], interp=interpolation)
        self.interpolation = interpolation
        
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0] 
        
        # scipy's interp1d expects atleast 4 datapoints
        if len(in0) < 4:
            return 0
               
        n = numpy.linspace(0, len(in0), num=len(in0))
        f = interp1d(n, in0, kind='cubic')
        outn = numpy.linspace(0, len(in0), num=len(in0)*self.interpolation, endpoint=False)
        tmp_out = f(outn)
        out0[:] = tmp_out[:]

        return len(output_items[0])

