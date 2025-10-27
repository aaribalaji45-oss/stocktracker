# Stock Portfolio Tracker
# Author: Balaji AH
# Goal: Calculate total investment value based on user input and hardcoded stock prices.

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 330
}

portfolio = {}

print(" Welcome to the Stock Portfolio Tracker")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"  {stock}: ${price}")

print("\nEnter your stock holdings (type 'done' to finish):")

# Get user input for stocks and quantities
while True:
    stock_name = input("Enter stock symbol: ").strip().upper()
    if stock_name == "DONE":
        break
    if stock_name == "":
        print(" Please enter a stock symbol or 'done' to finish.")
        continue

    if stock_name not in stock_prices:
        print(" Stock not found in the hardcoded list. Try again.")
        continue

    # allow fractional shares (float) or integer shares
    qty_str = input(f"Enter quantity of {stock_name} (e.g., 10 or 0.5): ").strip()
    try:
        quantity = float(qty_str)
        if quantity <= 0:
            print(" Quantity must be positive.")
            continue
        # If the user enters the same symbol again, add to existing quantity
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print(" Please enter a valid number for quantity (e.g., 5 or 0.25).")

# If portfolio empty, inform user and exit
if not portfolio:
    print("\nNo stocks entered. Exiting.")
    raise SystemExit

# Calculate total investment
total_value = 0.0
print("\n--- Your Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = qty * price
    total_value += investment
    # Format numbers: show up to 4 decimal places for qty (useful for fractional shares)
    print(f"{stock}: {qty:.4f} shares × ${price:.2f} = ${investment:,.2f}")

print(f"\n Total Investment Value: ${total_value:,.2f}")

# Optional: Save to file
save = input("\nDo you want to save your portfolio to a file? (yes/no): ").strip().lower()
if save in ("y", "yes"):
    filename = "portfolio_summary.csv"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                investment = qty * price
                file.write(f"{stock},{qty:.8f},{price:.2f},{investment:.2f}\n")
            file.write(f"TOTAL,,,{total_value:.2f}\n")
        print(f"✅ Portfolio saved successfully as '{filename}'")
    except OSError as e:
        print(f" Could not save file: {e}")

print("\nThank you for using the Stock Portfolio Tracker!")
