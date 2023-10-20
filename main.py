import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """ Check the hotels availability """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        print(availability)
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.hotel = hotel_object
        self.customer_name = customer_name
        pass

    def generate(self):
        content = f"""
        Thankyou for your reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


if __name__ == '__main__':
    print(df)
    id = input("Enter the id of the hotel: ")
    hotel = Hotel(id)
    if hotel.available():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("This hotel is not available")