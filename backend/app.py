from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # we do this to enable CORS filter for all the routes

# here we are creating a list of affirmations which will be replaced using a db at a later point
affirmations = [
    "I speak fluent Python, JavaScript, and sarcasm.",
    "Bugs fear me—I'm their worst nightmare.",
    "I can write code that compiles on the first try.",
    "My code is so clean that even my boss can understand it.",
    "I don't always test my code, but when I do, I do it in production.",
    "I'm a keyboard ninja—I code at the speed of thought.",
    "I comment my code so well that even future me understands it.",
    "I'm not lazy, I'm just on 'efficient energy saving mode.'",
    "I don't need Stack Overflow; Stack Overflow needs me.",
    "My coding style is like a fine wine—it gets better with age (and lots of refactoring).",
    "I am constantly learning and growing in my coding skills.",
    "I am capable of solving complex problems.",
    "Every bug is an opportunity to improve and understand the code better.",
    "I write clean, efficient, and maintainable code.",
    "I am a valuable member of my development team.",
    "I embrace challenges and learn from my mistakes.",
    "I am patient and persistent in debugging and problem-solving.",
    "My work makes a positive impact on users and clients.",
    "I am open to feedback and use it to enhance my skills.",
    "I balance productivity with self-care and mental well-being.",
    "I am a creative and innovative developer.",
    "I can adapt to new technologies and frameworks.",
    "I collaborate effectively with my peers.",
    "I trust my intuition and expertise in coding.",
    "I am confident in my ability to learn and master new programming languages.",
    "I contribute to a positive and supportive work environment.",
    "I am proud of the projects I complete.",
    "I stay focused and motivated, even during challenging tasks.",
    "I continually strive to improve my development processes.",
    "I celebrate my achievements and acknowledge my progress."
]


@app.route('/random-affirmation', methods=['GET'])
def get_random_affirmation():
    affirmation = random.choice(affirmations)
    return jsonify({'affirmation': affirmation})


if __name__ == '__main__':
    app.run(debug=True)