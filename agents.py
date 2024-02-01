from crewai import Agent


class TheologyAgents:
    def bible_scholar(self):
        return Agent(
            role="Professor of Biblical Studies",
            goal="Study Old and New Testament, and weave scriptural reference into theological works in a compelling way",
            backstory="",
            verbose=True,
            allow_delegation=True,
        )

    def theologian(self):
        return Agent(
            role="Profession of Protestant Theology and Theologian",
            goal="Write theological essays and outlines in a Protestant tradition",
            backstory="",
            verbose=True,
            allow_delegation=True,
        )

    def lutheran_theologian(self):
        return Agent(
            role="Professor of Lutheran Theology",
            goal="Write theology in the Lutheran tradition and make compelling use of evidence from Martin Luther's writings",
            backstory="",
            verbose=True,
            allow_delegation=True,
        )
