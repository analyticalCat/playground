require 'httparty'
require 'json'

class Recipe
  include HTTParty

  base_uri 'http://food2fork.com/api'
  default_params key: ENV["FOOD2FORK_KEY"]
  format :json

  def self.for keyword
    recipearray=[]
    data=self.get("/search", { query: {q: keyword}}).parsed_response["recipes"]
    # data.each do |item|
    #   recipearray<<item
    # end

  end

end







# class Recipe
#
#   include HTTParty
#
#   def self.for keyword
#     puts HTTParty.get('http://food2fork.com/api/search?key=a5551a6a4dde0c46f8259fa18e5c8d3e&q=' + keyword)
#   end
#
# end



