from tabnanny import verbose
from dotenv import load_dotenv

load_dotenv()

from crewai import Crew

from tasks import TheologyTasks
from agents import TheologyAgents

tasks = TheologyTasks()
agents = TheologyAgents()

topic = input("What topic should we theologize about today?")

# Create Agents
theologian_agent = agents.theologian()
bible_agent = agents.bible_scholar()
lutheran_agent = agents.lutheran_theologian()

# Create Tasks
draft_thology = tasks.draft_task(theologian_agent, topic)
# will need to update to make sure that the draft from the first tasks is passed to the bible agent
add_scripture = tasks.scripture_task(bible_agent, topic)
# make it more lutheran
add_luther = tasks.luther_task(lutheran_agent, topic)

# Create Crew
crew = Crew(
    agents=[theologian_agent, bible_agent, lutheran_agent],
    tasks=[draft_thology, add_scripture, add_luther],
    verbose=True,
)

game = crew.kickoff()

# Print our new theology
print("Here's our theological imagining")
print("\n\n###############")
print(topic)
