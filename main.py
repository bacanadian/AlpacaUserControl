from classes.UserInteraction import UserInteraction
from classes.logger import log
from colorama import Fore


print(Fore.CYAN + "\n********************* Welcome to Alpaca's User Input Driven Program *********************\n")
session = UserInteraction()

while True:
    try:
        print()
        log("Press 1 to purchase equitites", 3)
        log("Press 2 to sell equities", 3)
        log("Press 3 to display portfolio", 3)
        log("Press 4 to display orders", 3)
        log("Press 5 to check if the market is open", 3)
        log("Press 6 to check if a stock is tradable", 3)
        log("Press 7 to list assets on the NASDAQ", 3)
        log("Press 8 to exit", 3)

        choice = int(input())

        if choice == 1:
            session.submitOrder()

        elif choice == 2:
            session.sellOrder()

        elif choice == 3:
            session.displayPortfolio()

        elif choice == 4:
            session.displayOrders()

        elif choice == 5:
            session.checkMarket()

        elif choice == 6:
            session.checkTradable()

        elif choice == 7:
            session.getAssets()

        elif choice == 8:
            break

        else:
            log("Please enter a valid option", 2)

    except:
        log("Error understanding input. Make sure to use integers", 2)

print(Fore.CYAN + "*********************                Closing Program               *********************\n\n\n")
