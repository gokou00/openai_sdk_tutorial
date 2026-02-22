from dotenv import load_dotenv
from agents import Agent, Runner





load_dotenv()

agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agent that answers questions.",
)

messages = []

while True:
    question = input("You: ")
    messages.append({
        "role": "user",
        "content": question
    })
    result = Runner.run_sync(agent, messages)
    print(f"Agent:  {result.final_output}")
    #messages.append({
    #    "role":"assistant",
    #    "content": result.final_output
    #})
    messages = result.to_input_list()


