from dataclasses import dataclass

@dataclass
class FlightData(object):
    ticket_price = "Not set"
    link_to_tickets = "Not set"
    ticket_city = "Not set"
    ticket_lowest_price_wanted = "Not set"
    ticket_IATA_code = "Not set"
    ticket_departure_IATA = "Not set"
    