
# 🧳 AI Travel Designer Agent

This multi-agent system helps design a full travel experience based on user mood or interests. It demonstrates the use of **OpenAI Agent SDK**, **tooling**, and **agent handoffs** powered by **Gemini 1.5 Flash** via LiteLLM.

---

## 🌐 What It Does

- Takes a user input like "I want a peaceful nature vacation"
- Recommends travel destinations
- Simulates booking flights and hotels (mock data)
- Suggests top attractions and food

---

## 🧠 Agents Involved

| Agent Name          | Role                                                                 |
|---------------------|----------------------------------------------------------------------|
| `DestinationAgent`  | Suggests destinations based on user interest or mood                 |
| `BookingAgent`      | Uses tools to simulate flight and hotel bookings                     |
| `ExploreAgent`      | Suggests attractions and local food options for the destination      |
| `TravelPlannerAgent`| Triage agent that manages the flow and delegates tasks via handoffs  |

---

## 🛠 Tools

These tools are used by `BookingAgent` to simulate responses:

```python
@function_tool
def get_flights(destination: str) -> str:
    return f"Mock flight booked to {destination} via SkyAir at 10:00 AM."

@function_tool
def suggest_hotels(destination: str) -> str:
    return f"Recommended hotels in {destination}: DreamStay, ComfortNest, and Luxe Inn."
````

---

## ⚙️ Technologies Used

* **OpenAI Agent SDK**
* **LiteLLM** (using `google/gemini-1.5-flash`)
* **Asynchronous Execution** via `asyncio`
* **Agent-to-Agent Handoff**
* **Tool Integration** (function-based tools)

---

## 🚀 How to Run

1. **Install dependencies:**

```bash
pip install openai-agents[viz] litellm
```

2. **Replace `YOUR_GEMINI_API_KEY` with your actual key** in the code.

3. **Run the agent:**

```bash
python main.py
```

Expected Output:

```
Mock output including destination, flight & hotel booking, and attractions.
```

---

## 🖼 Optional: Visualize Agent Graph

If you want to view how agents are connected:

```python
from agents.extensions.visualization import draw_graph
draw_graph(travel_planner_agent).view()
```

---

## 🧩 File Structure

```
travel_designer_agent/
│
├── main.py             # Entry point with full agent logic
├── README.md           # This file
```

---

## 📌 Notes

* Gemini 1.5 Flash is integrated via `OpenAIChatCompletionsModel` from `LiteLLM`.
* Tracing is disabled with `set_tracing_disabled(disabled=True)` to avoid exporting traces.
* All responses are mock-based for demo purposes.

---

## ✨ Example Prompt

```text
"I want a peaceful nature vacation."
```

Agent will:

1. Recommend nature-based destinations
2. Simulate booking
3. Recommend nearby food and activities

---

## 🔐 Credits

* Built using [OpenAI Agent SDK](https://github.com/openai/openagents)
* Gemini model accessed via [LiteLLM](https://docs.litellm.ai/docs/providers)
