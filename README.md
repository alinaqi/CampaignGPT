# CampaignGPT Project Overview

Welcome to **CampaignGPT**! This project demonstrates how to implement an AI-driven marketing campaign manager using three different frameworks: CrewAI, AutoGen, and LangGraph. Each subproject serves as a unique approach to building an AI-powered campaign management system.

## Project Structure

The project is organized into three main directories:

```
CampaignGPT
│
├── campaigngpt/               # Implementation using CrewAI
├── campaigngpt_autogen/       # Implementation using AutoGen
└── campaigngpt_langgraph/     # Implementation using LangGraph
```

## Overview of Each Implementation

### 1. CampaignGPT Using CrewAI
- **Directory:** `campaigngpt/`
- **Framework:** [CrewAI](https://www.crewai.com/open-source)
- **Description:** This version of CampaignGPT uses CrewAI to build an agent-based system that manages different aspects of the campaign. It focuses on creating multiple agents for tasks such as strategy development, ad creation, campaign deployment, and performance analysis.
- **Highlights:** 
  - Task orchestration with multiple agents
  - Human feedback loop integrated for agent decision-making

### 2. CampaignGPT Using AutoGen
- **Directory:** `campaigngpt_autogen/`
- **Framework:** [AutoGen](https://github.com/microsoft/autogen)
- **Description:** This implementation leverages Microsoft’s AutoGen framework to build a multi-agent system for campaign management. It automates the communication between agents and handles tasks like strategy, ad creation, and analysis through LLM-powered agents.
- **Highlights:** 
  - Autonomous agent-to-agent communication
  - Easy configuration for LLM-based interactions
  - Task automation with human-in-the-loop capabilities

### 3. CampaignGPT Using LangGraph
- **Directory:** `campaigngpt_langgraph/`
- **Framework:** [LangGraph](https://langchain-ai.github.io/langgraph/)
- **Description:** The LangGraph implementation offers a graph-based approach to building AI workflows. It allows you to define complex workflows for the campaign by defining stateful interactions between various nodes (tasks) in a graph.
- **Highlights:** 
  - Graph-based task management with customizable nodes
  - Supports OpenAI's API for LLM interactions
  - Powerful state management and workflow orchestration

## How to Get Started

### Prerequisites
- Python 3.8+
- Install dependencies using `pip`:
  ```
  pip install -r requirements.txt
  ```

### Running Each Version

#### CrewAI Version
1. Navigate to the `campaigngpt/` directory:
   ```bash
   cd campaigngpt
   ```
2. Run the application:
   ```bash
   python main.py
   ```

#### AutoGen Version
1. Navigate to the `campaigngpt_autogen/` directory:
   ```bash
   cd campaigngpt_autogen
   ```
2. Run the application:
   ```bash
   python main.py
   ```

#### LangGraph Version
1. Navigate to the `campaigngpt_langgraph/` directory:
   ```bash
   cd campaigngpt_langgraph
   ```
2. Run the application:
   ```bash
   python main.py
   ```

## How Each Version Differs

| Feature                   | CrewAI                     | AutoGen                   | LangGraph                 |
|---------------------------|----------------------------|---------------------------|---------------------------|
| **Agent Interaction**     | Human feedback loop        | Autonomous multi-agents   | Graph-based interaction   |
| **Task Management**       | Defined via tasks          | Dynamic agent tasks       | Node-based task execution |
| **LLM Integration**       | Via individual agents      | LLM-powered agents        | OpenAI API via nodes      |
| **State Management**      | Handled within CrewAI      | Automatic in AutoGen      | Managed via state graph   |

## Which Version Should You Use?

- **CrewAI:** Ideal if you want a structured approach to defining agents and tasks with human feedback.
- **AutoGen:** Best for those interested in autonomous agent communication with a focus on LLM integration.
- **LangGraph:** Suitable for users who prefer a graph-based approach to task management and workflow orchestration.

## Contribution

Feel free to open issues or pull requests to improve the project. Contributions are welcome!

## License

This project is open-source and licensed under the MIT License.

## Author

Ali Shaheen, ashaheen@workhub.ai & ali.shaheen@zenloop.com
