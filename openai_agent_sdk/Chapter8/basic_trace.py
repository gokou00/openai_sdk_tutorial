from agents import Agent, Runner, SQLiteSession, trace , handoff, function_tool
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="QuestionAnswerAgent",
    instructions="You are an AI agent that answers questions in as few words as possible"
)

result = Runner.run_sync(agent,"Where is the Eiffel Tower?")
print(result.final_output)