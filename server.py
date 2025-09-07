from flask import Flask
import pyautogui

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
    # On écoute sur toutes les interfaces (0.0.0.0)
    app.run(host="0.0.0.0", port=5000)
