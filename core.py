"""
core.py — Core system functions that define the foundation of Masculinity.OS:
identity, values, and purpose.
"""

class Identity:
    def __init__(self, name="User", values=None):
        self.name = name
        self.values = values or []
        self.purpose = None

    def set_purpose(self, purpose):
        self.purpose = purpose

    def add_value(self, value):
        if value not in self.values:
            self.values.append(value)

    def summary(self):
        return {
            "Name": self.name,
            "Values": self.values,
            "Purpose": self.purpose
        }
