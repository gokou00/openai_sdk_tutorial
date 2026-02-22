from agents import(
    Agent, Runner, SQLiteSession, trace,
    function_tool, FileSearchTool
)

import sqlite3
from agents import (
    GuardrailFunctionOutput, InputGuardrailTripwireTriggered,
    input_guardrail, RunContextWrapper, TResponseInputItem
)

from pydantic import BaseModel
from dotenv import load_dotenv
from agents.extensions.visualization import draw_graph

load_dotenv()

@function_tool
def query_orders(sql_query: str, authorization_key: str):
    """
    Executes the given SQL query on the orders table and returns the results.
    You must provide an authorization key to access the data.
    Table: orders
        order_id: INTEGER PRIMARY KEY,
        authorization_key: TEXT,
        order_status: TEXT
    Only rows matching the provided authorization_key will be accessible.
    """
    db_path = "paper_data.db"


    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sub_query = f"(SELECT * FROM orders WHERE authorization_key = {authorization_key}) a "
        filtered_query = sql_query.replace("orders", sub_query)
        cursor.execute(filtered_query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        return f"Error querying orders.db: {e}"


file_search_tool = FileSearchTool(
    vector_store_ids=["vs_6990cec75c608191aeff8f0ecd1737bf"]
)

class GuardrailTrueFalse(BaseModel):
    is_relevent_to_customer_service: bool


guardrail_agent = Agent(
    name="Guardrail check",
    instructions="You are an AI agent that checks if the user's prompt is relevant to answering customer service and order related questions",
    output_type=GuardrailTrueFalse,
)

@input_guardrail
async def relevant_detector_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    prompt: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, prompt)
    tripwire_triggered = False

    if result.final_output.is_relevent_to_customer_service == False:
        tripwire_triggered = False
    
    return GuardrailFunctionOutput(
        output_info="",
        tripwire_triggered=tripwire_triggered,
    )

retention_agent = Agent(
    name="Retention Agent",
    instructions="You are a rentention agent. Your goal is to encourage the customer not to cancel thier service, understand their pain points and empathize with their situation. If the customer insists on canelling , you may offer up to $100 credit on their account as a rentention incentive.",
    tools=[query_orders],
)


customer_service_agent = Agent(
    name="Customer Service Agent",
    instructions=(
        "Introduce yourself as the complaints agent."
        "Handle any customer complaints with empathy and clear next steps."
        "Use the file_search_tool to get general answers to questions"
        "For specific order related questions, use the query_orders tool to get the order details."
        "To use the query_order tool, you will need the user's authorization key."
    ),
    tools=[query_orders, file_search_tool],
    input_guardrails=[relevant_detector_guardrail],
    handoffs=[retention_agent],
)

session = SQLiteSession("session")
last_agent = customer_service_agent

with trace("Customer service agent"):
    while True:
        try:
            question = input("You: ")
            result = Runner.run_sync(last_agent, question, session=session)
            print(f"Agent: {result.final_output}")
            last_agent = result.last_agent
        except InputGuardrailTripwireTriggered:
            print("This comment is irrelevant to customer service.")
