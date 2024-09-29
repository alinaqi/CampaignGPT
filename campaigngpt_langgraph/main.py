import os
import openai
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.checkpoint.memory import MemorySaver



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

# Define the shared state structure
class State(TypedDict):
    messages: Annotated[list, add_messages]
    strategy: str
    ads: str
    performance_metrics: dict
    competitor_analysis: dict
    next_steps: str
    campaign_inputs: dict  # Add this line


# Initialize the graph builder with the state definition
print("Initializing the graph builder...")
graph_builder = StateGraph(State)



def call_openai(messages):
    # Ensure the messages are correctly formatted as a list of dictionaries
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
    # Incorporate campaign inputs into the prompt
    prompt = f"Develop a campaign strategy based on the following inputs: {state['campaign_inputs']}"
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)  # Using OpenAI to simulate agent response
    state["strategy"] = response
    return {"messages": [("assistant", response)], "strategy": response}



def ad_creation_node(state: State):
    prompt = f"Create ads based on the strategy: {state['strategy']}"
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    state["ads"] = response
    return {"messages": [("assistant", response)], "ads": response}


def campaign_deployment_node(state: State):
    prompt = "Deploy the ads based on the provided campaign strategy."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    return {"messages": [("assistant", response)]}

def performance_analysis_node(state: State):
    prompt = f"Analyze the performance of the deployed ads: {state['ads']}"
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    state["performance_metrics"] = {"insights": response}
    return {"messages": [("assistant", response)], "performance_metrics": state["performance_metrics"]}

def optimization_node(state: State):
    prompt = f"Based on the performance metrics {state['performance_metrics']} and competitor analysis {state['competitor_analysis']}, optimize the campaign."
    messages = state["messages"] + [("assistant", prompt)]
    response = call_openai(messages)
    state["next_steps"] = response
    return {"messages": [("assistant", response)], "next_steps": response}


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

def human_review_node(state: State):
    print("\nEntering human review phase...")
    review_input = input("Please provide your feedback for the current campaign state or press Enter to approve: ")

    if review_input.strip():
        state["messages"].append(("user", review_input))
        print(f"Human feedback: {review_input}")
    else:
        print("No feedback provided. Proceeding with the current plan.")

    return {"messages": state["messages"]}

print("adding nodes...")
# Add nodes to the graph
graph_builder.add_node("human_review", human_review_node)
graph_builder.add_node("business_strategy", business_strategy_node)
graph_builder.add_node("ad_creation", ad_creation_node)
graph_builder.add_node("performance_analysis", performance_analysis_node)
graph_builder.add_node("optimization", optimization_node)


print("adding edges...")
graph_builder.add_edge(START, "business_strategy")
graph_builder.add_edge("business_strategy", "ad_creation")
graph_builder.add_edge("ad_creation", "performance_analysis")
graph_builder.add_edge("performance_analysis", "optimization")
graph_builder.add_edge("optimization", "human_review")
graph_builder.add_edge("human_review", END)

print("Compiling the graph with human interrupt...")
memory = MemorySaver()

graph = graph_builder.compile(checkpointer=memory,interrupt_before=["optimization"], interrupt_after=["performance_analysis"])


def run_campaign_workflow(user_input: str):
    print("Running the collaborative campaign workflow...")
    # Initialize the state with campaign inputs and other required fields
    state = {
        "messages": [("user", user_input)], 
        "strategy": "", 
        "ads": "", 
        "performance_metrics": {}, 
        "competitor_analysis": {}, 
        "next_steps": "",
        "campaign_inputs": campaign_inputs  # Include the campaign inputs
    }
    
    # Define the config for this session
    config = {"configurable": {"thread_id": "campaign_workflow_session"}}
    
    # Stream graph updates and handle each step's result
    for event in graph.stream(state, config):
        for value in event.values():
            print("Campaign Output:", value["messages"][-1][1])  # Display the message content
            
            # Check if the graph is waiting for human input
            current_state = graph.get_state(config)  # Use the config when calling get_state()
            
            if current_state.next and current_state.next[0] in ["optimization", "END"]:
                # Prompt for human input
                human_input = input("The system is awaiting your input before proceeding. Please provide your feedback or press Enter to continue: ")
                
                if human_input.strip():
                    state["messages"].append(("user", human_input))
                    print(f"Human input received: {human_input}")
                    graph.update_state(config, {"messages": state["messages"]})  # Update the state with the config
                else:
                    print("No additional input provided. Proceeding to the next step.")



# Example usage
if __name__ == "__main__":
    user_input = "Start the campaign planning process."
    run_campaign_workflow(user_input)


