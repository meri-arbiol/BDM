from data_collector import data_collector
from loader_idealista import loader_idealista
from loader_lookup_tables import loader_lookup_tables
from loader_income import loader_income
from loader_rent import loader_rent


if __name__ == '__main__':
    data_collector() #we apply the data collector to our new dataset added to the project
    loader_idealista()
    loader_lookup_tables()
    loader_rent()
    loader_income()
