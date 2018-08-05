#This is the definition of effects.
#There are three types of powers an ore can have:
#1: overrides.
#Overrides are only for the most powerful ores, these rewrite an effect of another ore of any prioritythey can't override overrides or additions.)
#2: additions.
#Additions are for moderate and high powered ores, they extend the effect of another ore by adding an extra calculation to an existing effect.
#3: effects.
#Effects are the most basic power. An effect takes a base chance that a mob will spawn, and applies an equation to it to make a new chance.

ores = {
    "light" :
        {
            "priority" : 1,
            "priorityFlag" : 1,
            "overrides" :
                {
                    "water" :
                        {
                            "testmob" : (2, lambda x: x + 1),
                        },
                },
            "additions" :
                {
                    "lava" :
                        {
                            "testmob" : lambda x: x + 1,
                        }
                },
            "effects" :
                {
                    "testmob" : lambda x: x + 2,
                }
        },
        
    "lava" :
        {
            "priority" : 1,
            "priorityFlag" : 1,
            "overrides" :
                {
			"water" :
				{
					"testmob" : lambda x: x + 3,
				},
                },
            "additions" :
               {
               },
            "effects" :
               {
                   "testmob": lambda x: x + 2,
               }
        },
        
    "water" :
        {
            "priority" : 3,
            "priorityFlag" : 3,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
			"testmob" : lambda x: x + 2
                }
        },
        
    "dona" :
        {
            "priority" : 4,
            "priorityFlag" : 4,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "gash" :
        {
            "priority" : 5,
            "priorityFlag" : 5,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "nee" :
        {
            "priority" : 6,
            "priorityFlag" : 6,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "shal" :
        {
            "priority" : 7,
            "priorityFlag" : 7,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "vus" :
        {
            "priority" : 8,
            "priorityFlag" : 8,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "yos" :
        {
            "priority" : 9,
            "priorityFlag" : 9,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "besh" :
        {
            "priority" : 10,
            "priorityFlag" : 10,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "klam" :
        {
            "priority" : 11,
            "priorityFlag" : 11,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "mee" :
        {
            "priority" : 12,
            "priorityFlag" : 12,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "queem" :
        {
            "priority" : 13,
            "priorityFlag" : 13,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "sal" :
        {
            "priority" : 14,
            "priorityFlag" : 14,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "wem" :
        {
            "priority" : 15,
            "priorityFlag" : 15,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "ama" :
        {
            "priority" : 16,
            "priorityFlag" : 16,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "zak" :
        {
            "priority" : 17,
            "priorityFlag" : 17,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "ael" :
        {
            "priority" : 18,
            "priorityFlag" : 18,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "jash" :
        {
            "priority" : 19,
            "priorityFlag" : 19,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "ip" :
        {
            "priority" : 20,
            "priorityFlag" : 20,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "um" :
        {
            "priority" : 21,
            "priorityFlag" : 21,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "hamee" :
        {
            "priority" : 22,
            "priorityFlag" : 22,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "om" :
        {
            "priority" : 23,
            "priorityFlag" : 23,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "chal" :
        {
            "priority" : 24,
            "priorityFlag" : 24,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "ipe" :
        {
            "priority" : 25,
            "priorityFlag" : 25,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "eef" :
        {
            "priority" : 26,
            "priorityFlag" : 26,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "oom" :
        {
            "priority" : 27,
            "priorityFlag" : 27,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "pas" :
        {
            "priority" : 28,
            "priorityFlag" : 28,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "rus" :
        {
            "priority" : 29,
            "priorityFlag" : 29,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "los" :
        {
            "priority" : 30,
            "priorityFlag" : 30,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },
        
    "ome" :
        {
            "priority" : 31,
            "priorityFlag" : 31,
            "overrides" :
                {
                },
            "additions" :
                {
                },
            "effects" :
                {
                }
        },

}
