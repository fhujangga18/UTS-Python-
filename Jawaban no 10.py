def analyze_transactions(transactions):
    """
    Analyzes a series of transactions to calculate the final balance,
    identify the day with the largest expense, and find days without transactions.

    Args:
        transactions: A dictionary where keys are days (strings) and values are transaction amounts (integers).

    Returns:
        A tuple containing:
            - The final balance (integer).
            - The day with the largest expense (string).
            - A list of days without transactions (list of strings).
    """

    balance = 0
    largest_expense_day = None
    largest_expense = 0
    no_transaction_days = []

    for day, amount in transactions.items():
        balance += amount
        if amount < largest_expense:
            largest_expense = amount
            largest_expense_day = day
        if amount == 0:
            no_transaction_days.append(day)

    return balance, largest_expense_day, no_transaction_days


# Example usage:
transactions = {
    "Senin": 50000,
    "Selasa": -20000,
    "Rabu": 0,
    "Kamis": 100000
}

final_balance, largest_expense_day, no_transaction_days = analyze_transactions(transactions)

print("Saldo akhir:", final_balance)
print("Hari dengan pengeluaran terbesar:", largest_expense_day)
print("Hari tanpa transaksi:", no_transaction_days)
