import asyncio
from agents import Agent, Runner, function_tool
from agents import (
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
)

# Gemini setup
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

# Tools
@function_tool
def roll_dice(sides: int = 6) -> int:
    import random
    return random.randint(1, sides)

@function_tool
def generate_event(location: str) -> str:
    return f"While exploring the {location}, you encounter a mysterious cave with glowing runes."

# Agents
narrator_agent = Agent(
    name="NarratorAgent",
    instructions="You narrate the story based on player input. Hand off to other agents as needed.",
    model=model
)

monster_agent = Agent(
    name="MonsterAgent",
    instructions="Control the combat phase. Use dice rolls to determine outcomes.",
    tools=[roll_dice],
    model=model
)

item_agent = Agent(
    name="ItemAgent",
    instructions="Manage player's inventory and rewards. Use tools to generate magical events.",
    tools=[generate_event],
    model=model
)

# Main Game Master Agent
game_master_agent = Agent(
    name="GameMasterAgent",
    instructions=(
        "You are the Game Master of a fantasy adventure game. Narrate the journey. "
        "When there's combat, handoff to MonsterAgent. For loot/rewards, handoff to ItemAgent. "
        "Continue the story with dynamic choices."
    ),
    handoffs=[narrator_agent, monster_agent, item_agent],
    model=model
)

# Run game
if __name__ == "__main__":
    async def run_game():
        result = await Runner.run(game_master_agent, "I enter the dark forest, sword in hand.")
        print(result.final_output)

    asyncio.run(run_game())
