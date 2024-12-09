from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data pertanyaan dan jawaban kuis
questions = [
    {"question": "Apa ibu kota Indonesia?", "options": ["Jakarta", "Surabaya", "Bandung", "Medan"], "answer": "Jakarta"},
    {"question": "Berapa hasil dari 5 + 3?", "options": ["5", "8", "10", "15"], "answer": "8"},
    {"question": "Siapakah penemu bola lampu?", "options": ["Albert Einstein", "Thomas Edison", "Nikola Tesla", "Isaac Newton"], "answer": "Thomas Edison"},
    {"question": "Planet terbesar di tata surya adalah?", "options": ["Mars", "Jupiter", "Bumi", "Venus"], "answer": "Jupiter"},
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        answers = []
        for i, q in enumerate(questions):
            selected_option = request.form.get(f"q{i}")
            if selected_option == q["answer"]:
                score += 1
                answers.append({'question': q['question'], 'selected': selected_option, 'correct': True})
            else:
                answers.append({'question': q['question'], 'selected': selected_option, 'correct': False, 'correct_answer': q['answer']})
                
        return render_template("index.html", questions=questions, score=score, total=len(questions), answers=answers, enumerate=enumerate)

    return render_template("index.html", questions=questions, score=None, total=len(questions), answers=None, enumerate=enumerate)

if __name__ == "__main__":
    app.run(debug=True)
