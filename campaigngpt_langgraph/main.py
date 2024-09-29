import os
import openai
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict


# Load OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define campaign inputs
campaign_inputs = {
    "business_name": "WorkHub Platform Inc.",
    "website": "https://www.workhub.ai",
    "industry": "Technology",
    "unique_selling_proposition": "Enterprise AI platform with knowledge management, chatbots, and voice agents.",
    "campaign_objectives": "Increase leads and signups",
    "target_audience": "Business leaders looking to leverage AI to increase efficiencies",
    "budget": 2000,
    "campaign_duration": "1 week",
    "platforms": ["LinkedIn", "Facebook", "Google Ads"],
}

class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize the graph builder with the state definition
print("Initializing the graph builder...")
graph_builder = StateGraph(State)



def call_openai(messages):
    # Ensure the messages are correctly formatted as a list of dictionaries
    print("Calling OpenAI API...")
    print("Messages:", messages)
    formatted_messages = []
    for item in messages:
        if isinstance(item, tuple) and len(item) == 2:
            role, content = item
            formatted_messages.append({"role": role, "content": content})
        elif isinstance(item, dict) and "role" in item and "content" in item:
            formatted_messages.append(item)
        else:
            print(f"Invalid message format detected: {item}")
            continue
    
    # Make the OpenAI API call
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Set the appropriate model here
        messages=formatted_messages
    )
    return response.choices[0].message.content


def business_strategy_node(state: State):
    prompt = "Develop a campaign strategy based on the provided inputs."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    return {"messages": [("assistant", response)]}

def ad_creation_node(state: State):
    prompt = "Create ads based on the campaign strategy."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    return {"messages": [("assistant", response)]}

def campaign_deployment_node(state: State):
    prompt = "Deploy the ads based on the provided campaign strategy."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    return {"messages": [("assistant", response)]}

def performance_analysis_node(state: State):
    prompt = "Analyze the performance of the deployed campaign."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    return {"messages": [("assistant", response)]}

def competitor_analysis_node(state: State):
    prompt = "Conduct a competitor analysis to enhance our campaign further."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    return {"messages": [("assistant", response)]}

def campaign_summary_node(state: State):
    prompt = "Provide a summary of the entire campaign process."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    return {"messages": [("assistant", response)]}

print("adding nodes...")
graph_builder.add_node("business_strategy", business_strategy_node)
graph_builder.add_node("ad_creation", ad_creation_node)
graph_builder.add_node("campaign_deployment", campaign_deployment_node)
graph_builder.add_node("performance_analysis", performance_analysis_node)
graph_builder.add_node("competitor_analysis", competitor_analysis_node)
graph_builder.add_node("campaign_summary", campaign_summary_node)

print("adding edges...")
graph_builder.add_edge(START, "business_strategy")
graph_builder.add_edge("business_strategy", "ad_creation")
graph_builder.add_edge("ad_creation", "campaign_deployment")
graph_builder.add_edge("campaign_deployment", "performance_analysis")
graph_builder.add_edge("performance_analysis", "competitor_analysis")
graph_builder.add_edge("competitor_analysis", "campaign_summary")
graph_builder.add_edge("campaign_summary", END)

print("Compiling the graph...")
graph = graph_builder.compile()


def run_campaign_workflow(user_input: str):
    print("Running the campaign workflow...")
    state = {"messages": [("user", user_input)]}
    
    # Stream graph updates and handle each step's result
    for event in graph.stream(state):
        for value in event.values():
            print("Campaign Output:", value["messages"][-1][1])  # Display the message content

# Example usage
if __name__ == "__main__":
    user_input = "Start the campaign planning process."
    run_campaign_workflow(user_input)


