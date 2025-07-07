stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 310,
    "AMZN": 3500
}

portfolio = {}
total_value = 0

print("Enter your stock portfolio (type 'done' to finish):")
while True:
    stock = input("Stock symbol : ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

print("\n{:<10} {:<10} {:<10} {:<10}".format("Stock", "Quantity", "Price", "Value"))
print("-" * 40)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock:<10} {qty:<10} ${price:<9} ${value:<10}")

print("-" * 40)
print(f"{'Total':<32} ${total_value:<10}")
