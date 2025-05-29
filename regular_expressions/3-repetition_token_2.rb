#!/usr/bin/env ruby

input = ARGV[0]

# Match only the exact valid strings
if input =~ /^(hbtn|hbttn|hbtttn|hbttttn|hbtttttn)$/
  puts input
end

