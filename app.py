from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "MSDS Bahan Kimia API Aktif"

@app.route('/get-json')
def get_json():
    # Baca Excel
    df = pd.read_excel('msds_bahan_kimia.xlsx')
    # Convert ke JSON
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

