def main():
    # Ask the user for the current quarter
    quarter = int(input("Which quarter is the basketball game in? "))

    # Ask the user for the time remaining in mm:ss format
    time_remaining_input = input("Enter the time remaining in mm:ss format: ")
    minutes, seconds = map(int, time_remaining_input.split(":"))

    # Calculate the total time remaining in the game
    total_time_remaining = ((4 - quarter) * 20 * 60) + (minutes * 60) + seconds

    # Ask the user for the number of points scored by each team
    points_team_a = int(input("How many points has Team A scored? "))
    points_team_b = int(input("How many points has Team B scored? "))

    # Calculate the elapsed time in the game
    if quarter < 4:
        elapsed_time = (quarter * 20 * 60) - (minutes * 60 + seconds)
    else:
        elapsed_time = 60 * 4 * 60  # Total time of the game in seconds

    # Calculate points per second for each team
    points_per_second_team_a = points_team_a / elapsed_time
    points_per_second_team_b = points_team_b / elapsed_time

    # Predict the additional points each team will score in the remaining time
    predicted_points_team_a = points_team_a + (points_per_second_team_a * total_time_remaining)
    predicted_points_team_b = points_team_b + (points_per_second_team_b * total_time_remaining)

    # Adjust the predicted total score based on relative team strengths
    score_difference = predicted_points_team_a - predicted_points_team_b
    if score_difference > 0:
        predicted_points_team_b += score_difference
    elif score_difference < 0:
        predicted_points_team_a -= score_difference

    predicted_total_points = predicted_points_team_a + predicted_points_team_b

    print("Predicted total points for Team A: {:.2f}".format(predicted_points_team_a))
    print("Predicted total points for Team B: {:.2f}".format(predicted_points_team_b))
    print("Predicted total score of the game: {:.2f}".format(predicted_total_points))


if __name__ == "__main__":
    main()
