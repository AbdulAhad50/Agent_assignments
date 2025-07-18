
# Career Mentor Agent
````markdown

The **Career Mentor Agent** is a multi-agent system built using the [OpenAI Agents SDK](https://github.com/openai/openai-python/tree/main/packages/agents) with support for **Google Gemini 1.5 Flash** model via LiteLLM-compatible interface. This agent guides users through career exploration by suggesting fields, skill roadmaps, and real-world job roles.

---

## 🚀 Features

- 🧠 **CareerAgent**: Suggests career fields based on user interests.
- 🛠️ **SkillAgent**: Uses a tool to return a roadmap of skills for a given field.
- 🧳 **JobAgent**: Provides 2–3 real-world job roles in that career field.
- 🔁 **MentorAgent**: Orchestrates the conversation and performs handoffs between the agents.
- 🔒 **Tracing disabled**: No telemetry or data is sent externally.

---

## 🧱 Tech Stack

- **OpenAI Agents SDK**
- **Google Gemini 1.5 Flash** via `OpenAIChatCompletionsModel` (LiteLLM-compatible)
- **Python 3.10+**
- **Async support using `asyncio`**

---

## 🛠️ Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yourname/career-mentor-agent
cd career-mentor-agent
````

### 2. Install dependencies

```bash
pip install openai-agents
```

### 3. Run the agent

Make sure your file is named `main.py` or similar:

```bash
python main.py
```

---

## 🔐 Gemini API Key Setup

The agent uses the **Google Gemini API** with an OpenAI-compatible wrapper.

Replace this line in the code with your **actual Gemini API key**:

```python
api_key='YOUR_GEMINI_API_KEY'
```

You must also ensure the `base_url` is set correctly for Gemini:

```python
base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
```

---

## 💡 Example Output

When run, the system might return:

```
Based on your interest in tech, here are some suggested careers: Software Engineering, UX Design...
To succeed in Software Engineering, learn: Communication, Problem Solving, and Specialized Knowledge.
Here are a few jobs: Frontend Developer, Backend Engineer, QA Analyst...
```

---

## 📂 File Structure

```
main.py               # Entry point for running the agent
README.md             # Documentation
```

---

## ✅ Notes

* No tracing or telemetry is enabled (`set_tracing_disabled(True)`).
* Gemini API must support OpenAI-style chat completions.
* Designed for educational and exploration purposes.

---

## 📬 Contact

For any questions, feel free to reach out at \[[your-email@example.com](mailto:your-email@example.com)].

```

---
