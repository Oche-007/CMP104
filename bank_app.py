import tkinter as tk

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank App")

        # Initialize account balances
        self.savings_balance = 1000
        self.current_balance = 500

        # Create widgets
        self.savings_label = tk.Label(self, text="Savings Account Balance: ${}".format(self.savings_balance))
        self.current_label = tk.Label(self, text="Current Account Balance: ${}".format(self.current_balance))
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_entry = tk.Entry(self)
        self.savings_deposit_button = tk.Button(self, text="Savings Deposit", command=self.savings_deposit)
        self.savings_withdraw_button = tk.Button(self, text="Savings Withdraw", command=self.savings_withdraw)
        self.current_deposit_button = tk.Button(self, text="Current Deposit", command=self.current_deposit)
        self.current_withdraw_button = tk.Button(self, text="Current Withdraw", command=self.current_withdraw)

        # Grid layout
        self.savings_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.current_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.amount_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)
        self.savings_deposit_button.grid(row=3, column=0, padx=10, pady=5)
        self.savings_withdraw_button.grid(row=3, column=1, padx=10, pady=5)
        self.current_deposit_button.grid(row=4, column=0, padx=10, pady=5)
        self.current_withdraw_button.grid(row=4, column=1, padx=10, pady=5)

    def savings_deposit(self):
        amount = self.get_amount()
        self.savings_balance += amount
        self.update_balances()

    def savings_withdraw(self):
        amount = self.get_amount()
        if amount <= self.savings_balance:
            self.savings_balance -= amount
        else:
            tk.messagebox.showerror("Error", "Insufficient funds.")
        self.update_balances()

    def current_deposit(self):
        amount = self.get_amount()
        self.current_balance += amount
        self.update_balances()

    def current_withdraw(self):
        amount = self.get_amount()
        if amount <= self.current_balance:
            self.current_balance -= amount
        else:
            tk.messagebox.showerror("Error", "Insufficient funds.")
        self.update_balances()

    def get_amount(self):
        amount = self.amount_entry.get()
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.amount_entry.delete(0, tk.END)
        return amount

    def update_balances(self):
        self.savings_label.config(text="Savings Account Balance: ${}".format(self.savings_balance))
        self.current_label.config(text="Current Account Balance: ${}".format(self.current_balance))

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
    