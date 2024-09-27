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
        config=self.agents_config['manager_agent']
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

    @task
    def create_strategy_task(self) -> Task:
        config = self.tasks_config['create_strategy_task']
        print("config: " , config)
        # Extracting the values from config
        description = config.get('description')
        expected_output = config.get('expected_output')
		
		# Define the agent and context correctly
        agent = self.business_layer_agent()  # Assigning the agent instance directly
        context = [self.manager_agent()]     # Assigning the context instance directly
		
        print("description: " , description)
        print("expected_output: " , expected_output)
        print("agent: " , agent)
        print("context: " , context)
        return Task(
			description=description,
			expected_output=expected_output,
			agent=agent,
			inputs=self.inputs
		)


    @task
    def create_ads_task(self) -> Task:
        config = self.tasks_config['create_ads_task']
        description = config.get('description')
        expected_output = config.get('expected_output')
		
		# Define the agent and context correctly
        agent = self.business_layer_agent()  # Assigning the agent instance directly
        context = [self.create_strategy_task()]     # Assigning the context instance directly
		
        print("description: " , description)
        print("expected_output: " , expected_output)
        print("agent: " , agent)
        print("context: " , context)
        return Task(
			description=description,
			expected_output=expected_output,
			agent=agent,
			inputs=self.inputs
		)

    @task
    def deploy_campaign_task(self) -> Task:
        config = self.tasks_config['deploy_campaign_task']
        description = config.get('description')
        expected_output = config.get('expected_output')
		
		# Define the agent and context correctly
        agent = self.business_layer_agent()  # Assigning the agent instance directly
        context = [self.create_ads_task()]     # Assigning the context instance directly
		
        print("description: " , description)
        print("expected_output: " , expected_output)
        print("agent: " , agent)
        print("context: " , context)
        return Task(
			description=description,
			expected_output=expected_output,
			agent=agent,
			inputs=self.inputs
		)

    @task
    def analyze_performance_task(self) -> Task:
        config = self.tasks_config['analyze_performance_task']
        description = config.get('description')
        expected_output = config.get('expected_output')
		
		# Define the agent and context correctly
        agent = self.business_layer_agent()  # Assigning the agent instance directly
        context = [self.deploy_campaign_task()]     # Assigning the context instance directly
		
        print("description: " , description)
        print("expected_output: " , expected_output)
        print("agent: " , agent)
        print("context: " , context)
        return Task(
			description=description,
			expected_output=expected_output,
			agent=agent,
			inputs=self.inputs
		)

    @task
    def conduct_competitor_analysis_task(self) -> Task:
        config = self.tasks_config['conduct_competitor_analysis_task']
        print("config: ", config)
        
        # Extracting the values from the config
        description = config.get('description')
        expected_output = config.get('expected_output')
        
        # Define the agent and context correctly
        agent = self.intel_layer_agent()  # Assigning the agent instance directly
        context = [self.create_strategy_task()]  # Referencing the appropriate task in the context
        
        print("description: ", description)
        print("expected_output: ", expected_output)
        print("agent: ", agent)
        print("context: ", context)
        
        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            inputs=self.inputs
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
