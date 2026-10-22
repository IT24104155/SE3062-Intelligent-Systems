# agent.py
import random


class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # If standing directly on food, or just wander / move towards coordinates
        pos = percept['agent_pos']
        # Simple heuristic or fallback random sweep
        return random.choice(self.actions_pool)


class SimpleReflexAgent:
    """
    A simple reflex agent that makes decisions purely based on current perceptions.
    It does not have any internal memory or historical knowledge of past states.

    Lecture Concept: Condition-Action Rules (If-Then Rules)
    - Receives a percept (e.g. food present or wall ahead) and maps it directly to an action.
    - Operates under the assumption of a fully observable or immediately actionable state.
    """

    def __init__(self):
        self.actions = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # Condition-Action Rule 1: If standing on food, move forward to collect/keep moving
        if percept.get('food_here'):
            return 'Up'

        # Condition-Action Rule 2: If a wall is ahead, change direction to avoid hitting it
        if percept.get('wall_ahead'):
            return 'Right'

        # Default action
        return 'Up'


class ModelBasedAgent:
    """
    A model-based reflex agent that maintains an internal state (memory) to track
    the history of the environment. This helps solve loops arising from partial observability.

    Lecture Concept: Internal State / Model of the World
    - Maintains a memory of past actions (`self.last_action`).
    - Uses this internal representation to make decisions that avoid repetitive failures (like hitting the same wall twice).
    """

    def __init__(self):
        self.actions = ['Up', 'Right', 'Down', 'Left']
        # Internal state to remember the last action executed
        self.last_action = None

    def sense_and_act(self, percept: dict) -> str:
        # If a wall is ahead, update action selection based on our memory/history
        if percept.get('wall_ahead'):
            # Filter out the last action to ensure we change direction and escape the corner loop
            available_actions = [a for a in self.actions if a != self.last_action]
            action = available_actions[0]
        else:
            action = 'Up'

        # Update the internal state with the selected action
        self.last_action = action
        return action


class SearchAgent:
    """Stub class for SearchAgent to be implemented in Lab 02."""
    pass
