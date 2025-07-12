import os
import openai

openai.api_key = os.getenv("OPENROUTER_API_KEY")

def generate_site(client_id, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    content = response['choices'][0]['message']['content']

    with open("templates/portfolio-template/index.html", "r") as f:
        template = f.read()

    site_output = template.replace("{{CONTENT}}", content)

    output_path = f"client-sites/{client_id}/index.html"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(site_output)

    return output_path
