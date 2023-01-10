from data_manager import DataManager
from flight_search import FlightSearch
import time
from concurrent.futures import ThreadPoolExecutor
pool = ThreadPoolExecutor(max_workers=3)
results = 0


def handle_task(key, value):
    global results
    IATA = value["IATA"]
    city = key
    data = FlightSearch.get_cheap_flight_from_to("HEL", IATA)
    new_data = data

    results += 1
    print(results)
    new_data.ticket_IATA_code = value["IATA"]
    print(city, new_data.ticket_IATA_code, new_data.ticket_price, flush=True)
    print(new_data.link_to_tickets,  flush=True)

    if new_data.ticket_price != "no price":
        if int(new_data.ticket_price) <= int(value["lowest price"]):
            print("send mail", flush=True)
    print("------------------------------------", flush=True)
    return None


futures = []
DataManager.fill_empty_IATA_codes(self=DataManager)
cities = DataManager.get_all_cities(self=DataManager)
start = time.time()
for city, info in cities.items():
    future = pool.submit(handle_task, city, info)
    futures.append(future)

pool.shutdown()
print("Prosesses are shutdown!")
end = time.time()
print(end- start, results)
