#Stock Transaction Program
#The number of shares that Joe purchased 
# was 2,000.
#When Joe purchased the stock, he paid
#  $40.00 per share.
#Joe paid his stockbroker a commission
#  that amounted to 3 percent of the amount
# he paid for the stock.
#Two weeks later, Joe sold the stock. 
# Here are the details of the sale:
#The number of shares that Joe sold was 2,000.
#He sold the stock for $42.75 per share.
#He paid his stockbroker another commission that amounted to 3 percent of the
#  amount he received for the stock.
#Write a program that displays the following information:
#The amount of money Joe paid for the stock.
#The amount of commission Joe paid his broker when he bought the stock.
#The amount for which Joe sold the stock.
#The amount of commission Joe paid his broker when he sold the stock.
#Display the amount of money that Joe had left when he sold the stock and paid
#  his broker (both times). 
#If this amount is positive, then Joe made a profit. If the amount is negative, 
# then Joe lost money.


QTY_SHARES_PURCHASED = 2000
PRICE_PER_SHARE = 40.00
INITIAL_STOCK_BOUGHT = QTY_SHARES_PURCHASED * PRICE_PER_SHARE
print('Joe paid $',INITIAL_STOCK_BOUGHT)

def main():
    initial_commission()
    second_stock_sold()
    second_commission()
    profit_or_loss()
    
def initial_commission():
        com = (3 / 100 * INITIAL_STOCK_BOUGHT)
        return (com)
print('initial commission $', initial_commission())

def second_stock_sold():
        shares_sold_later = 2000
        price_sold = 42.75
        amount_received = shares_sold_later * price_sold
        return (amount_received)
print('he sold it for $',second_stock_sold())

def second_commission():
        new_commission = (3 / 100 * second_stock_sold())
        return (new_commission)
print('second commission $', second_commission())


def profit_or_loss():
        total_sold = second_stock_sold() - INITIAL_STOCK_BOUGHT
        total_commission = initial_commission() + second_commission()
        amount = total_sold - total_commission
        return (amount)
if profit_or_loss() > 0:
    print('he made profit of $',profit_or_loss())
else:
    print('he made loss of $', profit_or_loss)
profit_or_loss()
main()