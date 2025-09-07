from flask import Flask
import os
import platform

app = Flask(__name__)

# --- Helpers pour envoyer les touches ---
def press_key(key):
    system = platform.system()
    if system == "Darwin":  # macOS
        keycodes = {
            "right": 124,   # Flèche droite
            "left": 123,    # Flèche gauche
            "f5": 96,       # F5
            "esc": 53       # Escape
        }
        if key in keycodes:
            os.system(f'''osascript -e 'tell application "System Events" to key code {keycodes[key]}' ''')
    else:  # Windows/Linux → pyautogui
        import pyautogui
        pyautogui.press(key)


@app.route("/next")
def next_slide():
    press_key("right")
    return "➡️ Slide suivante"


@app.route("/prev")
def prev_slide():
    press_key("left")
    return "⬅️ Slide précédente"


@app.route("/play")
def play():
    press_key("f5")
    return "▶️ Diaporama lancé"


@app.route("/stop")
def stop():
    press_key("esc")
    return "⏹️ Diaporama arrêté"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
