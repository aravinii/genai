# Available Houses Dataset

This dataset contains 1,346 real estate property records from the city of São Paulo, Brazil. It includes 8 structured features describing property characteristics, pricing information, and location attributes.

The dataset is structured for real estate market analysis, pricing modeling, and exploratory data analysis. It enables evaluation of how structural attributes and location influence property valuation within São Paulo.

### Columns
	•	price: Property listing price in Brazilian Reais (BRL).
	•	type: Property category, either Apartment or House.
	•	region_name: Name of the São Paulo region where the property is located.
	•	total_area: Total property area measured in square meters.
	•	bedrooms: Number of bedrooms in the property.
	•	bathrooms: Number of bathrooms in the property.
	•	iptu: Annual municipal property tax (Imposto Predial e Territorial Urbano) paid by the owner, in BRL.
	•	parking_slots: Number of parking spaces available.

# Conversation data & reports

- **`conversations.json`** — Exported multi-turn chats (messages, roles, token counts, latencies).
- **`conversation_metrics_report.md`** — Auto-generated metrics overview; embeds **`conversation_metrics_latency.png`**. Regenerate both with `real_estate_agent/notebooks/conversation_metrics.ipynb`.
