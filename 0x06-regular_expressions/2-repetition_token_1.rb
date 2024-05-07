#!/usr/bin/env ruby
# Match only one or no occurence of "b" in "hbtn" strings
puts ARGV[0].scan(/^hb?tn/).join
