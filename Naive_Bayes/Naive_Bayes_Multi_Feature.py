weather=['R','R','O','S','S','S','O','R','R','S','R','O','O','S']
temperature=['H','H','H','M','C','C','C','M','C','M','M','M','H','M']
windy=['F','T','F','F','F','T','T','F','F','F','T','T','F','T']
play_golf=['N','N','Y','Y','Y','N','Y','N','Y','Y','Y','Y','Y','N']
n = len(play_golf)
yes_tot = play_golf.count('Y')
no_tot = play_golf.count('N')

# Function to calculate probabilities for a given feature
def calculate_probabilities(feature, play_golf):
    yes_count, no_count = {}, {}
    for i in range(n):
        if play_golf[i] == 'Y':
            yes_count[feature[i]] = yes_count.get(feature[i], 0) + 1
        else:
            no_count[feature[i]] = no_count.get(feature[i], 0) + 1

    # Normalize by the total yes/no counts
    yes_prob = {k: v/yes_tot for k, v in yes_count.items()}
    no_prob = {k: v/no_tot for k, v in no_count.items()}

    return yes_prob, no_prob

# Calculate probabilities for each feature
Pweather_yes, Pweather_no = calculate_probabilities(weather, play_golf)
Ptemperature_yes, Ptemperature_no = calculate_probabilities(temperature, play_golf)
Pwindy_yes, Pwindy_no = calculate_probabilities(windy, play_golf)

# Output results
print(f"Weather probabilities given 'yes': {Pweather_yes}")
print(f"Weather probabilities given 'no': {Pweather_no}")

print(f"Temperature probabilities given 'yes': {Ptemperature_yes}")
print(f"Temperature probabilities given 'no': {Ptemperature_no}")

print(f"Windy probabilities given 'yes': {Pwindy_yes}")
print(f"Windy probabilities given 'no': {Pwindy_no}")
Pyes_cond=(yes_tot/n)*Pweather_yes['S']*Ptemperature_yes['H']*Pwindy_yes['F']
Pno_cond=(no_tot/n)*Pweather_no['S']*Ptemperature_no['H']*Pwindy_no['F']
print(Pyes_cond)
print(Pno_cond)
