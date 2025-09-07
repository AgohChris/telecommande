from flask import Flask
import pyautogui
import os


app = Flask(__name__)

@app.route("/next")
def next_slide():
    pyautogui.press("right")   # Flèche droite = slide suivante
    return "Slide suivante"

@app.route("/prev")
def prev_slide():
    pyautogui.press("left")    # Flèche gauche = slide précédente
    return "Slide précédente"

@app.route("/play")
def play():
    pyautogui.press("f5")      # F5 = démarrer diaporama
    return "Diaporama lancé"

@app.route("/stop")
def stop():
    pyautogui.press("esc")     # Esc = quitter diaporama
    return "Diaporama arrêté"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)