from agents import Agent, Runner, SQLiteSession, trace , handoff
import time
from dotenv import load_dotenv


load_dotenv()

gpt4o_agent = Agent(
    name="GPT4o Agent",
    instructions="You are an AI agent",
    model="gpt-4o"
)

o3pro_agent=Agent(
    name="o3-pro Agent",
    instructions="You are an AI agent",
    model="o3-pro"
)

prompt= "How many integers from 1 to 10000 (inclusive) are divisible by 3 or 5 but not by both? Do reasoning but only return the answer."


print("Running GPT4o Agent...")
start_fast=time.time()
response=Runner.run_sync(gpt4o_agent, prompt)
print(f"GPT4o Agent response: {response.final_output}")
end_fast=time.time()
print(f"GPT4o Agent time: {end_fast-start_fast} seconds")
print("--------------------------------")

print("Running o3-pro Agent...")
start_slow=time.time()
response=Runner.run_sync(o3pro_agent, prompt)
print(f"o3-pro Agent response: {response.final_output}")
end_slow=time.time()
print(f"o3-pro Agent time: {end_slow-start_slow} seconds")
print("--------------------------------")
