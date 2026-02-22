from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, CodeInterpreterTool , HostedMCPTool
from typing import List
from pydantic import BaseModel
from agents.tool import CodeInterpreter , Mcp



load_dotenv()

tool_config = Mcp(
    server_label="CryptocurrencyPriceFetcher",
    server_url="https://mcp.api.coingecko.com/sse",
    type="mcp",
    require_approval="never"
)

mcp_tool = HostedMCPTool(tool_config=tool_config)

agent = Agent(
    name="Crypto Agent",
    instructions="You are an AI agent that return crypto prices.",
    tools = [mcp_tool],
)

result = Runner.run_sync(agent, "What is the price of Bitcoin?")
print(result.final_output)