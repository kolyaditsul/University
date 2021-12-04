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
        obj[1] = int(obj[1])
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
        obj = split_line(market)
        obj[0] = int(obj[0])
        markets_splitted.append(obj)

    return markets_splitted 

         
# вивід списку цін
def show_prices(prices):
    """виводить список цін по заданому інтервалу кодів
    """
    # задати інтервал кодів 
    price_code_from = int(input("З якого кода ринкових цін? "))
    price_code_to = int(input("До якого кода ринкових цін? ")) 

 # відбір списку цін 
    filtered_prices = []
    for price in prices:
        if price_code_from <= price[1] <= price_code_to:
            filtered_prices.append(price)

    if len(filtered_prices) == 0:
        print('В списку цін нема таких кодів')
        return


    # вивід списку
    print('СПИСОК ЦІН')
    for price in filtered_prices:
        print(f'дата: {price[0]:20} код ринку: {price[1]:3}    ціна: картопля: {price[2]:25}  капуста: {price[3]:25} цибуля: {price[4]:25}')
         
# вивід списку ринків 
def show_markets(markets):
    """виводить список ринків по заданому інтервалу кодів
    """ 
    #задати інтервал кодів
    market_code_from = int(input("З якого кода ринків? ")) 
    market_code_to = int(input("До якого кода ринків? ")) 

    # відбір списку ринків 
    filtered_markets = []
    for market in markets:
        if market_code_from <= market[0] <= market_code_to:
            filtered_markets.append(market)

    if len(filtered_markets) == 0:
        print('В списку цін нема таких кодів')
        return


    # вивід списку 
    print('СПИСОК РИНКІВ')
    for market in filtered_markets:
        print(f'код ринку: {market[0]:3} найменування ринку: {market[1][:-1]:20}')              

if __name__ == '__main__':
    prices = get_prices()
    markets = get_markets()

    show_prices(prices)
    show_markets(markets)

pass

