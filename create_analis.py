"""Модуль призначено для формування аналізу,
який формується з файлів `prices` та `markets`"""

from data_service import get_prices,get_markets 

TITLE = "Аналіз середніх ринкових цін на основі продуктів споживчого кошика"
HEADER = \
"""
=======================================================================================================================
 Код ринку    :  Найменування ринку :      Дата :                Ціна,                            Середня ціна
=======================================================================================================================                                       
                                                        Картопля:    Капуста:    Цибуля:
=======================================================================================================================                                                     
""" 

prices = get_prices() 
markets = get_markets()

def find_market_name(market_code):
    """шукає в довіднику назву ринку по його коду"""

    for market in markets:
        if market_code == market[0]:
           return market[1]

    return "нема назви"


def str_to_num(str_num):
    """повертає строкове число в число"""
    if str_num.isnumeric():
        return int(str_num)
    else:
        return int(str_num[:-1])
    
      

 
def show_analis(analizu):

    print(TITLE)
    print(HEADER)
    for row in analizu:
        print(f"{row['code']:5}",
        f"{row['market']:20}",
        f"{row['date']:20}",
        f"{row['price kartoplya']:15}",
        f"{row['price kapusta']:15}",
        f"{row['price tsubulya']:15}",
        f"{row['average']:10.2f}")
         

    
analis = {
    'cod'              : "",     # код ринку               (markets)
    'market'           : "",     # найменування ринку      (marktes)
    'date'             : "",     # дата                    (prices)
    'price kartoplya'  : 0.0,    # ціна, картопля          (prices)
    'price kapusta'    : 0.0,    # ціна, капуста           (prices)
    'price tsubulya'   : 0.0,    # ціна, цибуля            (prices)
    'average'          : 0.0     # середня ціна            ((price kartoplya + price kapusta + price tsubulya) / 3 )
}

 

analises = []
for price in prices:
    analis['cod']= price[1]
    analis['date'] = price[0]
    analis['price kartoplya'] = price[2]
    analis['price kapusta'] = price[3]
    analis['price tsubulya'] = price[4]
    analis['average'] = (str_to_num(price[2]) + str_to_num(price[3]) + str_to_num(price[4])) / 3
    analis['market'] = find_market_name(price[1])
     
    analises.append(analis) 
    
  
 
pass
