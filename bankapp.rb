require 'json'

class BankAccoun
  attr_reader :balance

  def initialize(owner_name, initial_balance = 0)
    @owner_name = owner_name
    @balance = initial_balance
  end

  def deposit(amount)
    @balance += amount
    puts "#{amount} deposited. New balance: #{@balance}"
  end

  def withdraw(amount)
    if amount <= @balance
      @balance -= amount
      puts "#{amount} withdrawn. New balance: #{@balance}"
    else
      puts "Insufficient funds. Your current balance is #{@balance}"
    end
  end

  def display_balance
    puts "Current balance for #{@owner_name}: #{@balance}"
  end
end

class BankApp
  def initialize
    @accounts = load_accounts || {}
    puts "Loaded Accounts: #{@accounts}"  
  end

  def load_accounts
    accounts_file = 'accounts.json'
    begin
      if File.exist?(accounts_file)
        JSON.parse(File.read(accounts_file), symbolize_names: true)
      else
        nil
      end
    rescue StandardError => e
      puts "Error loading accounts: #{e.message}"
      nil
    end
  end

  def save_accounts
    accounts_file = 'accounts.json'
    begin
      File.open(accounts_file, 'w') do |file|
        file.write(JSON.pretty_generate(@accounts))
      end
    rescue StandardError => e
      puts "Error saving accounts: #{e.message}"
    end
  end

  def create_account(owner_name, initial_balance)
    if owner_name.empty?
      puts "Account name cannot be empty."
      return
    end

    if @accounts.has_key?(owner_name)
      puts "Account already exists for #{owner_name}."
    else
      @accounts[owner_name] = { balance: initial_balance }
      save_accounts
      puts "Account created for #{owner_name} with initial balance of #{initial_balance}."
      display_account(owner_name) 
    end
  end

  def access_account(owner_name)
    if @accounts.has_key?(owner_name)
      account = @accounts[owner_name]
      loop do
        puts "\nWhat would you like to do?"
        puts "1. Deposit"
        puts "2. Withdraw"
        puts "3. Check Balance"
        puts "4. Exit"
        print "Enter your choice: "
        choice = gets.chomp.to_i

        case choice
        when 1
          print "Enter the amount to deposit: "
          amount = get_valid_amount("deposit")
          account[:balance] += amount
          puts "#{amount} deposited. New balance: #{account[:balance]}"
          save_accounts
        when 2
          print "Enter the amount to withdraw: "
          amount = get_valid_amount("withdraw")
          if amount <= account[:balance]
            account[:balance] -= amount
            puts "#{amount} withdrawn. New balance: #{account[:balance]}"
          else
            puts "Insufficient funds. Your current balance is #{account[:balance]}"
          end
          save_accounts
        when 3
          account.display_balance
        when 4
          break
        else
          puts "Invalid choice. Please enter a number from 1 to 4."
        end
      end
    else
      puts "Account not found for #{owner_name}."
    end
  end

  def display_account(owner_name)
    if @accounts.has_key?(owner_name)
      account_data = @accounts[owner_name]
      puts "\nAccount Details:"
      puts "Owner Name: #{owner_name}"
      puts "Balance: #{account_data[:balance]}" 
    else
      puts "Account not found for #{owner_name}."
    end
  end

  def get_valid_amount(action)
    loop do
      amount = gets.chomp.to_f
      if amount <= 0.0
        puts "Invalid amount. Please enter a positive amount for #{action}."
      else
        return amount
      end
    end
  end
end

# Main Program Loop
bank_app = BankApp.new

loop do
  puts "\nWhat would you like to do?"
  puts "1. Create Account"
  puts "2. Access Account"
  puts "3. Exit"
  print "Enter your choice: "
  choice = gets.chomp.to_i

  case choice
  when 1
    print "Enter your name: "
    owner_name = gets.chomp
    print "Enter initial balance: "
    initial_balance = gets.chomp.to_f
    bank_app.create_account(owner_name, initial_balance)
  when 2
    print "Enter your name: "
    owner_name = gets.chomp
    bank_app.access_account(owner_name)
  when 3
    break
  else
    puts "Invalid choice. Please enter a number from 1 to 3."
  end
end
