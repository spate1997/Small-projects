#
def century(year)
    (year + 99) / 100
  end
  
  puts "Enter year:"
  year = gets.chomp.to_i  # Reads input from the user, removes the newline, and converts to an integer
  
  puts "The year #{year} is in the #{century(year)} century."
  