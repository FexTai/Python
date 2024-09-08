import openai

# Setze deinen OpenAI API-Schlüssel hier ein
api_key = "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"

# Konfiguriere das OpenAI-Paket mit deinem API-Schlüssel
openai.api_key = api_key

# Beispieltext für die Anfrage an das Modell
input_text = "bist du genauso gut wie chatgpt?"

# Rufe die OpenAI API auf, um eine Antwort vom GPT-3.5 Turbo-Modell zu erhalten
response = openai.Completion.create(
  engine="gpt-3.5-turbo-16k",  # GPT-3.5 Turbo-Modell verwenden
  prompt=input_text,
  max_tokens=150  # Maximale Anzahl von Tokens in der Antwort
)

# Extrahiere und drucke die generierte Antwort
generated_text = response["choices"][0]["text"]
print("Generierte Antwort:", generated_text)