import json

FILE_NAME = "data.json"


# Load old data
def load_data():

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data

    except:
        return []


# Save data
def save_data(history):

    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


# Store interview question and answer
def store_interview(question, answer, topic, evaluation):

    history = load_data()

    interview_data = {
        "question": question,
        "answer": answer,
        "topic": topic,
        "evaluation": evaluation
    }

    history.append(interview_data)

    save_data(history)


# Build smart context
def build_context():

    history = load_data()

    # Keep only last 2 records
    recent_history = history[-2:]

    previous_questions = []
    previous_answers = []

    strong_topics = []
    weak_topics = []

    # Store recent questions and answers
    for item in recent_history:

        previous_questions.append(item["question"])
        previous_answers.append(item["answer"])

    # Build evaluation summary
    for item in history:

        if item["evaluation"] == "Good":

            if item["topic"] not in strong_topics:
                strong_topics.append(item["topic"])

        else:

            if item["topic"] not in weak_topics:
                weak_topics.append(item["topic"])

    # Final context
    context = {

        "previous_questions": previous_questions,

        "previous_answers": previous_answers,

        "evaluation_summary": {

            "strong_topics": strong_topics,
            "weak_topics": weak_topics
        },

        "current_state": "Interview Running"
    }

    return context