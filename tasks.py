from textwrap import dedent
from crewai import Task


class TheologyTasks:
    def draft_task(self, agent, topic):
        return Task(
            description=dedent(
                """\
                    Write a series of theses, no more than 10, that outline a new theological perspective on {topic}.
                    Theses should be concise and clear, and in a logical order. Group together theses in subgroups as needed.
                    The final result should be a numbered list."""
            ),
            agent=agent,
        )

    def scripture_task(self, agent, topic):
        return Task(
            description=dedent(
                """\
                    Identify passages from the Old and New Testaments relevant to {topic} and the theses provided, no more than 5 passages total. 
                    Provide the book, chapter, and verse of each passage, along with a one sentence explanation of relevance for the topic and theses."""
            ),
            agent=agent,
        )

    def synthesis_task(self, agent, topic):
        return Task(
            description=dedent(
                """\
                    Write a 500 word short essay on {topic} that weaves together the theological theses and scriptural evidence."""
            ),
            agent=agent,
        )
