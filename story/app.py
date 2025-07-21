from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# ✅ Add your real OpenAI API key here
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("ai_storybook_final.html")

@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return jsonify({"image_url": image_url})
    except Exception as e:
        print("Image generation failed:", str(e))
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
