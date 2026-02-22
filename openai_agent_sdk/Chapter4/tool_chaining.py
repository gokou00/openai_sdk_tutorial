from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
from typing import List
from pydantic import BaseModel


load_dotenv()

@function_tool
def get_customer_orders(customer_id: str) -> List[str]:
    """
    Retrieve all order IDs associated with a given customer ID.
    """

    if customer_id == "CUST123":
        return ["ORD001", "ORD002", "ORD003"]


@function_tool
def get_order_information(order_id: str) -> str:
    """
    Fetch detailed information about a specific order
    """

    status_map = {
        "ORD001": "Shipped",
        "ORD002": "Processing",
        "ORD003": "Delivered"
    }

    return f"Order {order_id} is currently {status_map.get(order_id, 'Unknown')}"


customer_service_agent = Agent(
    name="CustomerSupportAgent",
    instructions="You are a customer service assistant.",
    tools=[get_customer_orders, get_order_information]
)

result = Runner.run_sync(customer_service_agent, "Please check on the status of my orders? My customer ID is CUST123")
print(result.final_output)