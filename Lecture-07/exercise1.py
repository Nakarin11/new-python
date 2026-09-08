# Survey results (each list represents a participant's choices)
survey_results = [
    ["Python", "JavaScript", "C++"], # Participant 1
    ["Python", "JavaScript", "C#"], # Participant 2
    ["Python", "Java"], # Participant 3
    ["Python", "C++", "JavaScript"], # Participant 4
    ["Python", "JavaScript", "C++", "Java"], # Participant 5
]

# 1. Identify the languages that were chosen by all participants.
all_languages = [set(participant) for participant in survey_results]
common_languages = set.intersection(*all_languages)
print("1. Languages chosen by all participants:", common_languages)  # Output: {'Python'}

# 2. Find the languages that were chosen by a single participant.
# 3. Determine the number of unique languages mentioned in the survey.
# 4. List the languages that were chosen by exactly two participants.
# 5. Find participants who have the exact same set of favorite languages.