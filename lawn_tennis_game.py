class LawnTennis:
    def __init__(self, golden_point):
        self.scores = {'Player A': 0, 'Player B': 0}
        self.sets = {'Player A': 0, 'Player B': 0}
        self.current_set_winner = None
        self.golden_point = golden_point

    def print_scores(self):
        point_names = [0, 15, 30, 40]

        def get_point_name(score):
            return point_names[score] if score < 4 else "Game"

        print(
            f"Current Scores: Player A - {get_point_name(self.scores['Player A'])}, Player B - {get_point_name(self.scores['Player B'])}")

    def check_set_winner(self):
        if (self.scores['Player A'] >= 4 and
                self.scores['Player A'] - self.scores['Player B'] >= 2):
            self.sets['Player A'] += 1
            self.current_set_winner = 'Player A'
            return True
        elif (self.scores['Player B'] >= 4 and
              self.scores['Player B'] - self.scores['Player A'] >= 2):
            self.sets['Player B'] += 1
            self.current_set_winner = 'Player B'
            return True
        return False

    def play(self):
        while True:
            print("\n-----------------------------------")
            print("| Scoring Options for Lawn Tennis |")
            print("-----------------------------------")
            print("| 1. Player A scores a point      |")
            print("| 2. Player B scores a point      |")
            print("-----------------------------------")

            choice = input("Select scoring option by index: ").strip()

            if choice == '1':
                self.scores['Player A'] += 1
            elif choice == '2':
                self.scores['Player B'] += 1
            else:
                print("Invalid choice. Please select 1 or 2.")
                continue

            self.print_scores()

            if self.check_set_winner():
                print(f"\n{self.current_set_winner} wins the set!")
                self.scores = {'Player A': 0, 'Player B': 0}
                if input("Should we proceed with another set? (yes/no): ").strip().lower() != 'yes':
                    break

        print("Game Over!")
        print(f"Final Score: Player A - {self.sets['Player A']} sets, Player B - {self.sets['Player B']} sets")
