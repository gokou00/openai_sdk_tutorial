from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, CodeInterpreterTool , HostedMCPTool
from typing import List
from pydantic import BaseModel
from agents.tool import CodeInterpreter , Mcp



load_dotenv()

agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agent that answers questions.",
)

messages = []

messages.append({
    "role": "user",
    "content": "How hot is the sun?"
})

result = Runner.run_sync(agent, messages)
print(result.final_output)

messages.append({
    "role": "assistant",
    "content": result.final_output
})

messages.append({
    "role": "user",
    "content": "how big is it?"
})

result = Runner.run_sync(agent, messages)
print(result.final_output)