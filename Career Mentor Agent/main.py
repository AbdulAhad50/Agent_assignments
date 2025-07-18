from agents import Agent, Runner, function_tool, tracing, AsyncOpenAI, OpenAIChatCompletionsModel
import asyncio
from agents import (
    Agent,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

from agents.run import RunConfig

external_client = AsyncOpenAI(
    api_key='YOUR_GEMINI_API_KEY',
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

set_default_openai_client(client=external_client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)

@function_tool
def get_career_roadmap(career: str) -> str:
    return f"To succeed in {career}, you should learn: Communication, Problem Solving, and Specialized Knowledge."

career_agent = Agent(
    name="CareerAgent",
    instructions="Ask the user about their interests and suggest suitable career paths.",
    model=model
)

skill_agent = Agent(
    name="SkillAgent",
    instructions="Given a career path, explain the skill roadmap using the tool.",
    tools=[get_career_roadmap],
    model=model
)

job_agent = Agent(
    name="JobAgent",
    instructions="Given a career field, share 2-3 real-world job roles and a brief description.",
    model=model
)

mentor_agent = Agent(
    name="CareerMentorAgent",
    instructions=(
        "You are a career mentor. Ask the user their interests. "
        "First recommend a field (handoff to CareerAgent), "
        "then explain skill roadmap (handoff to SkillAgent), "
        "then real job examples (handoff to JobAgent)."
    ),
    handoffs=[career_agent, skill_agent, job_agent],
    model=model,
)

if __name__ == "__main__":
    async def run_agent():
        result = await Runner.run(mentor_agent, "I'm interested in tech.")
        print(result.final_output)

    asyncio.run(run_agent())
