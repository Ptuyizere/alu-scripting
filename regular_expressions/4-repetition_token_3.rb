#!/usr/bin/env ruby

input = ARGV[0]

# Match only the exact valid strings
if input =~ /^(hbtn|hbttn|hbtttn|hbttttn|hbn|hbttttttttttn)$/
  puts input
end

