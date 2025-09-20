# pig-game
🎲 Dice Game (Multiplayer Turn-Based Game)

This is a simple multiplayer dice game built with Python. Players take turns rolling a die to accumulate points. The first player to reach 50 points wins the game.

📜 Game Rules

The game supports 2 to 4 players.

Each player takes turns rolling a die.

If the player rolls a 1, their turn ends and they lose all points accumulated during that turn.

If the player rolls between 2 and 6, the value is added to their turn score.

After each roll, the player can decide whether to:

Roll again (y)

Hold and keep the current turn score

The first player to reach 50 total points wins the game.
- Code Structure

roll(): Rolls a die (between 1 and 6).

Player input validation: Ensures the number of players is between 2 and 4.

Main game loop:

Iterates through each player

Allows them to roll or hold

Keeps track of scores

Ends when a player's score reaches 50.

📌 Features

Input validation for number of players

Clean UI with player prompts

Basic terminal-based game logic

Auto winner detection
