import alpaca_trade_api as tradeapi
from classes.logger import log

# Replace these with your API connection info from the dashboard
base_url = 'https://paper-api.alpaca.markets'
api_key_id = 'AKAVR4UTXSWA2UR4JT5M'
api_secret = 'PoaSvq2lHqTkPHD0jBY3pztZKXWcKiuX6QLk15cj'




class UserInteraction:

    def __init__(self):  # Creates session/logs in
        try:
            self.api = tradeapi.REST(
                base_url=base_url,
                key_id=api_key_id,
                secret_key=api_secret
            )


            self.account = self.api.get_account()
            log("Successfully logged into account.", 1)
            log('${} is available as buying power.'.format(self.account.buying_power), 1)  # Checks buying power
        except:
            log("Failed to login to account.", 2)
            quit()


    def submitOrder(self):  # FUNCTION 1
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


    def sellOrder(self):  # FUNCTION 2
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


    def displayPortfolio(self):  # FUNCTION 3
        portfolio = self.api.list_positions()
        for position in portfolio:
            log("{} shares of {}".format(position.qty, position.symbol), 1)


    def displayOrders(self):  # FUNCTION 4
        orders = self.api.list_orders()
        print(orders)


    def checkMarket(self):  # FUNCTION 5
        clock = self.api.get_clock()
        log('The market is {}'.format('open.' if clock.is_open else 'closed.'), 1)  # checks if market is open


    def checkTradable(self):  # FUNCTION 6
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


    def getAssets(self):  # FUNCTION 7
        active_assets = self.api.list_assets(status='active')
        nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']  # Finds all tickers listed on NASDAQ
        for i in nasdaq_assets:
            print(i)






