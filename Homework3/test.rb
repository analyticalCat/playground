require 'httparty'

puts HTTParty.get('http://food2fork.com/api/search?key=a5551a6a4dde0c46f8259fa18e5c8d3e&q=chocolate')