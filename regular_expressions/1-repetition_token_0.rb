#!/usr/bin/env ruby

input = ARGV[0]

# Match pattern: h, b, at least two 't's, then n
if input =~ /^(hbttn|hbtttn|hbttttn|hbtttttn)$/
  puts input
end
