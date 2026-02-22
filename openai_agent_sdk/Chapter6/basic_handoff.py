from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()


complaints_agent = Agent(
    name="Complaints Agent",
    instructions="Handle any customer complaints with empathy and clear next steps."
)

inquiry_agent = Agent(
    name="General Inquiry Agent",
    instructions="Answer general questions about our services promptly."
)


triage_agent = Agent(
    name="Triage Agent",
    instructions="Triage the user's request and call the appropriate agent",
    handoffs=[complaints_agent,inquiry_agent]
)

while True:
    question = input("You:  ")
    result = Runner.run_sync(triage_agent,question)
    print(f"Agent: {result.final_output}")