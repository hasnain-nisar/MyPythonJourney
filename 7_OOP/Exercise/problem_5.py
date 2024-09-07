'''
Write a Class 'Train' which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.
'''

class Train:
    def __init__(self, name, fare, total_seats):
        self.name = name
        self.fare = fare
        self.total_seats = total_seats
        self.booked_seats = 0

    def get_stats(self):
        # Print the current status of available train seats
        available_seats = self.total_seats - self.booked_seats
        print(f"{self.name}: Available Seats: {available_seats}")

    def get_fair_info(self):
        print(f"The fair for {self.name} is: {self.fare} per ticket.")

    def book_ticket(self):
        # Book a tocket of seats are available
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print(f'Ticket booked successfully for {self.name}')
        else:
            print(f"Sorry! No seats available for {self.name}")

# Example of how to use the train class
train1 = Train('xyz Express', 1500, 5)

# Get status of seats
train1.get_stats()

# Get fair info
train1.get_fair_info()

# Book a ticket
train1.book_ticket()

# Check status after booking a ticket.
train1.get_stats()