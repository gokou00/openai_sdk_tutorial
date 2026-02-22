from agents import Agent, Runner, SQLiteSession, trace , handoff, function_tool
from agents.extensions.visualization import draw_graph
from agents import GuardrailFunctionOutput, InputGuardrailTripwireTriggered, input_guardrail, RunContextWrapper, TResponseInputItem
from dotenv import load_dotenv

load_dotenv()

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


@input_guardrail
def complaint_detector_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    prompt: str | list[TResponseInputItem]
)-> GuardrailFunctionOutput:

    tripwire_triggered = False
    if "complaint" in prompt:
        tripwire_triggered = True
    
    return GuardrailFunctionOutput(
        output_info="The word complaint was detected in the prompt",
        tripwire_triggered=tripwire_triggered,
    )


agent = Agent(name="Customer Service Agent", instructions="You are an AI agent that helps responds to customer queries for a local paper company.",
    model="gpt-4o-mini", tools=[get_order_status], input_guardrails=[complaint_detector_guardrail] )


with trace("Input Guardrails"):
    while True:
        question = input("You: ")
        result = Runner.run_sync(agent, question)
        print(f"Agent: {result.final_output}")