from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, CodeInterpreterTool, WebSearchTool
from typing import List
from pydantic import BaseModel
from agents.tool import CodeInterpreter



load_dotenv()


websearchtool = WebSearchTool()
location_agent = Agent(
    name="LocationAgent",
    instructions = "You are an AI agent that searches the web and gets the latitude and longitude numbers for a particular city.",
    tools = [websearchtool],
)

tool_config = CodeInterpreter(
    type="code_interpreter",
    container={"type":"auto"}
)

codetool = CodeInterpreterTool(tool_config=tool_config)

distance_calculator_agent = Agent(
    name="DistanceCalculatorAgent",
    instructions="You are an AI agent that writes and runs python code to calculate the distance in KM between two latitude and longitude points.",
    tools = [codetool],
)


agent = Agent(
    name="Agent",
    instructions="You are an AI agent that calculates the distance between two locations. Use the Location Agent to get the latitude/longitude. Use the distance calculator agent to calculate the distance",
    tools = [
        location_agent.as_tool(
            tool_name="LocationAgent",
            tool_description="Returns the latitude and longitude for a particular location",
        ),
        distance_calculator_agent.as_tool(
            tool_name="DistanceCalculatorAgent",
            tool_description="Calculates the distance between two latitude and longitude points",
        ),
    ]
)

result = Runner.run_sync(agent, "What is the straight line distance between Toronto and Vancouver?")
print(result.final_output)