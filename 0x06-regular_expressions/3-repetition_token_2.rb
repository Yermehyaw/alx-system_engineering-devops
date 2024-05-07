#!/usr/bin/env ruby
# Match one or more repititions of "t" in "hbtn" strings
puts ARGV[0].scan(/^hbt+n/).join
