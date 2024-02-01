from crewai import Task


class TheologyTasks:
    def draft_task(self, agent, topic):
        return Task(description="{topic}", agent=agent)

    def scripture_task(self, agent, topic):
        return Task(description="", agent=agent)

    def luther_task(self, agent, topic):
        return Task(description="", agent=agent)
