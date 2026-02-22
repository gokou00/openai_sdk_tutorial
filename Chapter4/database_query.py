from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
from typing import List
from pydantic import BaseModel

load_dotenv()


#Create a sim database

TICKETS_DB = {
    "henry@gmail.com":[
        {"id":"TCKT-001", "issue":"Login not working","status":"resolved"},
        {"id":"TCKT-002", "issue":"Password reset failed","status":"open"},
    ],
    "tom@gmail.com":[
        {"id":"TCKT-003", "issue":"Billing issue","status":"in progress"},
        
    ],
}

class CustomerQuery(BaseModel):
    email: str



@function_tool
def get_customer_tickets(query: CustomerQuery) -> str:
    """
    Retrive recent support tickets for a customer based on email.

    """

    tickets = TICKETS_DB.get(query.email.lower())

    if not tickets:
        return f"No tickets found for {query.email}"
    
    response = "\n".join([f"Ticket ID: {ticket['id']}, Issue: {ticket['issue']}, Status: {ticket['status']}" for ticket in tickets])

    return f"Tickets for {query.email}:\n{response}"



support_agent = Agent(
    name="SupportHelper",
    instructions="You are a customer support agent. Use tools to fetch user support history when asked about their tickets",
    tools=[get_customer_tickets]
)

result = Runner.run_sync(support_agent, "Can you show me the ticket history for henry@gmail.com?")
print(result.final_output)