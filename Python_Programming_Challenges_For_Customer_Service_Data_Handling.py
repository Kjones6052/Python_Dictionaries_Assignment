# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
# Example ticket structure:
# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }
# Problem Statement: Develop a program that:
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
service_tickets = {}

def new_service_ticket():
    customer_name = input("What is the customer's name?: ").lower()
    customer_issue = input("What issue do they need to resolve?: ").lower()
    ticket_status = "open"
    ticket = {f"Customer Name": {customer_name}, "Issue": {customer_issue}, "Status": {ticket_status}}
    ticket_id = id(ticket)
    service_tickets[ticket_id] = [ticket]
    print(f"Your service ticket is now being processed. Service ticket information: {ticket_id}: {ticket}")

def close_service_ticket():
    service_ticket_id = input("What is the service ticket number you would like to close?: ")
    if service_ticket_id in service_tickets.keys():
        service_tickets["Status"] = "closed"
        print(f"Service ticket: {service_ticket_id} is now closed.")
    elif service_ticket_id in service_tickets.keys():
        print("Service ticket number not found.")

def view_service_tickets():
    print(service_tickets)

while True:
    user_input = input(f"Options: Enter New Ticket, Close Open Ticket, View Tickets, Quit\n What would you like to do?: ").lower()
    if user_input == "quit":
        break
    elif user_input == "enter new ticket":
        new_service_ticket()
    elif user_input == "close open ticket":
        close_service_ticket()
    elif user_input == "view tickets":
        view_service_tickets()
    else:
        print("I'm sorry, I didn't understand.")
        continue