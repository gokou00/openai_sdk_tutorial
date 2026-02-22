from agents import Agent, Runner, SQLiteSession, trace , handoff, function_tool, custom_span
from dotenv import load_dotenv
import time

load_dotenv()

agent = Agent(
    name="QuestionAnswerAgent",
    instructions="You are an AI agent that answers questions in as few words as possible"
)

with trace("Henry's workflow"):
    with custom_span("Task 1"):
        result = Runner.run_sync(agent,"Where is the statue of Liberty?")
        print(result.final_output)
    with custom_span("Task 2"):
        result = Runner.run_sync(agent,"Where is the Eiffel Tower?")
        print(result.final_output)
    with custom_span("Task 3"):
        result = Runner.run_sync(agent,"Where is the Notre Dame?")
        print(result.final_output)
    with custom_span("Task 4"):
        result = Runner.run_sync(agent,"Where is Burj Khalifa?")
        print(result.final_output)
