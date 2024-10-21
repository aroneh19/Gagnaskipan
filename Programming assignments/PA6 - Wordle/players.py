import json

class Player:
    def __init__(self, username):
        """Initializes a Player instance with the provided username.

        Args:
            username (str): The username of the player.
        """
        self.username = username
        self.stats = {
            'wins': 0,
            'losses': 0,
            'total_score': 0,
            'high_score': 0,
            'game_history': []
        }
    
    def update_stats(self, game_result):
        """Updates the player's statistics based on the result of a game.

        Args:
            game_result (int): The score obtained in the game.
        """
        self.stats['game_history'].append(game_result)
        self.stats['total_score'] = sum(self.stats['game_history'])
        if self.stats['total_score']:
            self.stats['high_score'] = max(self.stats['game_history'])
    
    def save_profile(self):
        """Saves the player's profile to a JSON file.

        The player's statistics are stored under their username in the JSON file.
        If the player already exists, their statistics are updated; otherwise, a new entry is created.
        """
        with open("players.json", "r") as file:
            data = json.load(file)

        player_found = False
        for player_data in data:
            if self.username in player_data:
                player_data[self.username] = self.stats
                player_found = True
                break

        if not player_found:
            data.append({self.username: self.stats})

        with open("players.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_profile(self):
        """Loads the player's profile from a JSON file.

        If the player exists in the file, their statistics are loaded into the player instance.
        """
        with open("players.json", "r") as file:
            data = json.load(file)
            for player_data in data:
                if self.username in player_data:
                    self.stats = player_data[self.username]
                    break
    
    def display_player(self):
        """Displays all information about the player."""

        print(f"Username: {self.username}")
        print("Statistics:")
        for key, value in self.stats.items():
            if key != 'game_history':
                print(f"{key.capitalize()}: {value}")
        print("Game History:")
        for game in self.stats['game_history']:
            print(f"  - Score: {game}")
            