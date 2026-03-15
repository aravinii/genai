# Gen AI
Hands-on exploration of Generative AI through structured courses, experiments, and applied projects.

## Context
Over the past few years, the field of Generative AI has evolved at an unprecedented pace. What once lived primarily in research papers and benchmarks is now embedded in APIs, SDKs, and real-world products. Models have become more capable, more accessible, and more integrated into practical systems.

Amid this acceleration, I decided not only to follow the trend, but to deepen my understanding in a structured way. This repository is the result of that effort: a hands-on journey through courses, experiments, and applied projects designed to move beyond surface-level usage and into implementation, evaluation, and system design.

## Courses
The [`course/`](course/) folder holds materials from two courses used as a base for this repo: **Generative AI** (Google/Kaggle — prompting, RAG, function calling, agents) and **Agentic AI** (DeepLearning.AI — reflection, tool use, planning, multi-agent design). Notebooks and deliverables are organized by course in the subfolders; see each subfolder’s README for details.

## Real Estate Multi-Agent with tools
As a capstone project, this repo implements a **multi-agent** real estate assistant (Quarto) for selected São Paulo neighborhoods. A **planner** agent holds the conversation and routes the user to two specialists: a **research** agent (qualitative neighborhood analysis, with optional web search) and a **pricing** agent (collects property details and returns a price estimate via an ML model served by API). The result is a single conversational flow that combines LLM-driven routing and reasoning with structured data and a trained pricing model. See [real_estate_agent/](real_estate_agent/) for structure and prompts.

## Setup and run the agent
1. **Clone** the repository.
2. **Install dependencies:**  
   `python -m venv .venv`, then `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`), then `pip install -r requirements.txt`.
3. **Run** `python start_here.py` from the repo root to start the conversation in the terminal.

For a more visual, notebook-based flow, open [real_estate_agent/notebooks/planner_agent.ipynb](real_estate_agent/notebooks/planner_agent.ipynb) and run the cells (start the server in the first cell, then use the chat in the next).
