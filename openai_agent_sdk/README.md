# OpenAI Agent SDK

A chapter-based tutorial and example collection for the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python). This project walks through building multi-agent applications with OpenAI models—from basic agents and tools through tracing, orchestration, and production-style workflows.

## Project Structure

```
openai_agent_sdk/
├── Chapter3/               # Getting started: environment & basic agents
├── Chapter4/               # Tools: function tools, built-ins, chaining
├── Chapter5/               # Memory & sessions
├── Chapter6/               # Multi-agent orchestration & handoffs
├── Chapter7/               # Model configuration & context
├── Chapter8/               # Tracing & guardrails
└── Chapter9/               # End-to-end applications
    ├── Chatbot/            # Customer service chatbot with guardrails
    └── WorkFlowAutomation/ # Automated customer research & email workflow
```

## Prerequisites

- Python 3.9+
- [OpenAI API key](https://platform.openai.com/api-keys)

## Setup

1. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install openai-agents[litellm,viz] python-dotenv pydantic requests
   ```

   The `litellm` extra enables model routing; the `viz` extra enables agent graph visualization.

3. **Configure your API key**

   Create a `.env` file in the project root:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Verify setup**

   ```bash
   python Chapter3/verify_environment_setuo.py
   ```

   You should see "API Key loaded successfully" and "Setup successful".

## Chapter Overview

| Chapter | Focus |
|---------|-------|
| **3** | Setup, basic agents, function tools, handoffs |
| **4** | Tools (function tools, built-ins, MCP, agents-as-tools) |
| **5** | Sessions, memory, conversation history |
| **6** | Multi-agent design (hierarchical, swarm, handoffs) |
| **7** | Model selection and local context |
| **8** | Tracing, spans, and guardrails |
| **9** | Full applications (chatbot, workflow automation) |

## Chapter 9 Applications

The Chapter 9 apps require database setup before running.

### Chatbot (Customer Service)

Creates a SQLite order database and runs an interactive customer service chatbot with input guardrails and handoff to a retention agent.

```bash
cd Chapter9/Chatbot
python setup.py   # Creates paper_data.db
python agent.py   # Run the chatbot
```

### WorkFlow Automation

Creates a customer database and runs a batch workflow: research customers, generate personalized emails, and write outputs to JSON files.

```bash
cd Chapter9/WorkFlowAutomation
python setup.py   # Creates customer_details.db
python agent.py   # Run the workflow
```

## Key Examples by Chapter

### Chapter 4 – Tools
- `crypto_pricing_agent.py` — Custom function tools with Pydantic models
- `database_query.py` — Simulated DB query tool
- `tool_chaining.py` — Multiple tools in sequence
- `web_search_tool.py` — WebSearchTool usage
- `code_interpreter_tool.py` — Code execution for calculations
- `image_generation_tool.py` — Image generation
- `mortage_agent.py` — ModelSettings, tool_choice, tool_use_behavior
- `mcp_tool.py` — HostedMCPTool (e.g., CoinGecko MCP server)
- `agents_as_tools.py` — Agents used as tools via `agent.as_tool()`

### Chapter 5 – Memory
- `conversations_with_sessions.py` — SQLiteSession for conversation history
- `ltm_sessions.py` — Sessions with custom DB path
- `memory_tracking_messages_simple.py` — Manual message history
- `ltm_structured_memory_call.py` — JSON-based memory save/load tools
- `us_constitution_agent.py` — Vector search with FileSearchTool + session

### Chapter 6 – Multi-Agent
- `basic_handoff.py` — Triage agent with handoffs
- `deterministic_approach.py` — Explicit routing by keywords
- `dynamic_approach.py` — Agents as tools for dynamic routing
- `hierarchical.py` — Triage → managers → domain agents
- `decentralized.py` — Turn-taking debate
- `swarm.py` — Parallel agents + aggregator
- `multi_agent_switching.py` — Bidirectional handoffs with shared session
- `hand-off_customization.py` — Custom handoff configuration
- `visualization.py` — `draw_graph()` for agent diagrams

### Chapter 8 – Tracing & Guardrails
- `basic_trace.py` — `trace()` for workflow tracking
- `custom_trace.py` — Named traces
- `custom_span.py` — `custom_span()` for custom segments
- `input_guardrail.py` — `@input_guardrail` for request validation
- `visualization.py` — Trace visualization

## Resources

- [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents GitHub](https://github.com/openai/openai-agents-python)

## License

See the upstream [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) for license information.
