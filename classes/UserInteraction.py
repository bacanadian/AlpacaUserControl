import alpaca_trade_api as tradeapi
from classes.logger import log

base_url = "https://paper-api.alpaca.markets"
api_key = "PKDRMTB4KT0W7NED1QDZ"
secret_key = "ysC/bdTg5265CCwRIXMAe1k/hCn5VUUny3dOd/lk"


class UserInteraction:

    def __init__(self):  # Creates session/logs in
        try:
            self.api = tradeapi.REST(
                    base_url=base_url,
                    key_id=api_key,
                    secret_key=secret_key
                )


            self.account = self.api.get_account()
            log("Successfully logged into account.", 1)
            log('${} is available as buying power.'.format(self.account.buying_power), 1)  # Checks buying power
        except:
            log("Failed to login to account.", 2)

    def getAssets(self):
        active_assets = self.api.list_assets(status='active')
        nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']  # Finds all tickers listed on NASDAQ
        for i in nasdaq_assets:
            print(i)


    def checkTradable(self):
        log("Please enter the stock you would like to see trade status for. (EX: 'AAPL')", 3)
        stock = input()
        try:
            checkAsset = self.api.get_asset(stock)  # Grabs stock
            if checkAsset.tradable:
                log(stock + " is tradable.", 1)
            else:
                log(stock + " is not tradable.", 4)
        except:
            log("Error finding " + stock, 2)


    def checkMarket(self):
        clock = self.api.get_clock()
        log('The market is {}'.format('open.' if clock.is_open else 'closed.'), 1)  # checks if market is open


    def submitOrder(self):
        log("Please enter the stock you would like to purchase or leave blank to exit.", 3)
        stock = input()

        if stock != "":
            log("Please enter the number of shares you would like to purchase:", 3)
            quantity = input()
            log("Confirming " + str(quantity) + " of " + stock, 3)
            log("Confirm order? (Y/N)", 3)
            status = input()

            if status == "Y":
                try:
                    self.api.submit_order(  # code for submitting order
                        symbol=stock,
                        qty=quantity,
                        side="buy",
                        type="market",
                        time_in_force='gtc'
                    )
                    log("Order Submitted.", 1)
                except:
                    log("Failed to submit order.", 2)

            else:
                log("Cancelling order...", 3)

        else:
            log("Exiting menu.", 3)


    def sellOrder(self):
        log("Please enter the stock you would like to sell or leave blank to exit.", 3)
        stock = input()

        if stock != "":
            log("Please enter the number of shares you would like to sell:", 3)
            quantity = input()
            log("Confirming " + str(quantity) + " of " + stock, 3)
            log("Confirm sale? (Y/N)", 3)
            status = input()

            if status == "Y":
                try:
                    self.api.submit_order(  # commit sell order
                        symbol=stock,
                        qty=quantity,
                        side="sell",
                        type="market",
                        time_in_force='gtc'
                    )
                    log("Order Submitted.", 1)
                except:
                    log("Failed to submit order.", 2)

            else:
                log("Cancelling order...", 3)

        else:
            log("Exiting menu.", 3)


    def displayPortfolio(self):
        portfolio = self.api.list_positions()
        for position in portfolio:
            log("{} shares of {}".format(position.qty, position.symbol), 1)


    def displayOrders(self):
        orders = self.api.list_orders()
        print(orders)

