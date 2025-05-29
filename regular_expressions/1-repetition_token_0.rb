#!/usr/bin/env ruby

input = ARGV[0]

# Match pattern: h, b, at least two 't's, then n
if input =~ /^(hbttn|hbtttn|hbttttn|hbtttttn)$/
  puts "Match found!"
else
  puts "No match."
end
