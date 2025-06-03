from flask import Flask, render_template, request, jsonify
from rgbmatrix import RGBMatrix, RGBMatrixOptions

app = Flask(__name__)

options = RGBMatrix()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = "adafruit-hat"
matrix = RGBMatrix(options = options)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/set_pixel', methods=['POST'])
def set_pixel():
    data = request.json
    x = int(data['x'])
    y = int(data['y'])
    hex_color = data['color'].lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    updatePixel(x, y, r, g, b)
    return jsonify({"status": "success"})

def updatePixel(x, y, r, g, b):
    matrix.SetPixel(x, y, r, g, b)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5090)