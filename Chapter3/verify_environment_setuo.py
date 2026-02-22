import os
from dotenv import load_dotenv
from agents import Agent, Runner


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY not found. Please set it in your .env file.")
else:
    print("API Key loaded successfully.")

agent = Agent(name="Echo Agent", instructions="Return the words 'Setup successful' ")

result = Runner.run_sync(agent, "Run setup")
print(result.final_output)

