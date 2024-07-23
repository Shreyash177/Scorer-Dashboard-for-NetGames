import json

class Admin:
    def __init__(self):
        self.data = self.load_game_data()

    def load_game_data(self):
        """Load game data from a JSON file."""
        try:
            with open('game_data.json', 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Error loading JSON data: {e}")
            raise
        except FileNotFoundError:
            print("Error: game_data.json file not found.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def save_game_data(self, data):
        """Save game data to a JSON file."""
        try:
            with open('game_data.json', 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            raise

    def authenticate_user(self, role_required):
        """Authenticate a user based on username and password."""
        while True:
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            for user in self.data.get('users', []):
                if (user['username'] == username and
                        user['password'] == password and
                        user['role'] == role_required):
                    print("\nAuthentication successful!\n")
                    return username

            print("\nAuthentication failed. Please try again.\n")

    def show_menu(self):
        """Display the main menu for game selection."""
        print("\n----------------------------------")
        print("|       Scorer Dashboard         |")
        print("----------------------------------")
        print("| 1. Badminton                   |")
        print("| 2. Table Tennis                |")
        print("| 3. Lawn Tennis                 |")
        print("| 4. Exit                        |")
        print("----------------------------------")
        choice = input("Select a game by index: ")
        return choice

    def display_game_settings(self, game):
        """Display the settings for the selected game."""
        settings = self.data['games'].get(game, {})
        points_to_win = settings.get('default_points_to_win')
        golden_point = settings.get('golden_point')

        print(f"Current settings for {game.capitalize()}:")
        if points_to_win:
            print(f"Points to win: {points_to_win}")
        else:
            print("Points to win: Not applicable")
        if golden_point:
            print(f"Golden Point: {golden_point}")
        else:
            print("Golden Point: Not applicable")

    def admin_menu(self):
        """Display the admin menu for game selection."""
        while True:
            game_choice = self.show_menu()
            if game_choice == '1':
                game = 'badminton'
            elif game_choice == '2':
                game = 'table_tennis'
            elif game_choice == '3':
                game = 'lawn_tennis'
            elif game_choice == '4':
                print("Exiting the dashboard.")
                return None, None, None
            else:
                print("\n----------------------------------")
                print("Invalid choice. Please try again.")
                print("----------------------------------")
                continue

            self.display_game_settings(game)
            points_to_win = self.data['games'][game].get('default_points_to_win') if game in ['badminton', 'table_tennis'] else None
            golden_point = self.data['games'][game].get('golden_point')
            return game, points_to_win, golden_point
