# N - number of workers
# B - number of bears
def find_min_beers(N, B, statistics):
    statistics = statistics.split()
    types_of_beer = 0
    beers_set = []

    for i in range(N):
        temp_set = []

        for j in range(B):
            if statistics[i][j] == "Y":
                temp_set.append(j)

        if temp_set and all(item not in beers_set for item in temp_set):  # Додаємо перевірку на непорожній список
            beers_set.extend(temp_set)
            types_of_beer += 1

    return types_of_beer