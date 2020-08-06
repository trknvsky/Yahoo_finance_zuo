import csv

COMPANIES_DATA = []
CLOSED_PRICES = []
EDITED_PRICES = []


class CSVFile:
    WRITE = 'w'
    READ = 'r'
    DELIMITER = ','
    HEADERS = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', '3days_before_change']

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, self.READ) as file:
            reader = csv.DictReader(file, delimiter=self.DELIMITER)
            for line in reader:                             
                CLOSED_PRICES.append(float(line['Close']))
                COMPANIES_DATA.append(line)
                line['3days_before_change'] = 0              
            step_counter = 3
            for price in CLOSED_PRICES:
                if step_counter != len(CLOSED_PRICES):
                    price /= CLOSED_PRICES[step_counter]
                    EDITED_PRICES.append(price)
                    step_counter += 1

            companies_counter = 0
            for company in COMPANIES_DATA:
                company['3days_before_change'] = EDITED_PRICES[companies_counter]
                companies_counter += 1
                if companies_counter == (len(COMPANIES_DATA)) - 3:
                    break

    def write(self, data):
        with open(self.filename, self.WRITE, newline='') as file:
            writer = csv.DictWriter(file, delimiter=self.DELIMITER, fieldnames=self.HEADERS)
            writer.writeheader()
            writer.writerows(data)
            file.close()
