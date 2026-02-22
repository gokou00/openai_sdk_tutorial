from agents import Agent, Runner, SQLiteSession, trace , handoff, function_tool
from agents.extensions.visualization import draw_graph
from dotenv import load_dotenv

load_dotenv()


@function_tool
def calculate_physics_equation(equation):
    pass

@function_tool
def perform_culture_survey(goal):
    pass

@function_tool
def perform_history_survey(goal):
    pass

physics_agent = Agent(
    name="Physics Agent",
    instructions="Answer questions about physics.",
    tools=[calculate_physics_equation]
)

chemistry_agent = Agent(
    name="Chemistry Agent",
    instructions="Answer questions about chemistry."
)

medical_agent = Agent(
    name="Medical Agent",
    instructions="Answer questions about medical science."
)

politics_agent = Agent(
    name="Politics Agent",
    instructions="Answer questions about political science."
)

warfare_agent = Agent(
    name="Warfare Agent",
    instructions="Answer questions about wars and military history."
)

culture_agent = Agent(
    name="Culture Agent",
    instructions="Answer questions about cultural history.",
    tools=[perform_culture_survey]
)


science_manager = Agent(
    name="Science Manager",
    instructions="Manage science-related questions and route them to the appropriate subdomain agent.",
    handoffs=[physics_agent, chemistry_agent, medical_agent]
)

history_manager = Agent(
    name="History Manager",
    instructions="Manage history-related questions and route them to the appropriate subdomain agent.",
    handoffs=[politics_agent, warfare_agent, culture_agent]
)


triage_agent = Agent(
    name="Research Triage Agent",
    instructions="Triage the user's question and decide whether it's a science or history related, and route accordingly",
    handoffs=[science_manager, history_manager]
)

draw_graph(triage_agent, filename="graph_visualization")

session = SQLiteSession("hierarchy")
last_agent = triage_agent

with trace("Hierarchical System"):
    while True:
        question = input("You:  ")
        result = Runner.run_sync(last_agent, question, session=session)
        print(f"Agent: {result.final_output}")
        last_agent = result.last_agent



