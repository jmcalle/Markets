import requests
import json
import pandas

basic_url = "https://min-api.cryptocompare.com/data/"
topvol_url = "https://min-api.cryptocompare.com/data/top/totalvol?limit=300&tsym=USD"
hist_exec = "histoday"
fiat = "USD"
# https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,ADA,XRP,ENJ&tsyms=USD
multiprice = "pricemultifull"
list_url = "https://min-api.cryptocompare.com/data/all/coinlist"
# headers = {} no OAuth nor special header authentication is required at this point
price_payload = {'fsyms': 'BTC', 'tsyms': 'USD'}

top_exec = "top/volumes"


class Controller:
    list_payload = {'tsym': 'BTC', 'limit': '600'}

    def __init__(self):
        coins = []
        self.listcoin = List()
        self.listcoin.get_list()
        self.listcoin.get_price()
        print("apetekan")

# Deprecated
    def get_data(self):
        r = requests.get(basic_url + top_exec, params=self.list_payload)

    def get_list(self):
        return self.listcoin.merge_price()


class List:
    price_df: DataFrame

    def __init__(self, coin=None):
        self.coin_df = pandas.DataFrame()
        self.price_df = pandas.DataFrame()
        self.json_response = {}
        # print(self.coin_matrix.to_string)

    def load_json(self, action: None, option=None) -> object:
        if option == "disk":
            with open(option, 'r') as infile:
                self.json_response = json.load(infile)
        else:
            if action == "list":
                self.json_response = requests.get(topvol_url)
                self.json_response = json.loads(self.json_response.text)
            elif action == "price":
                self.json_response = requests.get(basic_url + multiprice,params=price_payload)
                self.json_response = json.loads(self.json_response.text)

    def dump_json(self, option=None, action=None):
        # Action takes either of the following values: list, current_price, historical, analysis (TBD)
        # Include try except to avoid issues
        if option == "disk":
            with open(option, 'w') as outfile:
                outfile.truncate()
                json.dump(self.json_response.text, outfile)
            # self.json_response, outfile)
        else:
            None

    def get_list(self, option=None, list_coins=None):
        self.load_json(action="list", option=option)
        self.dump_json(action="list", option=option)
        print(self.json_response['Data'])
        i = 0
        for coin in self.json_response["Data"]:
            i += 1
            coin_s = pandas.Series([i, coin["CoinInfo"]["Name"],
                                    coin["CoinInfo"]["FullName"],
                                    float(coin["ConversionInfo"]["Supply"]),
                                    float(coin["ConversionInfo"]["TotalVolume24H"])],
                                   index=['id', 'coin', 'desc', 'supply', '24h_total'],
                                   name=coin["CoinInfo"]["Name"])
            self.coin_df = self.coin_df.append(coin_s)

    # Pre-ordered by Volume self.coin_df = self.coin_df.sort_values(by=['sortOrder'], ascending=True)
    #        print(self.coin_df.head(n=600))

    def get_price(self, option=None, list_coins=None):
        self.load_json(action="price", option=option)
        self.dump_json(action="price", option=option)
        print(self.json_response)
        for coin in self.json_response["RAW"]:
            print(self.json_response["RAW"][coin]["USD"]["FROMSYMBOL"])
            price_s = pandas.Series([self.json_response["RAW"][coin]["USD"]["FROMSYMBOL"],
                                     self.json_response["RAW"][coin]["USD"]["PRICE"],
                                     self.json_response["RAW"][coin]["USD"]["OPENDAY"],
                                     self.json_response["RAW"][coin]["USD"]["HIGHDAY"],
                                     self.json_response["RAW"][coin]["USD"]["LOWDAY"],
                                     self.json_response["RAW"][coin]["USD"]["CHANGEDAY"],
                                     self.json_response["RAW"][coin]["USD"]["MKTCAP"]],
                                     index=['id', 'price', 'openday', 'highday', 'lowday', 'changeday', 'mktcap'],
                                     name=self.json_response["RAW"][coin]["USD"]["FROMSYMBOL"])
            self.price_df = self.price_df.append(price_s)

    def merge_price(self):
        self.coin_df.merge(self.price_df, how="right", left_on="id", right_on="id")
        print(self.coin_df.to_string)
        return self.coin_df


mycoin = Controller()