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

class spline_resampler_fff(gr.basic_block):
    """
    docstring for block spline_resampler_fff
    """
    def __init__(self, interpolation=1, decimation=1):
        gr.basic_block.__init__(self,
            name="spline_resampler_fff",
            in_sig=[numpy.int16],
            #out_sig=[(numpy.int16,interpolation/decimation)])
            out_sig=[numpy.int16])
        self.interpolation = interpolation
        self.decimation = decimation

    def forecast(self, noutput_items, ninput_items_required):
        for i in range(len(ninput_items_required)):
            #ninput_items_required[i] = noutput_items * self.decimation/self.interpolation
            ninput_items_required[i] = noutput_items
        
        print("forecast", noutput_items, noutput_items * self.decimation/self.interpolation)

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        print("work input_items", len(input_items))
        print("work output items", len(output_items))
        print("in0",len(in0))
        print(len(out0))
        
        i=0
        #for i in range (len(out0)):
        while i < len(out0):
            out0[i] = in0[i]
            out0[i+1] = in0[i]*3
            i = i+1
        
        #consume(0, len(xinput_items[0]))
        self.consume(0, len(in0)/2)
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])
