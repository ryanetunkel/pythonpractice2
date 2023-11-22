import math
import csv
from enum import Enum

'''Function that can calculate the lowest possible levels needed to deal all types of damage in D&D 5e in one melee attack'''

# Background, feats, class, species, cantrip, concentration

SOURCES = []

with open("./recreational/Rainbow Warrior.csv",newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        SOURCES.append(', '.join(row))

print(SOURCES)

sources_list = []
for idx in range(len(SOURCES)):
    sources_list.append(SOURCES[idx].split(', '))
    print(sources_list[idx])
print(sources_list)

class Source(Enum):
    NONE = 0
    WEAPON = 1
    POISON = 2
    BACKGROUND = 3
    CANTRIP = 4
    FEAT = 5
    SPECIES = 6
    CONCENTRATION = 7
    CLASS = 8
    REPETITIVE = CLASS # Call to check if the source can be used again

class Damage():
    def __init__(self, name, source, levels, source_name):
        self.name = name
        self.source = source
        self.levels = levels
        self.source_name = source_name
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_source(self):
        return self.source
    
    def set_source(self,new_source,new_source_name):
        self.source = new_source
        self.set_source_name(new_source_name)
    
    def get_levels(self):
        return self.levels
    
    def set_levels(self, new_levels):
        self.levels = new_levels
    
    def get_source_name(self):
        return self.source_name
    
    def set_source_name(self,new_source_name):
        self.source_name = new_source_name
        
class Build():
    def __init__(self):
        self.damages = Damage [("Acid",0,0,""),
                               ("Bludgeoning",Source.CLASS,1,"Genie Warlock"),
                               ("Cold",0,0,""),
                               ("Fire",0,0,""),
                               ("Force",0,0,""),
                               ("Lightning",0,0,""),
                               ("Necrotic",0,0,""),
                               ("Piercing",0,0,""),
                               ("Poison",Source.POISON,0,"Poison"),
                               ("Psychic",0,0,""),
                               ("Radiant",0,0,""),
                               ("Slashing",Source.WEAPON,0,"Greatsword"),
                               ("Thunder",0,0,"")]
        self.levels = 1
    
    def get_damages(self):
        return self.damages
    
    def set_damages(self, idx, new_damages):
        self.damages[idx] = new_damages
        
    def get_levels(self):
        return self.levels
    
    def set_levels(self, new_levels):
        self.levels = new_levels
        
    def add_levels(self, added_levels):
        self.levels += added_levels
    
    def update_levels(self):
        self.set_levels(0)
        for dmg in self.get_damages():
            self.add_levels(dmg[2])

def check_source(build, source_search):
    source_used = False
    for dmg in build.damages:
        if dmg[1] == source_search:
            source_used = True
            break
    return source_used

def compare_build_level(build1, build2):
    if build1.levels > build2.levels:
        return 1
    if build1.levels == build2.levels:
        return 0
    if build1.levels < build2.levels:
        return -1

def calculate_lowest_levels():
    build_index = []
    feats_range = range(1,2 + 1) # 1 - 2 
    species_range = range(3,5 + 1) # 3 - 5
    cantrips_range = range(6,7 + 1) # 6 - 7
    backgrounds_range = 8 # Just 8
    concentration_range = range(9,20 + 1) # 9 - 20
    classes_range = range(21,42 + 1) # 21 - 42
    class Damage_Type(Enum): # For referencing row numbers more easily
        ACID = 2
        COLD = 3
        FIRE = 4
        FORCE = 5
        LIGHTNING = 6
        NECROTIC = 7
        PIERCING = 8
        PSYCHIC = 9
        RADIANT = 10
        THUNDER = 12
    
    # Start traversals at 1 for columns and 2 for rows
    
    # Species
    for species_idx in species_range: # Species range in csv
        return 0 # REMOVE - so it won't give an error
    
    return 0