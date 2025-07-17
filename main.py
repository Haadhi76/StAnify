from crewai import Agent, Task, Crew

# Agent 1: Planner
planner = Agent(
    role="Concept-to-Narrative Planner",
    goal="Create a child-friendly story outline from a concept",
    backstory="You are a narrative expert for kids' education.",
    verbose=True
)

# Agent 2: Scene Generator
scene_gen = Agent(
    role="Scene Generator",
    goal="Generate three visual scenes from a story outline",
    backstory="You turn story beats into picture book scenes.",
    verbose=True
)

# Tasks
task1 = Task(
    description="Turn the concept 'multiplication' into a story outline.",
    agent=planner
)
task2 = Task(
    description="Take the story outline and generate three visual scene prompts.",
    agent=scene_gen
)

crew = Crew(
    agents=[planner, scene_gen],
    tasks=[task1, task2],
    verbose=True
)

results = crew.run()
print(results)
