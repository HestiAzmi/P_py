from flask import Flask, render_template, request, redirect, url_for  # Mengimpor modul Flask dan fungsi terkait

app = Flask(__name__)  # Membuat instance dari aplikasi Flask

# Data pertanyaan dan jawaban kuis
questions = [
    {"question": "Apa ibu kota Indonesia?", "options": ["Jakarta", "Surabaya", "Bandung", "Medan"], "answer": "Jakarta"},  # Pertanyaan 1
    {"question": "Berapa hasil dari 5 + 3?", "options": ["5", "8", "10", "15"], "answer": "8"},  # Pertanyaan 2
    {"question": "Siapakah penemu bola lampu?", "options": ["Albert Einstein", "Thomas Edison", "Nikola Tesla", "Isaac Newton"], "answer": "Thomas Edison"},  # Pertanyaan 3
    {"question": "Planet terbesar di tata surya adalah?", "options": ["Mars", "Jupiter", "Bumi", "Venus"], "answer": "Jupiter"},  # Pertanyaan 4
    {"question": "Presiden Indonesia Pertama adalah Bapak?", "options": ["B.J Habibie", "Soekarno Hatta", "Jokowi", "Prabowo"], "answer": "Soekarno Hatta"},  # Pertanyaan 5
]

# Route utama untuk halaman kuis, mendukung metode GET dan POST
@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":  # Jika metode request adalah POST (form telah dikirim)
        score = 0  # Inisialisasi skor dengan nilai 0
        answers = []  # List untuk menyimpan jawaban yang dipilih oleh pengguna
        
        # Loop untuk memeriksa setiap jawaban dari pengguna
        for i, q in enumerate(questions):  # Mengiterasi setiap pertanyaan dengan indeksnya
            selected_option = request.form.get(f"q{i}")  # Mengambil jawaban yang dipilih dari form berdasarkan indeks pertanyaan
            
            # Jika jawaban yang dipilih sesuai dengan jawaban benar
            if selected_option == q["answer"]:
                score += 1  # Tambahkan skor jika jawaban benar
                answers.append({'question': q['question'], 'selected': selected_option, 'correct': True})  # Simpan jawaban benar ke list `answers`
            else:
                answers.append({'question': q['question'], 'selected': selected_option, 'correct': False, 'correct_answer': q['answer']})  # Simpan jawaban salah dan jawaban yang benar ke list `answers`
        
        # Render template `index.html` dengan skor, total pertanyaan, dan detail jawaban
        return render_template("index.html", questions=questions, score=score, total=len(questions), answers=answers, enumerate=enumerate)

    # Jika metode request adalah GET, tampilkan halaman kuis tanpa skor dan jawaban
    return render_template("index.html", questions=questions, score=None, total=len(questions), answers=None, enumerate=enumerate)

# Menjalankan aplikasi Flask jika file ini dijalankan secara langsung
if __name__ == "__main__":
    app.run(debug=True)  # Menjalankan server Flask dengan mode debug aktif
