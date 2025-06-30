# Match The Cards Game: Online!

Welcome to **Match The Cards**, a fun and challenging card-matching game where you need to find pairs of matching cards in the shortest time possible! Designed and developed by **Shayyan Husein**.

## ⚠️ Important Notice

The DynamoDB database used for storing leaderboard scores is currently restricted with certain permissions and is a work in progress to be made public. Please be aware that the leaderboard functionality may not be fully accessible at this time.

![Menu Background](img/menu-full.jpg)
Welcome to **Match The Cards**, a fun and challenging card-matching game where you must find pairs of matching cards in the shortest time possible! 

## 🛠️ Game Features

- **Card Matching**: Flip cards to find matching pairs from 4 suits: Diamonds, Hearts, Spades, and Clubs.
- **Timer**: Track how long it takes to match all pairs. Your final time will be saved to the leaderboard.
- **Leaderboard**: Compete against others and see how fast you can complete the game. The top 3 fastest times are displayed.
- **Sound and Visual Effects**: Enjoy smooth animations and card flip effects with custom background music.

## 🚀 How to Play
![Picture of How to Play](img/howto.png)
1. **Start the Game**: Click **START** to begin.
2. **Flip Cards**: Click on any card to flip it. Try to find matching pairs. The game will check the two cards for a match.
3. **Match Cards**: If the cards match, they'll disappear. If they don't, they’ll flip back over.
4. **Complete the Game**: Match all cards to win. Your time will be displayed and saved in the leaderboard.
5. **Restart or Exit**: After finishing, you can restart the game or exit.


## 📊 Leaderboard
- After completing the game, your time will be added to the **Leaderboard**.
- The top 3 players' times will be displayed, and your rank will be updated if you make it to the top 3.
- **Username**: You’ll be prompted to enter a username at the beginning of the game.

### 🗃 AWS DynamoDB

The leaderboard scores are stored in an AWS DynamoDB database. Below is an example of the DynamoDB table with items in it:

![AWS DynamoDB Table](img/aws_full.jpg)

### 🏆 In-Game Leaderboard

The in-game leaderboard displays the top 3 fastest times. Below is an example of the populated leaderboard from the Pygame window:

![In-Game Leaderboard](img/leaderboard-full.jpg)

## 🖥️ Requirements

- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **Pygame**: This game uses Pygame for graphics and event handling. You can install it using:

    ```bash
    pip install pygame
    ```
