#!/usr/bin/env ruby

input = ARGV[0]

# Match pattern: h, b, at least two 't's, then n
if input =~ /^hbtt{2,5}n$/
  puts "Match found!"
else
  puts "No match."
end
