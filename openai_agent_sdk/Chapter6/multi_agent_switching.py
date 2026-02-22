from agents import Agent, Runner, SQLiteSession, result, trace
from agents.memory import session
from dotenv import load_dotenv



load_dotenv()


complaints_agent = Agent(
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

complaints_agent.handoffs = [sales_agent,triage_agent]
sales_agent.handoffs = [complaints_agent,triage_agent]
triage_agent.handoffs = [complaints_agent,sales_agent]

session = SQLiteSession("first_session")
last_agent = triage_agent

with trace("Multi-agent system"):
    while True:
        question = input("You:  ")
        result = Runner.run_sync(last_agent,question,session=session)
        print(f"Agent: {result.final_output}")
        last_agent = result.last_agent