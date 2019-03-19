#require_relative "module3_1_assignment"


gem 'httparty'

require 'httparty'

puts "hello"
puts HTTParty.get('http://food2fork.com/api/search?key=a5551a6a4dde0c46f8259fa18e5c8d3e&q=chocolate')

#puts Recipe.for("chocolate")