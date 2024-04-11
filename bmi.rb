def bmi(weight, height)
    bmi = weight / height**
    if bmi <= 18.5
      "Underweight"
    elsif bmi <= 25.0
      "Normal"
    elsif bmi <= 30.0
      "Overweight"
    elsif bmi > 30
      "Obese"
    end
  end
  
  puts "Enter weight in kilograms:"
  weight = gets.chomp.to_f  # Converts input to a floating point number, suitable for weight
  
  puts "Enter height in meters:"
  height = gets.chomp.to_f  # Converts input to a floating point number, suitable for height
  
  puts "BMI Category: #{bmi(weight, height)}"
  