#!/usr/bin/env ruby

input = ARGV[0]

capital_letters = input.scan(/[A-Z]/).join

puts capital_letters unless capital_letters.empty?
