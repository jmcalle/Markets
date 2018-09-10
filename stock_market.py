import requests
import json
import pandas

basic_url = "/stock/market/collection/sector?"
#[{"symbol":"LLY","companyName":"Eli Lilly and Company","primaryExchange":"New York Stock Exchange","sector":"Healthcare","calculationPrice":"close","open":104.8,"openTime":1534944649727,"close":105.03,"closeTime":1534968194572,"high":105.63,"low":104.15,"latestPrice":105.03,"latestSource":"Close","latestTime":"August 22, 2018","latestUpdate":1534968194572,"latestVolume":1928288,"iexRealtimePrice":105.03,"iexRealtimeSize":100,"iexLastUpdated":1534967996704,"delayedPrice":105.03,"delayedPriceTime":1534968194572,"extendedPrice":105.03,"extendedChange":0,"extendedChangePercent":0,"extendedPriceTime":1534971514709,"previousClose":105.07,"change":-0.04,"changePercent":-0.00038,"iexMarketPercent":0.03125,"iexVolume":60259,"avgTotalVolume":4048281,"iexBidPrice":0,"iexBidSize":0,"iexAskPrice":0,"iexAskSize":0,"marketCap":112800944516,"peRatio":20.88,"week52High":106.38,"week52Low":73.69,"ytdChange":0.26471398167944443},{"symbol":"CYH","companyName":"Community Health Systems Inc.","primaryExchange":"New York Stock Exchange","sector":"Healthcare","calculationPrice":"close","open":3.47,"openTime":1534944668337,"close":3.6,"closeTime":1534968129712,"high":3.64,"low":3.41,"latestPrice":3.6,"latestSource":"Close","latestTime":"August 22,

sector = "Financials"

list_url = "https://min-api.cryptocompare.com/data/all/coinlist"
# headers = {} no OAuth nor special header authentication is required at this point


class Stock_Controller:

    list_payload = {'CollectionName': 'Financials' }

    def __init__(self):
        coins = []
        list = List()
        List().get_list()
        List().get_price()

    #Deprecated
    def get_data(self):
        r = requests.get(basic_url, params=self.list_payload)


class List:
    def __init__(self, coin=None):
        self.coin_df = pandas.DataFrame()
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
            elif id == "price":
                self.json_response = requests.get(basic_url + multiprice, params=price_payload)
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
#            print(coin["CoinInfo"]["Id"])
            i += 1
            coin_s = pandas.Series([i, coin["CoinInfo"]["Name"],
                                   coin["CoinInfo"]["FullName"],
                                   float(coin["ConversionInfo"]["Supply"]),
                                   float(coin["ConversionInfo"]["TotalVolume24H"])],
                                   index=['id', 'coin', 'desc', 'supply', '24h_total'],
                                   name=coin["CoinInfo"]["Name"])
            self.coin_df = self.coin_df.append(coin_s)
#Pre-ordered by Volume self.coin_df = self.coin_df.sort_values(by=['sortOrder'], ascending=True)
#        print(self.coin_df.head(n=600))

    def get_price(self, option=None, list_coins=None):
        #[{'CoinInfo': {'Id': '1182', 'Name': 'BTC', 'FullName': 'Bitcoin', 'Internal': 'BTC', 'ImageUrl': '/media/19633/btc.png', 'Url': '/coins/btc/overview', 'Algorithm': 'SHA256', 'ProofType': 'PoW', 'NetHashesPerSecond': 45737209658.535, 'BlockNumber': 538046, 'BlockTime': 600, 'BlockReward': 12.5, 'Type': 1, 'DocumentType': 'Webpagecoinp'}, 'ConversionInfo': {'Conversion': 'direct', 'ConversionSymbol': '', 'CurrencyFrom': 'BTC', 'CurrencyTo': 'USD', 'Market': 'CCCAGG', 'Supply': 17225575, 'TotalVolume24H': 325569.376142334, 'SubBase': '5~', 'SubsNeeded': ['5~CCCAGG~BTC~USD'], 'RAW': ['5~CCCAGG~BTC~USD~4~6417.11~1534996438~1.2~7686.839999999999~284447909~8332.281260159452~53603466.17972497~89019.99861014445~578685640.9575375~6366.13~6447.01~6356.96~6740.43~6770.17~6260.38~Bitfinex~7ffe9']}}, {'CoinInfo': {'Id': '7605', 'Name': 'ETH', 'FullName': 'Ethereum', 'Internal': 'ETH', 'ImageUrl': '/media/20646/eth_logo.png', 'Url': '/coins/eth/overview', 'Algorithm': 'Ethash', 'ProofType': 'PoW', 'NetHashesPerSecond': 264128594468356, 'BlockNumber': 6196911, 'BlockTime': 15, 'BlockReward': 3, 'Type': 1, 'DocumentType': 'Webpagecoinp'}, 'ConversionInfo': {'Conversion': 'direct', 'ConversionSymbol': '', 'CurrencyFrom': 'ETH', 'CurrencyTo': 'USD', 'Market': 'CCCAGG', 'Supply': 101495408.2803, 'TotalVolume24H': 3227835.7019727128, 'SubBase': '5~', 'SubsNeeded': ['5~CCCAGG~ETH~USD'], 'RAW': ['5~CCCAGG~ETH~USD~4~272.06~1534996440~0.17530695~47.737835554499995~39229810~65718.18302483085~18044022.626775924~627306.4115398205~173466937.9230377~270.36~275.5~269.09~291.57~292.72~259.23~Coinbase~7ffe9']}}
        self.load_json(action="price")
        print(self.json_response)


    def get_sector(self, option=None, list_coins=None):
        i = 0
        i += 1

#mycoin = Stock_Controller()