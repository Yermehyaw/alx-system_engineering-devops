#!/usr/bin/env ruby
# Matches any or no repitition of "t" in only the "hbtn" format
puts ARGV[0].scan(/^hbt*n/).join
