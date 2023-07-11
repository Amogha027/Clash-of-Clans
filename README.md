### Name: Amogha A Halhalli
### Roll No.: 2021101007
---
# Assignment 3

- Everything mentioned in the assignment has been implemented.
- **Bonus** :
    - King’s Leviathan Axe has also been implemented.
    - Dragon Character has been added, it can fly over walls.
    - Queen's Eagle Arrow has been added.
    - Movement avoiding walls has also been implemented.

- To run the game : `python3 game.py`
- To view replays : `python3 replay.py`  and select the replay you want to watch according to mentioned date and time.
- For Victory : All buildings apart from walls get destroyed from the map in all three levels.
- For Defeat : If all troops and King die before destroying all buildings apart from walls.

## Controls :

### Hero :

- w : move up
- a : move left
- d : move right
- s : move down
- 1 : Special Attack
- space : Normal Attack

### Barbarian :

- z : spawn at point 1
- x : spawn at point 2
- c : spawn at point 3

### Dragon :

- v : spawn at point 1
- b : spawn at point 2
- n : spawn at point 3

### Archer :

- i : spawn at point 1
- o : spawn at point 2
- p : spawn at point 3

### Stealth Archer :

- t : spawn at point 1
- y : spawn at point 2
- u : spawn at point 3

### Balloon :

- j : spawn at point 1
- k : spawn at point 2
- l : spawn at point 3

### Healer :

- e : spawn at point 1
- f : spawn at point 2
- g : spawn at point 3

q : Quit Game

## Assumptions :

- Rage and Heal Spell can be applied multiple times.
- The limit for troops in each level is as follows :
    - Barbarians : 10
    - Archers : 7
    - Balloon : 5
    - Dragon : 3
    - Healer : 5
    - Stealth Archer : 7
    
- You have to choose the type of troop movement at start of the game.
- You have to choose the hero after each level.
- The level of each cannon, each wizard tower or walls can be changed in points.py

## Stealth Archers :

- Inherited from the class of Archer.
- Invisible for the first ten seconds.
- Can attack other buildings all the time.
- Other buildings cannot attack during the invisibility.
- Once visible, it behaves just like an archer.

## Healers :

- Healers find the nearest troop whose health is not maximum.
- Manhattan distance is used to find the nearest troop.
- Increase the health of the nearest troop including the king.
- Euclidean distance is used to find the troop in the range.
- Healers heal troops in a certain AoE around its target location.
- Heal range is 7 tiles with heal radius being 1.
- Game ends if only healers are remaining in the battle field.

## Building Levels :

- Each building have a level (between 1 and 5, both inclusive).
- The level of walls, each cannon & wizard tower can be configured in points.py file.
- The level of a building will control its health, damage, and other attributes.
-  For Cannon and Wizard Tower:
    - Attack = 4 + level
    - Attack Range = 5 + (level/2)
    - Max Health = 20 + 30*level
- For Wall:
    - Max Health = 20 + 40*level
    - Walls with level >= 3 will explode upon being destroyed.
        - Explosion damage: 50
        - Explosion radius: 2 tiles
        
## Assumptions :

- Rage and Heal Spell can be applied multiple times.
- The limit for troops in each level is as follows :
    - Barbarians : 10
    - Archers : 7
    - Balloon : 5
    - Dragon : 3
- You have to choose the type of troop movement at start of the game.
- You have to choose the hero after each level.

---
# Assignment-4
- Unit Tests are written to check the funtionality of the move function of king of the provided codebase.
- The test.py file would be kept in the 'src' directory of the codebase to be evaluated.
- 'True' or 'False' string is output to a file named 'output.txt' indicating whether the provided codebase passes or fails the unit tests respectively.

### Bonus Part:
- Unit Tests are written to check the funtionality of the attack_target function of king of the provided codebase.
- The test_bonus.py file would be kept in the 'src' directory of the codebase to be evaluated.
- 'True' or 'False' string is output to a file named 'output_bonus.txt' indicating whether the provided codebase passes or fails the unit tests respectively.
