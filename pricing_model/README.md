# Pricing Model

This directory contains the machine learning pipeline developed to estimate property prices based on structured real estate features.

The primary objective of this module is not to build a state-of-the-art pricing engine, but to reinforce core ML engineering practices and prepare a deployable model artifact to be integrated into the AI agent developed in this repository.

⸻

## Overview

The pricing workflow is divided into two main stages:

**1. Exploratory Analysis**

The process begins in the `exploratory_analysis.ipynb` notebook.

In this notebook:
	•	Data is loaded from the data/ directory
	•	A lightweight exploratory data analysis (EDA) is performed
	•	Distributions and relationships between key features are inspected
	•	Basic data cleaning strategies are proposed

The goal of this stage is to understand the structure, scale, and statistical behavior of the dataset before formal modeling.

⸻

**2. Model Training** 

The `model_training.ipynb` notebook formalizes the modeling process.

Key elements include:
	•	Use of structured machine learning pipelines
	•	Feature preprocessing and transformations
	•	Training of an XGBoost regression model
	•	Performance evaluation using cross-validation techniques

The modeling approach emphasizes reproducibility, modularity, and alignment with software engineering best practices.

While the model does not achieve particularly high predictive performance, that was not the primary goal. The focus was:
	•	Skill reinforcement
	•	Clean ML workflow implementation
	•	Artifact generation for downstream system integration

The `requirements.txt` file specifies the exact library versions used during model development.

⸻

## Model Artifact

The trained model is serialized as a pickle object called `house_price_model.joblib`.

This artifact is intended to serve as a callable pricing function within the AI agent architecture developed in this repository.

Future steps include:
	•	Defining a clean inference interface
	•	Integrating the model into the agent pipeline
	•	Handling input validation and feature consistency
	•	Implementing production-ready loading mechanisms