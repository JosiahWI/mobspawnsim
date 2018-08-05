import spawnData
import locDef

locDef = locDef.locDef

ores = spawnData.ores

for oreName in locDef:
    if locDef[oreName] == 0:
        continue
    oreData = ores[oreName]
    overrides = oreData["overrides"]
    for oreGroup in overrides:
        for override in overrides[oreGroup]:
            priority = oreData["priority"]
            targetOre = ores[oreGroup]
            targetPriorityFlag = targetOre["priorityFlag"]
            if type(overrides[oreGroup][override]) == tuple:
	        print "special"
                priority = override[0]
                override = override[1]
            if targetPriorityFlag == priority:
                raise StandardError("Ore %s is attempting to override effect %s in ore %s, but there is a priority clash. Source priority: %d. Target priority flag: %d" % (oreName, override, oreGroup, priority, targetPriorityFlag))
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
