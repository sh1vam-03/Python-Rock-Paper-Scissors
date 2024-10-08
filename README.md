﻿
# Rock, Paper, Scissors Game in Python

This is a simple command-line Rock, Paper, Scissors game implemented in Python. The player competes against the computer, which randomly chooses rock, paper, or scissors. The game continues until the player decides to quit.

## Table of Contents

- [How to Play](#how-to-play)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Game Rules](#game-rules)
- [Example Output](#example-output)
- [Future Enhancements](#future-enhancements)

## How to Play

1. The game prompts the player to input one of three options: rock, paper, or scissors.
2. The computer randomly selects one of the three options.
3. The result of the game is displayed (win, lose, or tie).
4. The player is asked if they would like to play again.
5. The game continues until the player chooses to quit.

## Installation

To run this game, you need Python installed on your computer.

### Steps to install:

1. **Install Python:**
   - Download and install the latest version of Python from [python.org](https://www.python.org/downloads/).
   - Make sure Python is added to your system’s PATH.

2. **Download the Game Code:**
   - Clone or download this repository.
   - Or, copy the provided code into a Python file (e.g., `rock_paper_scissors.py`).


## Running the Game

1. Navigate to the directory containing the Python script (`rock_paper_scissors.py`).
2. Run the script with the following command:

```bash
python rock_paper_scissors.py
```

3. Follow the on-screen prompts to play the game.

## Game Rules

- **Rock** beats **Scissors**.
- **Scissors** beats **Paper**.
- **Paper** beats **Rock**.
- If both the player and the computer choose the same option, it's a tie or draw.



## Example Output

```bash
________________________________________________________
===================| Rock-Paper-Scissor |===================
----------------------------GAME----------------------------
Please Enter Your Choice:
Choice 1: Rock
Choice 2: Paper
Choice 3: Scissors

Select any option from 1 to 3 :-> 1
____________________________________________________________

[ Chooced by Machine : Rock ] [ Chooced by You : Rock ]
+--------------------( Ohh No, it's tie! )--------------------+

			~POINTES~
		[Machine : 0 | You : 0]
____________________________________________________________

Do you want to play again? (Yes/No) :-> y
____________________________________________________________
===================| Rock-Paper-Scissor |===================
----------------------------GAME----------------------------
Please Enter Your Choice:
Choice 1: Rock
Choice 2: Paper
Choice 3: Scissors

Select any option from 1 to 3 :-> 2
____________________________________________________________

[ Chooced by Machine : Paper ] [ Chooced by You : Paper ]
+--------------------( Ohh No, it's tie! )--------------------+

			~POINTES~
		[Machine : 0 | You : 0]
____________________________________________________________

Do you want to play again? (Yes/No) :-> n
____________________________________________________________

 --------------: Thanks for playing the game! :--------------

			Final Score
		Machine Score		[ 0 ]
		Your Score		[ 0 ]

Ohh No! Match is TIE...
____________________________________________________________

```

## License

This project is licensed under the [MIT License](./LICENSE).
