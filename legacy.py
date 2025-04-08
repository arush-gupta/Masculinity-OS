"""
legacy.py — Contains outdated modules like Alpha/Beta scripts, validation loops,
and performative masculinity. Useful for backward compatibility and analysis.
"""

class LegacyScript:
    def __init__(self, name, obsolete=True):
        self.name = name
        self.obsolete = obsolete

    def run(self):
        if self.obsolete:
            return f"[Warning] {self.name} is deprecated. Consider updating."
        return f"{self.name} script executed."

# Examples:
alpha_script = LegacyScript("Alpha Male Performance")
validation_loop = LegacyScript("External Validation Loop")
