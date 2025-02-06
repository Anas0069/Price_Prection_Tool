from flask import Flask, render_template, request, jsonify
from pricing import predict_product_price_with_range_and_profit

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        # Extract input values from the frontend
        production_cost = float(data['production_cost'])
        labour_cost = float(data['labour_cost'])
        raw_material_cost = float(data['raw_material_cost'])
        rent = float(data['rent'])
        advertising = float(data['advertising'])
        packet_size = int(data['packet_size'])

        # Call the prediction function from the pricing module
        predicted_price, lower_bound, upper_bound = predict_product_price_with_range_and_profit(
            production_cost=production_cost,
            labour_cost=labour_cost,
            raw_material_cost=raw_material_cost,
            rent=rent,
            advertising=advertising,
            packet_size=packet_size  # Removed R_and_D and tax_percentage
        )

        # Return the prediction result as JSON
        return jsonify({
            "predicted_price": round(predicted_price, 2),
            "lower_bound": round(lower_bound, 2),
            "upper_bound": round(upper_bound, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
