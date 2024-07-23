class TableTennis:
    def __init__(self, points_to_win, golden_point):
        self.points_to_win = points_to_win
        self.golden_point = golden_point
        self.scores = {'Player A': 0, 'Player B': 0}

    def show_scoring_options(self):
        """Display the scoring options for Table Tennis."""
        print("\n------------------------------------")
        print("| Scoring Options for Table Tennis |")
        print("------------------------------------")
        print("| 1. Player A scores a point       |")
        print("| 2. Player B scores a point       |")
        print("------------------------------------")
        choice = input("Select scoring option by index: ")
        return choice

    def check_winner(self):
        """Check if there's a winner based on the current score and rules."""
        if self.scores['Player A'] >= self.points_to_win and \
           self.scores['Player A'] - self.scores['Player B'] >= 2:
            return 'Player A'
        if self.scores['Player B'] >= self.points_to_win and \
           self.scores['Player B'] - self.scores['Player A'] >= 2:
            return 'Player B'
        return None

    def play(self):
        """Run the Table Tennis game with the specified scoring rules."""
        while True:
            scoring_choice = self.show_scoring_options()

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
                print("\n----------------------------------")
                print(f"{winner} wins the game!")
                print("----------------------------------")
                break

            # Implement Golden Point if applicable
            if self.golden_point and (self.scores['Player A'] >= self.golden_point or
                                      self.scores['Player B'] >= self.golden_point):
                if abs(self.scores['Player A'] - self.scores['Player B']) >= 2:
                    winner = self.check_winner()
                    if winner:
                        print("\n----------------------------------")
                        print(f"{winner} wins with the Golden Point!")
                        print("----------------------------------")
                        break

        another_game = input("Should we proceed with another set? (yes/no): ").strip().lower()
        if another_game == 'yes':
            self.__init__(self.points_to_win, self.golden_point)
            self.play()
