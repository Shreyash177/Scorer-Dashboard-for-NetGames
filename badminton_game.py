class BadmintonGame:
    def __init__(self, points_to_win, golden_point):
        self.points_to_win = points_to_win
        self.golden_point = golden_point
        self.scores = {'Player A': 0, 'Player B': 0}

    def show_badminton_scoring_options(self):
        """Display the scoring options for badminton."""
        print("\n-----------------------------------")
        print("|  Scoring Options for Badminton  |")
        print("-----------------------------------")
        print("| 1. Player A scores a point      |")
        print("| 2. Player B scores a point      |")
        print("-----------------------------------")
        choice = input("Select scoring option by index: ")
        return choice

    def check_winner(self):
        """Check if there's a winner based on the current score and rules."""
        if self.golden_point and (
                self.scores['Player A'] == self.golden_point or self.scores['Player B'] == self.golden_point):
            if self.scores['Player A'] == self.golden_point:
                return 'Player A'
            elif self.scores['Player B'] == self.golden_point:
                return 'Player B'

        if max(self.scores.values()) >= self.points_to_win and abs(
                self.scores['Player A'] - self.scores['Player B']) >= 2:
            if self.scores['Player A'] > self.scores['Player B']:
                return 'Player A'
            else:
                return 'Player B'

        return None

    def play(self):
        """Run the badminton game with the specified scoring rules."""
        while True:
            scoring_choice = self.show_badminton_scoring_options()

            if scoring_choice == '1':
                self.scores['Player A'] += 1
                print("\n----------------------------------")
                print("Player A scores a point!")
                print("----------------------------------")
            elif scoring_choice == '2':
                self.scores['Player B'] += 1
                print("\n----------------------------------")
                print("Player B scores a point!")
                print("----------------------------------")
            else:
                print("\n----------------------------------")
                print("Invalid choice. Please try again.")
                print("----------------------------------")
                continue

            print(f"\nCurrent Scores: Player A - {self.scores['Player A']}, Player B - {self.scores['Player B']}")

            winner = self.check_winner()
            if winner:
                print(f"\n----------------------------------")
                print(f"{winner} wins the game!")
                print("----------------------------------")
                break

        another_set = input("Should we proceed with another set? (yes/no): ").strip().lower()
        if another_set == 'yes':
            self.play()
