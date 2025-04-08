"""
utils.py — Tools for internal reflection, system diagnostics, and rewriting identity scripts.
"""

def self_diagnostic(identity):
    report = identity.summary()
    return f"System Check:\nName: {report['Name']}\nValues: {report['Values']}\nPurpose: {report['Purpose']}"

def rewrite_narrative(old_script, new_script):
    return f"Narrative Overwrite:\nOLD: {old_script}\nNEW: {new_script}"
