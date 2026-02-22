from agents import Agent, Runner, FileSearchTool, SQLiteSession
from dotenv import load_dotenv

load_dotenv()


filesearchtool = FileSearchTool(
    vector_store_ids=["vs_697a95de3a18819197a2c9c2c4626810"]
)

agent = Agent(
    name="USConstitutionTool",
    instructions="You are a an AI agent that answers questions from the listed vector store, which has the US Constitution. Answer in one sentence.",
    tools=[filesearchtool]
)

session = SQLiteSession("first_session")

while True:
    question = input("You: ")
    result = Runner.run_sync(agent, question, session=session)
    print(f"Agent: {result.final_output}")