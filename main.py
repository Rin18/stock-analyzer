import pandas as pd
import numpy as np
import yfinance as yf

def main():
    symbol = get_input("symbol")
    period = get_input("period")
    interval = get_input("interval")
    print(yf.Ticker(symbol).history(period, interval))


def get_input(type):
    allowed_input = ("symbol", "period", "interval")
    if type in allowed_input:
        match type:
            case "symbol":
                print("Please enter a symbol:")
                userinput = input()
                if validate_input(type, userinput):
                    return userinput
                else:
                    print("symbol invalid, please enter again:")
                    return get_input(type)
            case "period":
                print("Please enter a period, options(1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max):")
                userinput = input()
                if validate_input(type, userinput):
                    return userinput
                else:
                    print("period invalid, please enter again:")
                    return get_input(type)
            case "interval":
                print("Please enter a interval, options(1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo):")
                userinput = input()
                if validate_input(type, userinput):
                    return userinput
                else:
                    print("interval invalid, please enter again:")
                    return get_input(type)
    else:
        print("input invalid, please enter again:")
    
def validate_input(type, input):
    match type:
        case "symbol":
            if len(input) >= 10:
                return False
            else:
                return True
        case "period":
            if len(input) >= 4:
                return False
            else:
                return True
        case "interval":
            if len(input) >= 4:
                return False
            else:
                return True



if __name__ == "__main__":
    main()