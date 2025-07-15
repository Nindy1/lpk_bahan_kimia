from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Aplikasi Bahaya Bahan Kimia Organik</h1><p>Buka /data untuk melihat data JSON.</p>"

@app.route('/data')
def data():
    # Baca file Excel
    df = pd.read_excel('LIST BAHAN KIMIA ORGANIK LPK.xlsx')
    # Convert ke JSON
    result = df.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
