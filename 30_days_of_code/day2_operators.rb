# Enter your code here. Read input from STDIN. Print output to STDOUT
mealCost = gets.chomp.to_f
tipPercent = gets.chomp.to_i
taxPercent = gets.chomp.to_i

totalCost = mealCost + (mealCost * (tipPercent * 0.01)) + (mealCost * (taxPercent * 0.01))
puts "The total meal cost is #{totalCost.round} dollars."
