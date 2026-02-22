from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, ImageGenerationTool
from typing import List
from pydantic import BaseModel
from agents.tool import ImageGeneration


load_dotenv()

tool_config = ImageGeneration(
    type="image_generation",
)

imagetool = ImageGenerationTool(tool_config=tool_config)

agent = Agent(
    name="ImageTool",
    instructions="You are an AI agent that generates images.",
    tools=[imagetool],
)

result = Runner.run_sync(agent, "Generate an image of a elephant.")
print(result.final_output)
