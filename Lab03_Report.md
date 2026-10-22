# Lab Report 03 — Types of Intelligent Agents and How They Handle the World

**Module:** SE3062 – Intelligent Systems  
**Year:** 3rd Year, 1st Semester (2026)  
**Student IDs:** IT24104155, IT24103551, IT24200310  
**Original submission:** `IS-Lab03-IT24104155.pdf` (seven-page group report, provided by student)

## Types of Intelligent Agents and How They Handle the World

In our Intelligent Systems module we keep using the word "agent", but what does it actually mean? An agent is anything that can sense its environment through sensors and act on it through actuators, to try to reach some goal. Agents can be built in very different ways though, depending on how much information they keep and how much they think before acting. In this blog I go through the four main architectures that are simple reflex, model-based, goal-based and utility-based and explain when each one makes sense, and mention learning agents briefly near the end.

A more complex agent is not automatically the better choice. Sometimes a simple agent does the job fine, and adding planning or a utility function only adds cost without real benefit.

## The four architectures

**Simple reflex agents** work only with the current percept. They use condition-action rules, something like "if this situation, do this action". There is no memory of the past, no internal state at all. This makes them fast and cheap to build, but they fail badly when important information is not visible right now — if the agent needs to know something from a few steps ago and it's not in the current percept, it simply can't.

**Model-based agents** fix this by keeping an internal state. They combine the current perception with the history of past percepts and actions, and they hold a model of how the world works and how their own actions change it. This is useful in partially observable environments, since the agent is basically estimating what the world probably looks like right now.

**Goal-based agents** go a step further. Instead of just reacting, they have an explicit goal and use search or planning to decide which actions can reach it. This is more flexible than reflex behaviour because the agent can consider a whole sequence of actions. But goals alone only separate "good" and "bad" outcomes, not how good.

**Utility-based agents** solve that problem. When there are several acceptable outcomes, this type of agent uses a utility function to compare them, combining things like time, fuel or battery, cost, and safety, and picks the option with the best overall value.

**Learning agents** are a bit different, learning is more of an added capability than a separate reactive structure. A learning agent can improve its rules, model, or utility function over time based on feedback, and this is usually added on top of one of the four architectures above rather than replacing it.

## Quick comparison

| Agent Type | Main Idea | Memory / Internal State | Planning | Example |
|---|---|---|---|---|
| Simple Reflex | React to current percept only | No | No | Thermostat |
| Model-Based | Track internal state of the world | Yes | Limited | Robot vacuum avoiding known obstacles |
| Goal-Based | Search/plan to reach a goal | Yes | Yes | GPS navigation choosing a route |
| Utility-Based | Compare outcomes using utility function | Yes | Yes | Delivery drone balancing time, battery and safety |

## Real-world example: delivery drone

A delivery drone is a good example because the same task needs very different architectures as the environment gets more complicated. A drone that flies a fixed path and reacts to "obstacle detected which instructs it to stop" rules is basically simple reflex, fine in an empty, predictable area. Once it loses GPS for a moment or wind pushes it off course, it needs to remember its last known position and update a model of where it probably is that's model based. If it must plan a full route avoiding no-fly zones, that's goal based.

And with several valid routes, faster but more battery use, or longer but safer for it needs a utility function to weigh the trade-offs. A recent study on agent-based drone delivery describes drones this way too, as autonomous agents making local decisions across a multi-layered airspace instead of one central controller (Postorino & Sarnè, 2025). Autonomy gets added only where the environment actually needs it, not everywhere.

## Common pitfalls

A common mistake (I made this too while reading about the topic) is assuming utility based agents are always "the best" type. That's not true because in a simple, fully observable environment a simple reflex agent can be perfectly enough, and a utility function is just unnecessary overhead.

Another misconception is mixing up goal based and utility-based agents: both use planning, but only utility based agents actually rank multiple good outcomes against each other, while goal based agents just check if the goal is reached or not.

A third pitfall is thinking model based agents "know" the real world state that they don't, they only keep an internal estimate, and this estimate can be wrong if the model is not accurate.

## Conclusion

The four architectures are basically a spectrum of how much an agent perceives, remembers and reasons before acting. Simple reflex agents are fast but blind to hidden information. Model-based agents add memory for partial observability. Goal-based agents add planning towards an explicit goal. Utility-based agents go further and can rank between multiple good outcomes. The right choice depends on the environment and the task, and picking the simplest architecture that still solves the problem properly is usually the smarter engineering decision, not always jumping to the most advanced one.

## References

1. Russell, S., & Norvig, P. (2020). *Artificial intelligence: A modern approach* (4th ed.). Pearson.
2. Wooldridge, M. (2009). *An introduction to multiagent systems* (2nd ed.). Wiley.
3. Wooldridge, M., & Jennings, N. R. (1995). Intelligent agents: Theory and practice. *The Knowledge Engineering Review*.
4. Postorino, M. N., & Sarnè, G. M. L. (2025). Operational performance of a 3D urban aerial network and agent-distributed architecture for freight delivery by drones. *Drones, 9*(11), Article 759.

> This Markdown is a readable transcription of the student's submitted Lab 03 PDF. The PDF's original page design and images are not embedded in this Markdown copy.
