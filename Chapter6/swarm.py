from agents import Agent, Runner, SQLiteSession, trace , handoff
import concurrent.futures
from dotenv import load_dotenv


load_dotenv()


roles = [
    "Urban Planner","Artist","Chef","Engineer","Teacher","Doctor","Mechanic","Lawyer","Historian","Environmentalist"
]

city_agents = [
    Agent(
        name=f"{role} Agent",
        instructions=f"You are a {role.lower()}. Answer the question: 'If you were to design your dream city from scratch, what would it have?' Be creative and imaginative, but concise"
    ) for role in roles
]

summary_agent = Agent(
    name="City Design Aggregator",
    instructions="You are city designer. You've just received 10 creative responses from different citizens. Read all of their responses and consolidate them into a cohesive, imaginative, and well-rounded city plan."
)

session = SQLiteSession("swarm")
conversation_history = []

with trace("Swarm system"):
    prompt = "Design your dream city from scratch. What would it have?"

    for agent in city_agents:
        result = Runner.run_sync(agent,prompt,session=session)
        print(f"{agent.name}: {result.final_output}\n")
        conversation_history.append(f"{agent.name}: {result.final_output}")
        combined_responses = "\n\n".join(conversation_history)
        final_results = Runner.run_sync(summary_agent,combined_responses,session=session)
        print("\nFinal City Design Summary:")
        print(final_results.final_output)