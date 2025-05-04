from flask import Flask, request, jsonify

app = Flask(__name__)
pcr_data = {}

@app.route("/update_pcr", methods=["POST"])
def update_pcr():
    content = request.json
    symbol = content.get("symbol")
    pcr = content.get("pcr")
    if symbol and pcr:
        pcr_data[symbol.upper()] = pcr
        return jsonify({"status": "success", "message": f"PCR updated for {symbol}"}), 200
    return jsonify({"status": "error", "message": "Missing symbol or PCR"}), 400

@app.route("/get_pcr/<symbol>", methods=["GET"])
def get_pcr(symbol):
    value = pcr_data.get(symbol.upper())
    if value is not None:
        return jsonify({"symbol": symbol, "pcr": value}), 200
    return jsonify({"error": "PCR not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
