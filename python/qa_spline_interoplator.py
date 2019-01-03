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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from spline_interoplator import spline_interoplator

class qa_spline_interoplator (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.src_data = (1, 2, 3, 4)
        self.expected_result = (1, 2, 2, 4, 3, 6, 4, 8)
        self.src = blocks.vector_source_f(self.src_data)
        self.spline_interpolate = spline_interoplator(2)
        
        self.dst = blocks.vector_sink_f()
        self.tb.connect(self.src, self.spline_interpolate)
        self.tb.connect(self.spline_interpolate, self.dst)
        
        self.tb.run ()
        # check data
        self.result_data  = self.dst.data()
        print(self.result_data)
        self.assertFloatTuplesAlmostEqual(self.expected_result, self.result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_spline_interoplator, "qa_spline_interoplator.xml")
