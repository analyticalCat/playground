require 'httparty'

# class Recipe
#   include HTTParty
#
#   base_uri 'https://food2fork.com/api'
#   default_param key: ENV["FOOD2FORK_KEY"]
#   format :json
# #
#   def self.for (keyword)
#     get("/search", query: {q: keyword})["recipes"]
#   end
#
# end
#
# Recipe = Recipe.new()
# Recipe.for("chicken")
# Recipe.getRecipe("39165")
#

class Recipe

  include HTTParty

  def self.for keyword
    puts HTTParty.get('http://food2fork.com/api/search?key=a5551a6a4dde0c46f8259fa18e5c8d3e&q=' + keyword)
  end

end

puts Recipe.for("chocolate")