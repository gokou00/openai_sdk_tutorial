from agents import Agent, Runner, SQLiteSession, trace , handoff
from dotenv import load_dotenv

load_dotenv()



landlord_agent = Agent(
    name="Landlord Agent",
    instructions="Argue against rent control from the perspective of a landlord. Present strong economic and property-rights arguments."
)

tenant_agent = Agent(
    name="Tenant Agent",
    instructions="Argue in favor of rent control from the perspective of a tenant. Emphasize affordability, housing rights, and tenant protections."
)

summarizer_agent = Agent(
    name="Summarizer Agent",
    instructions="Summarize the main arguments of the landlord and tenant agents in a neutral, fair, and balanced way."
)

session = SQLiteSession("decentralized")

landlord_turn = True

conversation_history = []

with trace("decenralized"):
    print("Topic: Should there be rent control?")
    for _ in range(6):
        if landlord_turn:
            agent = landlord_agent
        else:
            agent = tenant_agent
        prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history])
        response = Runner.run_sync(agent, prompt or "Debate starting now.", session=session)
        conversation_history.append({"role": "user", "content": response.final_output})
        landlord_turn = not landlord_turn

        summary_prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history])
        summary_response = Runner.run_sync(summarizer_agent, summary_prompt, session=session)
        print("\nSummary of the debate: ")
        print(f"Summary: {summary_response.final_output}")

