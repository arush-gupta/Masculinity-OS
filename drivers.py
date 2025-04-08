"""
drivers.py — Represents influences like biology, socialization, trauma, etc.
These are the underlying forces that affect behavioral output.
"""

class InfluenceDriver:
    def __init__(self, name, source, intensity):
        self.name = name
        self.source = source  # e.g., 'biological', 'cultural', 'personal'
        self.intensity = intensity  # scale 1-10

    def influence_level(self):
        return f"{self.name} from {self.source}: {self.intensity}/10"


# Example:
#bio = InfluenceDriver("Sexual Drive", "biological", 8)
#trauma = InfluenceDriver("Abandonment Wound", "personal", 9)
