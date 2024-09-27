import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from campaigngpt.crew import CampaigngptCrew

def main():
    # Define the input data required for your campaign
    inputs = {
        "business_goal": "Increase brand awareness for our new product line",
        "target_audience": "Tech-savvy professionals aged 25-40",
        "budget": 10000,
        "campaign_duration": "1 month",
        "platforms": ["Facebook", "LinkedIn", "Instagram"],
        # Add more fields as required for your campaign tasks
    }

    # Initialize the CampaigngptCrew with the input data
    campaign_crew = CampaigngptCrew(inputs)

    # Kickoff the Crew with the provided inputs
    try:
        result = campaign_crew.crew().kickoff(inputs=inputs)

        # Print the results
        print("Campaign Execution Completed!")
        print(result)
        
    except Exception as e:
        print("An error occurred during campaign execution:")
        print(e)

if __name__ == "__main__":
    main()
