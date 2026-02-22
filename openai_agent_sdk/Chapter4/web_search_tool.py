from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, WebSearchTool
from typing import List
from pydantic import BaseModel


load_dotenv()

websearchtool = WebSearchTool(user_location={
    "type":"approximate",
    "country":"CA",
    "city":"Toronto",
    "region":"Ontario",
})

agent = Agent(
    name="WebTool",
    instructions="You are an AI agent that answer web questions. Answer in one sentence.",
    tools=[websearchtool],
)

result = Runner.run_sync(agent, "What are the top 3 Italian restaurants?")
print(result.final_output)
