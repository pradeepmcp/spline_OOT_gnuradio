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
from spline_resampler_fff import spline_resampler_fff

class qa_spline_resampler_fff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        src_data = (1, 2)
        expected_result = (1, 2, 2, 4)
        src = blocks.vector_source_i(src_data, vlen=1)
        resampler = spline_resampler_fff(interpolation=2, decimation=1)
        dst = blocks.vector_sink_i()
        self.tb.connect(src, resampler)
        self.tb.connect(resampler, dst)
        self.tb.run ()
        # check data
        result_data  = dst.data()
        print(result_data)
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

if __name__ == '__main__':
    gr_unittest.run(qa_spline_resampler_fff, "qa_spline_resampler_fff.xml")
