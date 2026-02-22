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


def orchestrate(user_message: str) -> str:
    chosen_agent = None
    if ("complaint" in user_message.lower() or "problem" in user_message.lower()):
        print("Redirecting you to the Complaints agent...")
        chosen_agent = complaints_agent
    else:
        print("Redirecting you to the General Inquiry agent...")
        chosen_agent = inquiry_agent

    result = Runner.run_sync(chosen_agent, user_message)
    return result.final_output


while True:
    question = input("You: ")
    result = orchestrate(question)
    print(f"Agent: {result}")
