from flask import Flask, render_template, request, send_from_directory
from DIAMind.search import load_embeddings, semantic_search
from DIAMind.answer_generator import generate_answer
import os
import re
import markdown

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "Data", "Cleaned")

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(DATA_DIR, filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    answer = ""
    user_query = ""
    if request.method == 'POST':
        user_query = request.form.get('query', '')
        embeddings, filenames, texts = load_embeddings(os.path.join(os.path.dirname(__file__), "DIAMind/data_embeddings.npz"))
        results = semantic_search(
            user_query,
            embeddings,
            filenames,
            texts,
            top_k=5
        )
        answer = generate_answer(user_query, results)
        # PULISCI E CONVERTI I TESTI DEI RISULTATI IN HTML
        for r in results:
            html = markdown.markdown(clean_math_expressions(r['text']))
            r['text'] = fix_image_paths(html)
        # CONVERTI ANCHE LA RISPOSTA GENERATA
        answer = fix_image_paths(markdown.markdown(clean_math_expressions(answer)))
    return render_template('frontend.html', results=results, answer=answer, user_query=user_query)

def clean_math_expressions(text):
    replacements = {
        r"\Sigma": "Alfabeto di simboli",
        r"\underline{b}": "Spazio bianco",
        r"\delta": "Funzione di transizione",
        r"\delta^{(k)}": "Funzione di transizione per k nastri",
        r"\vdash": "produce",
        r"\to": "→",
        r"\cup": "unione",
        r"\left\{": "{",
        r"\right\}": "}",
        r"\times": "×",
        # aggiungi altre sostituzioni se necessario
    }
    for latex, plain in replacements.items():
        text = text.replace(latex, plain)
    # Rimuovi eventuali altri simboli LaTeX
    text = text.replace("$", "")
    text = text.replace("\\", "")
    return text

def fix_image_paths(html):
    # Sostituisce src="nome.png" con src="/images/nome.png"
    return re.sub(r'src="([^"]+\.png)"', r'src="/images/\1"', html)

if __name__ == '__main__':
    app.run(debug=True)
