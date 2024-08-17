def bankingsystem():
        
        def Show_balance():
            print(f"\n\t\tYour balance is ₹{balance:.2f}")
            print("________________________________________________________________")
        
        def Deposit_money():
            print("________________________________________________________________")
            amt = float(input("\n\tEnter the amount to deposit:"))

            if amt < 0:
                print("_____________________________________________________________")
                print("\n\t\tInvalid amount! Please enter a positive value.")
                return 0
            else:
                transactions.append(f"Deposited: ₹{amt:.2f}")
                return amt
        
        def Withdraw_money():
            print("_____________________________________________________________")
            amt = float(input("\n\tEnter the amount to withdraw:"))
            
            if amt < 0:
                print("_____________________________________________________________")
                print("\n\t\tInvalid amount! Please enter a positive value.")
                return 0
            elif amt > balance:
                print("_____________________________________________________________")
                print("\n\t\tInsufficient balance!")
                return 0
            else:
                transactions.append(f"Withdrew: ₹{amt:.2f}")
                return amt

        def Calculate_interest():
            interest_rate = 0.05  
            interest = balance * interest_rate
            print("_____________________________________________________________")
            print(f"\n\t\tInterest earned on your balance: ₹{interest:.2f}")
            transactions.append(f"Interest Earned: ₹{interest:.2f}")
            return interest

        def Show_transaction_history():
            print("\n\tTransaction History:")
            print("_____________________________________________________________")
            if transactions:
                for transaction in transactions:
                    print(f"\t\t{transaction}")
            else:
                print("\t\tNo transactions found.")
            print("_____________________________________________________________")

        def Exit_program():
            print("_____________________________________________________________")
            print("\n\t\tThank you for using the Banking System!")
            print("________________________________________________________________")
            exit

        balance = 0
        transactions = []  

        while True:
            print("________________________________________________________________")
            print("________________________________________________________________")
            print("\n\t\tWelcome to the Banking System!")
            print("________________________________________________________________")
            print("\n\t1. Check Balance")
            print("________________________________________________________________")
            print("\n\t2. Deposit Money")
            print("________________________________________________________________")
            print("\n\t3. Withdraw Money")
            print("________________________________________________________________")
            print("\n\t4. Calculate Interest")
            print("________________________________________________________________")
            print("\n\t5. Show Transaction History")
            print("________________________________________________________________")
            print("\n\t6. Exit Program")
            print("________________________________________________________________")
            choice = int(input("\nEnter your choice (1-6): "))
            if choice == 1:
                Show_balance()
            elif choice == 2:
                balance += Deposit_money()
            elif choice == 3:
                balance -= Withdraw_money()
            elif choice == 4:
                balance += Calculate_interest()
                Show_balance()
            elif choice == 5:
                Show_transaction_history()
                Show_balance()
            elif choice == 6:
                Exit_program()
                break
            else:
                print("\n\t\tInvalid choice! Please try again.")

bankingsystem()
