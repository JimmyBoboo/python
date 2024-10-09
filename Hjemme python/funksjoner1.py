def count_game(game_to_count, game_list):
    count = 0
    for game in game_list:
        if game.lower() == game_to_count.lower():
            count += 1
    print(f"{game_to_count.title()} count: {count}")

print("-----Original Favorite Game Survey-----")
favorite_game_survey = ["Dark Souls", "Metal Gear Solid 3", "Portal 2", "Resident Evil 4", "Bloodborne", 
                          "Bloodborne", "Dark Souls", "Fornite", "Portal 2", "Bloodborne"]

count_game("Dark Souls", favorite_game_survey)
count_game("Bloodborne", favorite_game_survey)

print()
print("-----Another Favorite Game Survey-----")
another_favorite_game_survey = ["Fortnite", "The Witcher 3", "Fortnite", "Silent Hill 2", "The Witcher 3", "The Witcher 3"]

count_game("Dark Souls", another_favorite_game_survey)