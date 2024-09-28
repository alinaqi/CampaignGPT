import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from campaigngpt.crew import CampaigngptCrew

def main():
    # Define the input data required for your campaign
    inputs = {
        "business_name": "WorkHub Platform Inc.",
        "website": "https://www.workhub.ai",
        "industry": "Technology",
        "unique_selling_proposition": "Enterprise AI platform with knowledge management, chatbots, and voice agents.",
        "campaign_objectives": "Increase leads and signups",
        "target_audience": "Business leaders looking to leverage AI to increase efficiencies",
        "budget": 2000,
        "campaign_duration": "1 week",
        "platforms": ["LinkedIn", "Facebook", "Google Ads"],  # Add or adjust platforms as needed
    }

    # Initialize the CampaigngptCrew with the input data
    campaign_crew = CampaigngptCrew(inputs)

    # Initial execution of the campaign
    try:
        result = campaign_crew.crew().kickoff(inputs=inputs)
        print("Initial Campaign Execution Completed!")
        print(result)
        
    except Exception as e:
        print("An error occurred during the initial campaign execution:")
        print(e)
        return


def interact_with_manager(campaign_crew):
    print("\nYou can now interact with the Campaign Manager Agent.")

    while True:
        user_input = input("Ask a question or provide instructions for the next campaign phase (type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Ending interaction with the Campaign Manager.")
            break
        
        try:
            # Access the manager agent directly
            manager_agent = campaign_crew.manager_agent()
            
            # Execute the task with the user's input
            print("\nSending your question to the Campaign Manager Agent...")
            response = manager_agent.execute_task({"user_question": user_input})
            
            # Display the response from the manager
            if response and isinstance(response, dict):
                print("\nCampaign Manager Response:", response.get("answer", "No response"))
                
                # Check for next steps provided by the manager
                if response.get("next_campaign_phase"):
                    print("\nExecuting the next campaign phase as instructed by the Campaign Manager...")
                    campaign_crew.run_next_campaign_phase()
                    
        except Exception as e:
            print("An error occurred while interacting with the Campaign Manager Agent:")
            print(e)

if __name__ == "__main__":
    main()
