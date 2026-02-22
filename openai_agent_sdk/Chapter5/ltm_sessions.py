from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession


load_dotenv()

agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agent that answers questions.",
)

session = SQLiteSession("first_session",db_path="messages.db")

while True:
    question = input("You: ")
    result = Runner.run_sync(agent, question, session=session)
    print(f"Agent: {result.final_output}" )