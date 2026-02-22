from agents import Agent, Runner, SQLiteSession, trace , handoff
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

comapliants_agent = Agent(
    name="Complaints Agent",
    instructions="Introduce yourself as the complaints agent. Handle any customer complaints with empathy and clear next steps."
)

sales_agent = Agent(
    name="Sales Agent",
    instructions="Introduce yourself as the sales agent. Answer general questions about our services promptly."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Answer general questions. Triage the user's request and call the appropriate agent"
)


class NameOfAgentToBeHandedOff(BaseModel):
    name_of_agents_to_be_handed_off: str

def log(ctx,name_of_agent):
    msg = f"The system has transferred you to another agent: {name_of_agent.name_of_agents_to_be_handed_off}"
    print(msg)


complaints_handoff = handoff(
    agent=comapliants_agent,
    on_handoff=log,
    input_type=NameOfAgentToBeHandedOff
)

sales_handoff = handoff(
    agent=sales_agent,
    on_handoff=log,
    input_type=NameOfAgentToBeHandedOff
)

triage_handoff = handoff(
    agent=triage_agent,
    on_handoff=log,
    input_type=NameOfAgentToBeHandedOff
)

comapliants_agent.handoffs = [sales_handoff,triage_handoff]
sales_agent.handoffs = [complaints_handoff,triage_handoff]
triage_agent.handoffs = [complaints_handoff,sales_handoff]

session = SQLiteSession("first_session")
last_agent = triage_agent

with trace("Multi-agent system"):
    while True:
        question = input("You: ")
        result = Runner.run_sync(last_agent, question, session=session)
        print(f"Agent: {result.final_output}")
        last_agent = result.last_agent