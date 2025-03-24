from flask import Flask, jsonify

app = Flask(__name__)

# Sample campaign agenda data
campaign_agenda = {
    "economy": "Improve the economy by reducing taxes and increasing job opportunities.",
    "healthcare": "Provide affordable healthcare for all citizens.",
    "education": "Invest in education and provide free college tuition.",
    "environment": "Implement policies to protect the environment and combat climate change."
}

@app.route('/agenda', methods=['GET'])
def get_agenda():
    return jsonify(campaign_agenda)

if __name__ == "__main__":
    app.run(debug=True)