"""
ui.py — Manages interface behaviors: dating, relationships, expression of masculinity.
"""

def display_behavior(identity, context):
    if context == "dating":
        return f"{identity.name} presents confidence, curiosity, and groundedness."
    elif context == "work":
        return f"{identity.name} integrates purpose with presence."
    return f"{identity.name} expresses authentic masculinity."


def handle_rejection():
    return "Processing feedback... Identity intact. Re-routing purpose."
