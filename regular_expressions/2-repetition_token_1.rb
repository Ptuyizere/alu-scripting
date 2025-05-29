#!/usr/bin/env ruby

input = ARGV[0]

# Match only the exact valid strings
if input =~ /^(htn|hbtn)$/
  puts input
end

