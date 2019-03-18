def print_list(array, first = 1)
  counter = first
  array.each do |item|
    puts "#{yield counter}. #{item}"
    counter = counter.next
  end
end

print_list(['aa','bb'], 3) {|n| "<#{n}>"}
