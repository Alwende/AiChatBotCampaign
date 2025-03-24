from flask import Flask, request, jsonify

app = Flask(__name__)

campaign_agenda = {
    "economy": "The president's policies have greatly improved the economy.",
    "healthcare": "The president has expanded healthcare access to all citizens.",
    "education": "The president has increased funding for education and scholarships."
}

@app.route('/agenda', methods=['GET'])
def get_agenda():
    topic = request.args.get('topic')
    if topic in campaign_agenda:
        return jsonify({topic: campaign_agenda[topic]})
    else:
        return jsonify({"error": "Topic not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)