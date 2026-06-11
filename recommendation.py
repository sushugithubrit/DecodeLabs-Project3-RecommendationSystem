print("=" * 50)
print("AI COURSE RECOMMENDATION ENGINE")
print("=" * 50)

courses = {
    "Machine Learning": ["python", "ai"],
    "Deep Learning": ["ai"],
    "Data Science": ["python"],
    "Computer Vision": ["ai"],
    "Natural Language Processing": ["python", "ai"],
    "HTML & CSS": ["web development"],
    "JavaScript": ["web development"],
    "React": ["web development"],
    "Cyber Security Basics": ["cyber security"],
    "Ethical Hacking": ["cyber security"]
}

available_interests = [
    "python",
    "ai",
    "web development",
    "cyber security"
]

print("\nAvailable Interests:")
for interest in available_interests:
    print(f"• {interest}")

user_input = input(
    "\nEnter your interests (comma separated): "
).lower().strip()

user_interests = [
    interest.strip()
    for interest in user_input.split(",")
]

recommendations = []

for course, tags in courses.items():

    matched_tags = len(
        set(user_interests).intersection(tags)
    )

    if matched_tags > 0:

        score = (
            matched_tags / len(tags)
        ) * 100

        recommendations.append(
            (course, score, tags)
        )

recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nUser Profile:")
print(user_interests)

print("\nTop Recommendations:\n")

if recommendations:

    for index, (course, score, tags) in enumerate(
        recommendations,
        start=1
    ):

        matched = set(user_interests).intersection(tags)

        print(f"{index}. {course}")
        print(f"   Match Score: {score:.0f}%")
        print(f"   Reason: Matches {', '.join(matched)}")
        print()

else:
    print("No recommendations found.")