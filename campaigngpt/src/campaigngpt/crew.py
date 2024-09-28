from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.llm import LLM 

@CrewBase
class CampaigngptCrew():
    """Campaigngpt crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, inputs=None):
        # Initialize parent class
        super().__init__()
        self.inputs = inputs  # Store the inputs for later use
        self.current_results = {}  # Store results shared between agents/tasks
    
    def communicate_and_adapt(self):
        # Communicate results between agents and make decisions
        performance_result = self.current_results.get("performance_result", {})
        
        # Decide which A/B test variant worked better
        best_variant = "A" if performance_result.get("variant_A_CTR", 0) > performance_result.get("variant_B_CTR", 0) else "B"
        print(f"Decision Layer Agent: Variant {best_variant} performed better. Updating campaign strategy accordingly.")
        
        # Update the strategy based on the winning variant
        self.current_results["winning_variant"] = best_variant
        self.current_results["next_steps"] = ["Increase budget on LinkedIn", "Refine messaging for better engagement"] if best_variant == "A" else ["Focus on Instagram", "Optimize for mobile engagement"]
        
    def run_next_campaign_phase(self):
        next_steps = self.current_results.get("next_steps", [])
		
        if next_steps:
            print(f"Executing the next steps: {next_steps}")
            
            # Here, execute the necessary tasks based on the instructions
            # Example: re-running the strategy task based on the new instructions
            if "create_strategy_task" in next_steps:
                self.create_strategy_task().execute()
            elif "create_ads_task" in next_steps:
                self.create_ads_task().execute()
            elif "deploy_campaign_task" in next_steps:
                self.deploy_campaign_task().execute()
            elif "analyze_performance_task" in next_steps:
                self.analyze_performance_task().execute()
            elif "conduct_competitor_analysis_task" in next_steps:
                self.conduct_competitor_analysis_task().execute()
            elif "summarize_campaign_task" in next_steps:
                self.summarize_campaign_task().execute()


    @agent
    def business_layer_agent(self) -> Agent:
        # Extract the agent configuration
        config = self.agents_config['business_layer_agent']
        print("Agent config: ", config)
        
        # Extract the individual values from the config
        role = config.get('role', 'Default Role')
        goal = config.get('goal', 'Default Goal')
        backstory = config.get('backstory', 'Default Backstory')
        # Assign the LLM model explicitly
        # Create the LLM instance using your desired model configuration
        llm_instance = LLM(
            model="gpt-4o-mini",    # Replace with your desired model name
            temperature=0.7,        # Set this value as per your requirement
            base_url="https://api.openai.com/v1",  # The base URL of the OpenAI API
        )
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=llm_instance,
            verbose=True
        )

    @agent
    def ads_layer_agent(self) -> Agent:
        config=self.agents_config['ads_layer_agent']
        print("Agent config: ", config)
        
        # Extract the individual values from the config
        role = config.get('role', 'Default Role')
        goal = config.get('goal', 'Default Goal')
        backstory = config.get('backstory', 'Default Backstory')
        # Assign the LLM model explicitly
        # Create the LLM instance using your desired model configuration
        llm_instance = LLM(
            model="gpt-4o-mini",    # Replace with your desired model name
            temperature=0.7,        # Set this value as per your requirement
            base_url="https://api.openai.com/v1",  # The base URL of the OpenAI API
        )
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=llm_instance,
            verbose=True
        )

    @agent
    def campaign_layer_agent(self) -> Agent:
        config=self.agents_config['campaign_layer_agent']
        print("Agent config: ", config)
        
        # Extract the individual values from the config
        role = config.get('role', 'Default Role')
        goal = config.get('goal', 'Default Goal')
        backstory = config.get('backstory', 'Default Backstory')
        # Assign the LLM model explicitly
        # Create the LLM instance using your desired model configuration
        llm_instance = LLM(
            model="gpt-4o-mini",    # Replace with your desired model name
            temperature=0.7,        # Set this value as per your requirement
            base_url="https://api.openai.com/v1",  # The base URL of the OpenAI API
        )
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=llm_instance,
            verbose=True
        )

    @agent
    def decision_layer_agent(self) -> Agent:
        config=self.agents_config['decision_layer_agent']
        print("Agent config: ", config)
        
        # Extract the individual values from the config
        role = config.get('role', 'Default Role')
        goal = config.get('goal', 'Default Goal')
        backstory = config.get('backstory', 'Default Backstory')
        # Assign the LLM model explicitly
        # Create the LLM instance using your desired model configuration
        llm_instance = LLM(
            model="gpt-4o-mini",    # Replace with your desired model name
            temperature=0.7,        # Set this value as per your requirement
            base_url="https://api.openai.com/v1",  # The base URL of the OpenAI API
        )
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=llm_instance,
            verbose=True
        )
    
    @agent
    def intel_layer_agent(self) -> Agent:
        config = self.agents_config['intel_layer_agent']
        print("Agent config: ", config)
        
        # Extract the individual values from the config
        role = config.get('role', 'Default Role')
        goal = config.get('goal', 'Default Goal')
        backstory = config.get('backstory', 'Default Backstory')
        # Assign the LLM model explicitly
        # Create the LLM instance using your desired model configuration
        llm_instance = LLM(
            model="gpt-4o-mini",    # Replace with your desired model name
            temperature=0.7,        # Set this value as per your requirement
            base_url="https://api.openai.com/v1",  # The base URL of the OpenAI API
        )
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=llm_instance,
            verbose=True
        )


    @agent
    def manager_agent(self) -> Agent:
        config = self.agents_config['manager_agent']
        print("Agent config: ", config)

        # Create the LLM instance
        llm_instance = LLM(
            model="gpt-4o-mini",
            temperature=0.7,
            base_url="https://api.openai.com/v1",
        )

        def execute_task(user_input=None):
            if not user_input:
                user_input = {}  # Ensure user_input is a dictionary

            # Process the user question or instruction
            user_question = user_input.get("user_question", "")
            if not user_question:
                print("No specific question provided. Prompting for further instructions...")
                user_question = input("Please provide your instructions or ask a question: ")
            
            print(f"Manager Agent processing user question: {user_question}")

            # Simulate manager response to user's question
            if "continue" in user_question.lower():
                response = {
                    "answer": "Yes, we should continue running the campaigns as they are showing good performance.",
                    "next_campaign_phase": None  # No new instructions in this case
                }
            elif "optimize" in user_question.lower():
                response = {
                    "answer": "We should optimize the campaign by increasing budget on LinkedIn.",
                    "next_campaign_phase": {
                        "campaign_objectives": "Optimize ad spend",
                        "budget": 3000,  # Adjust budget as needed
                        "platforms": ["LinkedIn", "Instagram"],  # Example update to platforms
                    }
                }
            else:
                response = {
                    "answer": f"The campaign currently focuses on {self.current_results.get('best_variant', 'variant B')} performing better.",
                    "next_campaign_phase": {
                        "campaign_objectives": "Optimize ad spend based on previous results",
                        "budget": 3000,  # Example change in budget for the next phase
                        "platforms": ["LinkedIn", "Instagram"],  # Example change in platforms
                    } if "optimize" in user_question.lower() else None
                }

            print("Manager Agent response:", response)
            return response

        return Agent(
            role=config.get('role', 'Campaign Manager'),
            goal=config.get('goal', 'Manage campaign tasks'),
            backstory=config.get('backstory', 'Experienced marketing professional'),
            llm=llm_instance,
            verbose=True,
            execute_task=execute_task,  # Define the execute_task logic for manager's tasks
            human_input=True  # Ensure human_input is enabled to prompt the user
        )

    @task
    def create_strategy_task(self) -> Task:
        config = self.tasks_config['create_strategy_task']
        
        # Extract the description and expected output
        description = config.get('description')
        expected_output = config.get('expected_output')
        
        def execute_task():
            # Access competitor analysis results
            competitor_analysis = self.current_results.get("competitor_analysis", {})
            print("Using competitor analysis in strategy creation:", competitor_analysis)
            
            # Adjust strategy based on competitor insights
            strategy = {
                "target_audience": self.inputs["target_audience"],
                "key_messaging": f"Leverage our integration capabilities and AI-driven solutions",
                "platforms": self.inputs["platforms"],
                "budget_allocation": {"Facebook": 6000, "LinkedIn": 4000},
                "differentiators": ["Superior customer support", "Seamless integration with enterprise tools"]
            }
            
            return strategy

        return Task(
            description=description,
            expected_output=expected_output,  # Make sure expected_output is included
            agent=self.business_layer_agent(),
            human_input=True,
            execute=execute_task
        )



    @task
    def create_ads_task(self) -> Task:
        config = self.tasks_config['create_ads_task']
        
        # Extract the description and expected output
        description = config.get('description')
        expected_output = config.get('expected_output')  # Ensure you extract the expected_output

        def execute_task():
            strategy_result = self.current_results.get("strategy_result", {})
            print(f"Executing ad creation task based on strategy: {strategy_result}")
            
            # Simulate ad creation based on the A/B test strategy
            simulated_ads = {
                "ads": {
                    "A": f"Ad with messaging '{strategy_result['ad_creatives'][0]}'",
                    "B": f"Ad with messaging '{strategy_result['ad_creatives'][1]}'"
                },
                "platforms": strategy_result.get("platforms", [])
            }
            self.current_results["ads_result"] = simulated_ads
            return simulated_ads
        
        return Task(
            description=description,
            expected_output=expected_output,  # Include expected_output here
            agent=self.ads_layer_agent(),
            human_input=True,
            execute=execute_task
        )



    @task
    def deploy_campaign_task(self) -> Task:
        config = self.tasks_config['deploy_campaign_task']
        
        # Extract the description and expected output
        description = config.get('description')
        expected_output = config.get('expected_output')  # Ensure you extract expected_output

        def execute_task():
            ads_result = self.current_results.get("ads_result", {})
            if not ads_result:
                print("No ads result found to deploy.")
                return {"error": "No ads to deploy"}
            
            print(f"Deploying ads on platforms: {ads_result['platforms']}")
            
            # Simulate campaign deployment
            simulated_deployment = {
                "platforms": ads_result["platforms"],
                "ad_status": "Running",
                "initial_metrics": {
                    "variant_A_CTR": 0.03,  # A variant has a 3% CTR
                    "variant_B_CTR": 0.05,  # B variant has a 5% CTR
                }
            }
            self.current_results["deployment_result"] = simulated_deployment
            return simulated_deployment
        
        return Task(
            description=description,
            expected_output=expected_output,  # Include expected_output
            agent=self.campaign_layer_agent(),
            human_input=True,
            execute=execute_task
        )


    @task
    def analyze_performance_task(self) -> Task:
        config = self.tasks_config['analyze_performance_task']
        
        # Extract the description and expected output
        description = config.get('description')
        expected_output = config.get('expected_output')  # Ensure you extract expected_output

        def execute_task():
            deployment_result = self.current_results.get("deployment_result", {})
            if not deployment_result:
                print("No deployment result found for analysis.")
                return {"error": "No deployment data to analyze"}
            
            print(f"Analyzing performance: {deployment_result}")
            
            # Simulate performance analysis
            performance_analysis = {
                "variant_A_CTR": deployment_result["initial_metrics"]["variant_A_CTR"],
                "variant_B_CTR": deployment_result["initial_metrics"]["variant_B_CTR"],
                "suggestions": ["Increase budget on LinkedIn", "Focus on Instagram"]
            }
            self.current_results["performance_result"] = performance_analysis
            
            # Make communication and adapt strategies
            self.communicate_and_adapt()
            
            return performance_analysis
        
        return Task(
            description=description,
            expected_output=expected_output,  # Include expected_output
            agent=self.decision_layer_agent(),
            human_input=True,
            execute=execute_task
        )

    @task
    def summarize_campaign_task(self) -> Task:
        config = self.tasks_config['summarize_campaign_task']
        
        # Extract the description and expected output
        description = config.get('description')
        expected_output = config.get('expected_output')  # Ensure you extract expected_output

        def execute_task():
            print("Summarizing campaign results.")
            final_summary = {
                "overall_summary": "The campaign achieved significant traction with variant B performing better.",
                "next_steps": self.current_results.get("next_steps", []),
                "best_variant": self.current_results.get("winning_variant")
            }
            self.current_results["final_summary"] = final_summary  # Save the summary in case other tasks need it
            return final_summary
        
        return Task(
            description=description,
            expected_output=expected_output,  # Include expected_output
            agent=self.manager_agent(),
            human_input=True,
            execute=execute_task
        )

    @task
    def conduct_competitor_analysis_task(self) -> Task:
        config = self.tasks_config['conduct_competitor_analysis_task']
        
        # Extract the description and expected output
        description = config.get('description')
        expected_output = config.get('expected_output')  # Ensure you extract expected_output

        # Define the agent and context correctly
        agent = self.intel_layer_agent()
        context = [self.create_strategy_task()]

        def execute_task():
            # Extract business information from inputs
            business_name = self.inputs.get("business_name", "Unknown Business")
            business_industry = self.inputs.get("business_industry", "Tech Solutions")
            usp = self.inputs.get("unique_selling_proposition", "Unknown USP")
            
            print(f"Conducting competitor analysis for: {business_name} in industry: {business_industry}")
            
            # Simulate a competitor analysis process
            competitors = [
                {"name": "InnovateTech", "strengths": ["Advanced AI technology", "User-friendly interface"],
                 "weaknesses": ["Limited support", "Higher prices"], "ad_channels": ["LinkedIn", "Facebook"],
                 "unique_selling_points": ["AI-driven insights", "Automated workflows"]},
                {"name": "ProSolution", "strengths": ["Affordable pricing", "24/7 support"],
                 "weaknesses": ["Outdated UI", "Limited integrations"], "ad_channels": ["Instagram", "Twitter"],
                 "unique_selling_points": ["Cost-effective", "Scalable solutions"]},
            ]
            
            # Simulate research findings
            research_summary = {
                "industry": business_industry,
                "primary_competitors": competitors,
                "key_observations": [
                    "Competitors are focusing heavily on AI-driven solutions",
                    "There is a gap in offering integration with existing enterprise tools",
                    "Most competitors have a strong presence on LinkedIn and Facebook"
                ],
                "opportunities": [
                    "Highlight integration capabilities in our messaging",
                    "Focus on providing excellent customer support as a differentiator",
                    "Target channels where competitors are less active, such as YouTube or TikTok"
                ],
                "threats": [
                    "Competitors have established brand recognition",
                    "Pricing may be a barrier to entry if not positioned correctly"
                ]
            }
            
            # Store results in self.current_results for access by other agents
            self.current_results["competitor_analysis"] = research_summary
            
            print("Competitor analysis completed.")
            return research_summary

        return Task(
            description=description,
            expected_output=expected_output,  # Include expected_output
            agent=agent,
            inputs=self.inputs,
            human_input=True,
            execute=execute_task
        )





    @crew
    def crew(self) -> Crew:
        """Creates the Campaigngpt crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2
        )
