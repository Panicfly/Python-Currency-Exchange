from dataclasses import dataclass

@dataclass
class ExchangeRate:
    eur: float
    aud: float
    gbp: float

class CurrencyConverter:
    dataCell = {"DATE": [], "RATE": []}
    chosen_rate = 1
    rates = [ExchangeRate(0, 0, 0), ExchangeRate(0, 0, 0), ExchangeRate(0, 0, 0)]

    def __init__(self):
        
        while True:
            print("ACME(tm) US DOLLAR EXCHANGE RATE APP")
            print("1) LOAD currency exchange rate data from a file")
            print("2) USE AVERAGE exchange rate")
            print("3) USE HIGHEST exchange rate")
            print("4) USE LOWEST exchange rate")
            print("5) CONVERT USD TO EUR")
            print("6) CONVERT USD TO AUD")
            print("7) CONVERT USD TO GBP")
            print("0) QUIT program")

            decision = int(input("Choose what to do: "))
            if decision == 0:
                break
            elif decision == 1:
                self.load()
            #0 is min, 1 is avg, 2 is max
            elif decision == 2:
                self.selected_rate = 1
            elif decision == 3:
                self.selected_rate = 2
            elif decision == 4:
                self.selected_rate = 0
            elif decision == 5:
                self.convert("EUR")
            elif decision == 6:
                self.convert("AUD")
            elif decision == 7:
                self.convert("GBP")
            print("")
    
    def load(self):
        self.reset()
        fileName = input("Give name of the data file: ")

        with open(fileName, "r") as file:
            next(file)
            for line in file:
                line = line.strip().split(';')
                self.dataCell["DATE"].append(line[0])
                #try:
                rate = ExchangeRate(float(line[1]), float(line[2]), float(line[3]))
                #self.check_min_max(rate)

                self.dataCell["RATE"].append(rate)
                #except ValueError:
                    #self.data["RATE"].append(Rate(0, 0, 0))  # fill with dummy data

        self.calc_avg()
        self.calc_min()
        self.calc_max()
        print("Data loaded successfully!")

        print("Currency exchange data is from {} days between {} and {}.".format(len(self.dataCell["DATE"]), self.dataCell["DATE"][0],
                                                                                    self.dataCell["DATE"][len(self.dataCell["DATE"]) - 1]))
    def calc_min(self):
        self.rates[0].eur = min(self.dataCell["RATES"],key=lambda x: x.eur)
        self.rates[0].aud = min(self.dataCell["RATES"],key=lambda x: x.aud)
        self.rates[0].gbp = min(self.dataCell["RATES"],key=lambda x: x.gbp)

    def calc_max(self):
        self.rates[2].eur = max(self.dataCell["RATES"],key=lambda x: x.eur)
        self.rates[2].aud = max(self.dataCell["RATES"],key=lambda x: x.aud)
        self.rates[2].gbp = max(self.dataCell["RATES"],key=lambda x: x.gbp)

    def calc_avg(self):
        total_eur, total_aud, total_gbp = 0, 0, 0
        for entry in self.dataCell["RATE"]:
            total_eur += entry.eur
            total_aud += entry.aud
            total_gbp += entry.gbp
        # filtering out non valid entries
        #size = len(list(filter(lambda x: x != Rate(0, 0, 0), self.data["RATE"])))
        size = len(self.data["RATE"])
        self.rates[1] = ExchangeRate(total_eur / size, total_aud / size, total_gbp / size)

    def convert(self, currency):
        amount = float(input("Give USD to convert: "))

        # currency selection
        rate = 0
        if currency == "EUR":
            rate = self.rates[selected_rate].eur
        elif currency == "GBP":
            rate = self.rates[selected_rate].gdp
        elif currency == "AUD":
            rate = self.rates[selected_rate].aud
        print("{} USD in {} is {} {}".format(amount, currency, round(amount * rate, 2), currency))