import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference configurations
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

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
    "platforms": ["LinkedIn", "Facebook", "Google Ads"],  # Adjust platforms as needed
}

# Convert the campaign inputs to a string message
campaign_message = (
    f"Business Name: {campaign_inputs['business_name']}\n"
    f"Website: {campaign_inputs['website']}\n"
    f"Industry: {campaign_inputs['industry']}\n"
    f"Unique Selling Proposition: {campaign_inputs['unique_selling_proposition']}\n"
    f"Campaign Objectives: {campaign_inputs['campaign_objectives']}\n"
    f"Target Audience: {campaign_inputs['target_audience']}\n"
    f"Budget: {campaign_inputs['budget']}\n"
    f"Campaign Duration: {campaign_inputs['campaign_duration']}\n"
    f"Platforms: {', '.join(campaign_inputs['platforms'])}"
)

# Define Agents
business_layer_agent = AssistantAgent(
    name="BusinessStrategist",
    llm_config={"config_list": config_list},
)

ads_layer_agent = AssistantAgent(
    name="AdCreator",
    llm_config={"config_list": config_list},
)

campaign_layer_agent = AssistantAgent(
    name="CampaignManager",
    llm_config={"config_list": config_list},
)

decision_layer_agent = AssistantAgent(
    name="PerformanceAnalyst",
    llm_config={"config_list": config_list},
)

intel_layer_agent = AssistantAgent(
    name="CompetitorAnalyst",
    llm_config={"config_list": config_list},
)

manager_agent = AssistantAgent(
    name="CampaignManager",
    llm_config={"config_list": config_list},
)

# User Proxy Agent for direct user interaction
user_proxy = UserProxyAgent(
    name="User",
    code_execution_config={"work_dir": "coding", "use_docker": False}
)

# Function to handle campaign workflow execution
def execute_campaign_workflow():
    current_results = {}

    try:
        # Start the campaign process by sending campaign details to the manager agent
        user_proxy.initiate_chat(manager_agent, message=f"Start the campaign planning with the following details:\n{campaign_message}")

        # Step 1: Strategy Creation
        manager_agent.initiate_chat(business_layer_agent, message="Develop a campaign strategy based on the provided inputs.")
        strategy_response = business_layer_agent.receive(message="Please create a campaign strategy based on the inputs provided.", sender=manager_agent)
        print("Strategy Created:", strategy_response)
        current_results['strategy_result'] = strategy_response

        # Step 2: Create Ads
        business_layer_agent.initiate_chat(ads_layer_agent, message=f"Create ads based on this strategy: {strategy_response}")
        ads_response = ads_layer_agent.receive(message="Please create ads based on the strategy.", sender=business_layer_agent)
        print("Ads Created:", ads_response)
        current_results['ads_result'] = ads_response

        # Step 3: Deploy Campaign
        ads_layer_agent.initiate_chat(campaign_layer_agent, message=f"Deploy the following ads: {ads_response}")
        deployment_response = campaign_layer_agent.receive(message="Please deploy the ads.", sender=ads_layer_agent)
        print("Campaign Deployed:", deployment_response)
        current_results['deployment_result'] = deployment_response

        # Step 4: Analyze Performance
        campaign_layer_agent.initiate_chat(decision_layer_agent, message=f"Analyze the performance of the deployed campaign: {deployment_response}")
        analysis_response = decision_layer_agent.receive(message="Please analyze the campaign's performance.", sender=campaign_layer_agent)
        print("Performance Analysis Completed:", analysis_response)
        current_results['performance_result'] = analysis_response

        # Step 5: Competitor Analysis
        decision_layer_agent.initiate_chat(intel_layer_agent, message="Conduct a competitor analysis to enhance our campaign further.")
        competitor_analysis = intel_layer_agent.receive(message="Please conduct a competitor analysis.", sender=decision_layer_agent)
        print("Competitor Analysis Completed:", competitor_analysis)
        current_results['competitor_analysis'] = competitor_analysis

        # Summarizing the Campaign
        intel_layer_agent.initiate_chat(manager_agent, message="Provide a summary of the entire campaign process.")
        campaign_summary = manager_agent.receive(message="Please provide a campaign summary.", sender=intel_layer_agent)
        print("Campaign Summary:", campaign_summary)
        current_results['campaign_summary'] = campaign_summary

    except Exception as e:
        print("An error occurred during campaign execution:", e)

    return current_results

if __name__ == "__main__":
    final_results = execute_campaign_workflow()
    print("\nFinal Campaign Execution Summary:", final_results)
