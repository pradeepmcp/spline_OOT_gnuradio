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
from gnuradio import gr

class spline_interoplator(gr.interp_block):
    """
    docstring for block spline_interoplator
    """
    def __init__(self, interpolation):
        gr.interp_block.__init__(self,
            name="spline_interoplator",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32], interp=interpolation)
        
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        # <+signal processing here+>
        print("in",len(in0))
        print("out",len(out0)) 
               
        
        i=0
        j=0
        #for i in range (len(out0)):
        while i < len(in0):
            #out0[i] = in0[i]
            out0[j] = in0[i]
            out0[j+1] = in0[i]*2
            #out0 = numpy.append(out0, in0[i]*2)
            i = i+1
            j = j+2
        
        self.set_history(4)
        return len(output_items[0])

