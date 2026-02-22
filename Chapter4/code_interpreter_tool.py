from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, CodeInterpreterTool
from typing import List
from pydantic import BaseModel
from agents.tool import CodeInterpreter



load_dotenv()


tool_config = CodeInterpreter(
    type="code_interpreter",
    container={"type":"auto"}
)

codetool = CodeInterpreterTool(tool_config=tool_config)

agent = Agent(
    name="CodeTool",
    instructions="You are an AI agent that writes and runs python code to answer questions.",
    tools=[codetool],
)

result = Runner.run_sync(agent, "What is my monthly payment for a $800,000 mortage at 6% for 30 years?")
print(result.final_output)