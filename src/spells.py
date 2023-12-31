from characters import barbarians, dragons, balloons, archers, stealth_archers, healers


def rage_spell(King):
    if King.alive == True:
        King.rage_effect()
    for barb in barbarians:
        if barb.alive == True:
            barb.rage_effect()
    for arch in archers:
        if arch.alive == True:
            arch.rage_effect()
    for dr in dragons:
        if dr.alive == True:
            dr.rage_effect()
    for bl in balloons:
        if bl.alive == True:
            bl.rage_effect()
### begin ###
    for star in stealth_archers:
        if star.alive == True:
            star.rage_effect()
    for he in healers:
        if he.alive == True:
            he.rage_effect()
### end ###

def heal_spell(King):
    if King.alive == True:
        King.heal_effect()
    for barb in barbarians:
        if barb.alive == True:
            barb.heal_effect()
    for arch in archers:
        if arch.alive == True:
            arch.heal_effect()
    for dr in dragons:
        if dr.alive == True:
            dr.heal_effect()
    for bl in balloons:
        if bl.alive == True:
            bl.heal_effect()
### begin ###
    for star in stealth_archers:
        if star.alive == True:
            star.heal_effect()
    for he in healers:
        if he.alive == True:
            he.heal_effect()
### end ###