from agents import Agent, Runner
from agents.model_settings import ModelSettings
from dotenv import load_dotenv


load_dotenv()

creative_agent = Agent(
    name="CreativeAgent",
    instructions="You are an AI agent that answers questions.",
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=1.0,
        max_tokens=300,
    )
)

precise_agent=Agent(
    name="PreciseAgent",
    instructions="You are an AI agent that answers questions.",
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=0.2,
        max_tokens=50,
    )
)

prompt= "Describe the future of AI in customer service."



print("Running CreativeAgent...")
response=Runner.run_sync(creative_agent, prompt)
print(f"CreativeAgent response: {response.final_output}")
print("--------------------------------")

print("Running PreciseAgent...")
response=Runner.run_sync(precise_agent, prompt)
print(f"PreciseAgent response: {response.final_output}")
print("--------------------------------")