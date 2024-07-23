from admin import Admin
from badminton_game import BadmintonGame
from table_tennis_game import TableTennis
from lawn_tennis_game import LawnTennis

def main():
    # Admin login and configuration
    admin = Admin()
    admin_role = admin.authenticate_user('admin')

    if not admin_role:
        print("Admin authentication failed.")
        return

    # Admin configures the game settings
    game, points_to_win, golden_point = admin.admin_menu()

    if not game:
        print("Exiting the dashboard.")
        return

    # Scorer login
    scorer = Admin()  # Reusing Admin class for scorer login
    scorer_role = scorer.authenticate_user('scorer')

    if not scorer_role:
        print("Authentication failed. Only the scorer can start the match.")
        return

    # Ensure the logged-in user is a scorer before starting the game
    if scorer_role != 'scorer':
        print("Only the scorer can start the match.")
        return

    # Create and start the game instance
    if game == 'badminton':
        game_instance = BadmintonGame(points_to_win, golden_point)
    elif game == 'table_tennis':
        game_instance = TableTennis(points_to_win, golden_point)
    elif game == 'lawn_tennis':
        game_instance = LawnTennis(golden_point)
    else:
        print("Invalid game selected.")
        return

    if game_instance:
        game_instance.play()



if __name__ == "__main__":
    main()
