#ores = {
#"iron": {
#
#"priority": 4,
#
#"overrides": {
#
#"coal": {
#
#"mob1": lambda x: x + 3,
#"mob2": lambda x: x + 4,
#
#},
#
#"dirt": {
#
#"mob1": lambda x: x + 5,
#"mob2": lambda x: x + 6,
#
#},
#
#},
#
#"effects": {
#"mob1": lambda x: x + 1,
#"mob2": lambda x: x + 2}
#},
#
#}

import spawnData
import locDef
import sys

locDef = locDef.locDef

ores = spawnData.ores

for oreName in locDef:
    if locDef[oreName] == 0:
        continue
    oreData = ores[oreName]
    priority = oreData["priority"]
    overrides = oreData["overrides"]
    for oreGroup in overrides:
        for override in overrides[oreGroup]:
            targetOre = ores[oreGroup]
            targetPriorityFlag = targetOre["priorityFlag"]
            if targetPriorityFlag < priority:
                continue
            else:
                targetOre["priorityFlag"] = priority
                targetOre["effects"][override] = overrides[oreGroup][override]
            
    additions = oreData["additions"]
    for overrideAdd in additions:
        for addition in additions[overrideAdd]:
            targetOre = ores[overrideAdd]
            oldEffect = targetOre["effects"][addition]
            newEffect = additions[overrideAdd][addition]
            targetOre["effects"][addition] = lambda x : newEffect(oldEffect(x))
            
while 1:

    effects = []

    mobName = raw_input("mobName? >> ")
    chance = int(raw_input("chance? >> ")) + 0.0

    for oreName in locDef:
        oreData = ores[oreName]
        oreEffects = oreData["effects"]
        if mobName in oreEffects:
            effect = oreEffects[mobName]
        else:
            continue
        for i in range(locDef[oreName]):
            effects.append(effect)
        
    nums = []
    for effect in effects:
        nums.append(effect(chance) - chance)
    if nums:
        sumOfNums = sum(nums)
        print chance + sumOfNums / (len(nums) + 0.0)
    else:
        print chance
