from transformers import pipeline
import requests
import os

generator = pipeline("text2text-generation", model="google/flan-t5-base", device=-1)

OPENROUTER_API_KEY = "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"

def generate_answer(query, results, max_length=256, context_max_chars=1200, max_doc_chars=400, first_doc_max_chars=1200):
    # Prendi solo i primi 3 documenti
    selected_results = results[:3]
    context = ""
    for idx, r in enumerate(selected_results):
        if idx == 0:
            doc_text = r["text"][:first_doc_max_chars]  # Primo documento: limite maggiore
        else:
            doc_text = r["text"][:max_doc_chars]        # Altri documenti: limite normale
        if len(context) + len(doc_text) < context_max_chars:
            context += doc_text + "\n"
        else:
            context += doc_text[:context_max_chars - len(context)]
            break
    prompt = (
        "Rispondi in linguaggio naturale alla domanda seguente. "
        "Se trovi la risposta nei documenti forniti, usali come fonte principale. "
        "Se la risposta non è presente nei documenti, fornisci comunque una risposta basata sulle tue conoscenze.\n\n"
        f"Domanda: {query}\n\nDocumenti:\n{context}\n\nRisposta:"
    )
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_length
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"].strip()
        else:
            answer = f"Errore nella generazione della risposta. Codice: {response.status_code}\n{response.text}"
    except Exception as e:
        answer = f"Errore nella generazione della risposta: {str(e)}"
    print("Risposta generata:", repr(answer))
    return answer