import os
from dotenv import load_dotenv
from agents import Agent, Runner , function_tool




@function_tool
def get_order_status(orderID: str) -> str:
    """
    Get the status of an order by its ID.
    """
    if orderID in (100,101):
        return "Delivered"
    elif orderID in (200,201):
        return "Delayed"
    elif orderID in (300,301):
        return "Canceled"
    else:
        return "Not Found"

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

customer_retention_agent = Agent(
    name="Customer Retention Agent",
    instructions="You are an AI agent that responds to customers that want to close their accounts and retains their business. Be very courteous , relatable, and kind. Offer discounts up to 10% if it helps",
    model="gpt-4o-mini"
)

agent = Agent(name="Customer Service Agent", instructions="You are an AI agent that helps responds to customer queries for a local paper company.",
    model="gpt-4o-mini", tools=[get_order_status], handoffs=[customer_retention_agent])

result = Runner.run_sync(agent, "I want to cancel my order and account. You delayed my order for the 3rd time!")
print(result.final_output)