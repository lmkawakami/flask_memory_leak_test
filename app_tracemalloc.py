import gc
from flask import Flask, jsonify
import random
import tracemalloc

tracemalloc.start()
s=None

LEAK = {}
app = Flask(__name__)

@app.route('/random')
def random_number():
    global LEAK
    number = random.randint(1, 1_000_000_000)
    LEAK[number] = f"Lorem Ipsum {number} is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    gc.collect()
    return jsonify({'random_number': number})

@app.route("/snapshot")
def snap():
    NUMBER_OF_TOP_LEAKS_TO_SHOW = 10
    APP_FOLDER = "flask_memory_leak_test"
    global s
    if not s:
        s = tracemalloc.take_snapshot()
        return "taken snapshot\n"
    else:
        lines = []
        top_stats = tracemalloc.take_snapshot().compare_to(s, 'lineno')
        for stat in top_stats[:NUMBER_OF_TOP_LEAKS_TO_SHOW]:
            if (APP_FOLDER in str(stat)) and (".venv" not in str(stat)):
                lines.append(str(stat))
        return "\n<br>".join(lines)

if __name__ == '__main__':
    app.run(debug=True)