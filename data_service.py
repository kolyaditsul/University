# модуль призначено для роботи з зовнішніми файлами
# читання та виведення для візуального контролю


def get_prices():
    """читання файла цін `prices`
    та формування списку цін
    повертає список цін
    """
    # накопичення даних файлу у списку
    with open("./data/prices.csv", 'r') as f:
         prices = f.readlines()
  
    # підготовка даних для подальшої обробки 
    prices_splitted = []
    # порізати в циклі строки на окремі елементи
    for price in prices:
        obj = split_line(price)
        prices_splitted.append(obj)

    return prices_splitted

def split_line(line):
    """повертає список обєктів з строки """ 
    object = line.split(',')
    return object          

 
 
# читання файлу `markets`
def get_markets():
    """читання файла ринків `markets`
    та формування списку ринків
    повертає список ринків
    """
    # накопичення даних файлу у списку
    with open("./data/markets.csv",'r') as f:
        markets = f.readlines()

    # підготовка подальшої обробки
    markets_splitted = []
    # порізати в циклі строки на окремі елементи
    for market in markets:
        object = split_line(market)
        markets_splitted.append(object)

    return markets_splitted 

def split_line(line):
    """повертає список обєктів з строки """ 
    object = line.split(',')
    return object          
      


# вивід списку цін
def show_prices():
    """виводить список цін по заданому інтервалу кодів
    """
    # задати інтервал кодів 
    price_code_from = int(input("З якого кода цін"))
    price_code_to = int(input("До якого кода цін ?"))

    pass 

# вивід списку ринків

if __name__ == '__main__':
    prices = get_prices()
    markets = get_markets()

    rc = show_prices
    pass

