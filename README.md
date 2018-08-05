# mobspawnsim
calculates chance of a mob spawning in a certain environment.
There are three types of powers an ore can have:
1: overrides.
Overrides are only for the most powerful ores, these rewrite an effect of another ore of any priority as long as that effect has not been overriden already by a more powerful ore. They can't override overrides or additions.)
2: additions.
Additions are for moderate and high powered ores, they extend the effect of another ore by adding an extra calculation to an existing effect.
3: effects.
Effects are the most basic power. An effect takes a base chance that a mob will spawn, and applies an equation to it to make a new chance.

Two ores may have the same priority, but if two ores of equal priority contain an override for the same effect, an error will be thrown and the situation must be resolved.

When writting effects, please put a comment with each ore to explain its general behavior, or if it doesn't have any general behavior say so.
Please also put a comment by each individual override/addition/effect to explain its behavior.

It is possible to specify a special priority specefic to a given effect as follows:
Instead of normal function definition "lambda x: functionDef"
Write "(specialPriority, lambda x: functionDef)"
