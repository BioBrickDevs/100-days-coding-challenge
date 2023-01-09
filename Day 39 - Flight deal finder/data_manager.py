import pymongo
import flight_search
import dotenv
import os
dotenv.load_dotenv()

MONGODB_SECRET = os.environ.get("MONGODB_SECRET")


class DataManager:

    client = pymongo.MongoClient(MONGODB_SECRET)
    db = client.flight_search
    collection = db.flight_search_data

    def insert_data(self):
        want_to_continue = True
        print("Welcome to insert new data to for flight search.\n")
        while want_to_continue:
            city = input("Give city: ")
            lowest_price_to_accept = input("Give lowest price to accept:")

            data = {"City": city,
                    "IATA Code": "",
                    "Lowest Price": lowest_price_to_accept,
                    }
            collection = self.collection
            collection.insert_one(data)
            print("Data inserted.")
            choice = input("Do you want, to continue? Y/N: ")
            if choice.lower() == "n":
                want_to_continue = False

    def fill_empty_IATA_codes(self):
        collection = self.collection
        result = collection.find({"IATA Code": ""})
        for row in result:
            city = row["City"]
            IATA_code = flight_search.FlightSearch.get_IATA_code_for_city(city)
            collection.update_one(
                {"City": city}, {"$set": {"IATA Code": IATA_code}})

    def get_all_cities(self):
        collection = self.collection
        result = collection.find({})
        data_to_return = {data["City"]: {"IATA": data["IATA Code"],
                                         "lowest price": data["Lowest Price"]}
                          for data in result}
        return dict(data_to_return)


# DataManager.fill_empty_IATA_codes(self=DataManager)

#DataManager.insert_data(self=DataManager)
# DataManager.get_all_cities(self=DataManager)
