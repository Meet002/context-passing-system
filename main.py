from memory import store_interview, build_context
import json


print("\n===== AI Interview Memory System =====\n")


questions = [

    {
        "question": "What is Python?",
        "topic": "Python"
    },

    {
        "question": "Explain OOP concepts.",
        "topic": "OOP"
    },

    {
        "question": "What is Bubble Sort?",
        "topic": "DSA"
    }

]


# Interview starts
for item in questions:

    question = item["question"]
    topic = item["topic"]

    print("\nQuestion:")
    print(question)

    answer = input("\nYour Answer: ")

    answer_lower = answer.lower()

    evaluation = "Average"

    # Python Evaluation
    if topic == "Python":

        python_keywords = [
            "language",
            "programming",
            "easy",
            "syntax"
        ]

        for word in python_keywords:

            if word in answer_lower:
                evaluation = "Good"

    # OOP Evaluation
    elif topic == "OOP":

        oop_keywords = [
            "class",
            "object",
            "inheritance",
            "polymorphism"
        ]

        for word in oop_keywords:

            if word in answer_lower:
                evaluation = "Good"

    # DSA Evaluation
    elif topic == "DSA":

        dsa_keywords = [
            "sorting",
            "algorithm",
            "array",
            "swap"
        ]

        for word in dsa_keywords:

            if word in answer_lower:
                evaluation = "Good"

    # Store interview data
    store_interview(
        question,
        answer,
        topic,
        evaluation
    )

    print("\nEvaluation:", evaluation)


# Generate final context
final_context = build_context()


print("\n===== Final Context Sent To LLM =====\n")

print(json.dumps(final_context, indent=4))