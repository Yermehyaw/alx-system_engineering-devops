#!/usr/bin/env ruby
# Match a 10 digit number only
puts ARGV[0].scan(/^\d\d\d\d\d\d\d\d\d\d$/).join
