# CampaignGPT

Welcome to **CampaignGPT**, an AI-driven marketing campaign generator that automates the creation, deployment, analysis, and optimization of digital marketing campaigns across platforms like Facebook and LinkedIn. Powered by [crewAI](https://crewai.com), CampaignGPT brings together multiple AI agents with distinct roles to handle every aspect of a marketing campaign, from strategy development to performance analysis. This allows you to create effective and data-driven marketing campaigns with minimal effort.

## Overview

CampaignGPT leverages a multi-agent AI system where each agent plays a specialized role in the campaign lifecycle:
- **Campaign Strategist**: Develops comprehensive campaign strategies that align with the business goals, including target audiences, messaging, and objectives.
- **Ad Creator**: Crafts compelling ad creatives based on the strategy, including ad copy, headlines, descriptions, and suggested images.
- **Campaign Manager**: Deploys and manages campaigns across different advertising platforms, ensuring proper targeting, budgets, and optimizations.
- **Performance Analyst**: Analyzes campaign performance metrics to provide actionable insights and optimization strategies.
- **Competitor Analyst**: Conducts competitor analysis to gather insights and trends that can enhance the campaign's effectiveness.
- **Campaign Manager**: Summarizes the entire campaign process, ensuring a comprehensive overview is provided for stakeholders.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` to the `.env` file**

- Modify `src/campaigngpt/config/agents.yaml` to define your agents' roles, goals, and configurations.
- Modify `src/campaigngpt/config/tasks.yaml` to define the tasks each agent will handle throughout the campaign lifecycle.
- Modify `src/campaigngpt/crew.py` to add custom logic, tools, and specific arguments tailored to your campaign needs.
- Modify `src/campaigngpt/main.py` to add custom inputs for your agents and tasks.

## Running the Project

To initiate the CampaignGPT crew and start executing tasks for your marketing campaign, run the following command from the root folder of your project:

```bash
poetry run campaigngpt
```

This command initializes CampaignGPT, activates the agents, and assigns them tasks as defined in your configuration files.

The default configuration will execute a comprehensive campaign process, including strategy creation, ad generation, campaign deployment, performance analysis, and competitor analysis. The output will be compiled into a `report.md` file with a summary of the campaign's performance and insights.

## Understanding Your CampaignGPT Crew

The CampaignGPT crew is a multi-agent system where each agent has a unique role in the campaign lifecycle. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their individual skills to create, manage, and optimize marketing campaigns effectively. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew, ensuring that every aspect of your campaign is handled by a specialized AI agent.

## Support

For support, questions, or feedback regarding CampaignGPT or crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord community](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Harness the power of AI to create data-driven marketing campaigns effortlessly with CampaignGPT and crewAI. Let’s revolutionize the way you approach digital marketing!

