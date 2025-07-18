import asyncio

from agents import Agent, Runner, function_tool, tracing, AsyncOpenAI, OpenAIChatCompletionsModel
from agents import (
    Agent,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

from agents.run import RunConfig

external_client = AsyncOpenAI(
    api_key='AIzaSyDaD0rRW_lgE_ChKkuWC0jt7opsgcvj6ig',
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
def get_flights(destination: str) -> str:
    return f"Mock flight booked to {destination} via SkyAir at 10:00 AM."

@function_tool
def suggest_hotels(destination: str) -> str:
    return f"Recommended hotels in {destination}: DreamStay, ComfortNest, and Luxe Inn."



destination_agent = Agent(
    name="DestinationAgent",
    instructions="Ask the user about their mood or interest and suggest travel destinations.",
    model=model
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="Simulate flight and hotel booking using tools.",
    tools=[get_flights, suggest_hotels],
    model=model
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="Given a destination, suggest top attractions and food.",
    model=model
)

travel_planner_agent = Agent(
    name="TravelPlannerAgent",
    instructions=(
        "You are a travel designer. Ask the user about their mood or interest. "
        "First handoff to DestinationAgent to suggest places. "
        "Then handoff to BookingAgent for mock bookings. "
        "Finally, handoff to ExploreAgent to share places and food."
    ),
    handoffs=[destination_agent, booking_agent, explore_agent],
    model=model,
)




if __name__ == "__main__":
    async def run_agent():
        result = await Runner.run(travel_planner_agent, "I want a peaceful nature vacation.")
        print(result.final_output)

    asyncio.run(run_agent())
