from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "real_estate_agent"))


from agents.planner_agent import planner_agent
from utils.pricing_model_deploy import start_server

start_server() 
planner_agent()