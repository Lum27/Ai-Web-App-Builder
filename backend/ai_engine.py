import os
import openai

openai.api_key = os.getenv("OPENROUTER_API_KEY")

def generate_site(client_id, prompt):
    # Request sectioned content from the AI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"""
You are an expert website copywriter. Based on this prompt:
"{prompt}", generate 4 sections as plain text:
- MAIN_TITLE
- ABOUT
- SERVICES
- CONTACT
Format the output exactly like this:

MAIN_TITLE: [Main headline here]
ABOUT: [Paragraph about the business]
SERVICES: [Bullet list or paragraph of services]
CONTACT: [Contact info or call-to-action]
            """}
        ]
    )

    # Parse the AI response
    content = response['choices'][0]['message']['content']
    lines = content.splitlines()

    data = {
        "MAIN_TITLE": "",
        "ABOUT": "",
        "SERVICES": "",
        "CONTACT": ""
    }

    for line in lines:
        if line.startswith("MAIN_TITLE:"):
            data["MAIN_TITLE"] = line.replace("MAIN_TITLE:", "").strip()
        elif line.startswith("ABOUT:"):
            data["ABOUT"] = line.replace("ABOUT:", "").strip()
        elif line.startswith("SERVICES:"):
            data["SERVICES"] = line.replace("SERVICES:", "").strip()
        elif line.startswith("CONTACT:"):
            data["CONTACT"] = line.replace("CONTACT:", "").strip()

    # Load your HTML template
    with open("templates/portfolio-template/index.html", "r") as f:
        template = f.read()

    # Inject AI-generated values into the template
    site_output = template \
        .replace("{{MAIN_TITLE}}", data["MAIN_TITLE"]) \
        .replace("{{ABOUT}}", data["ABOUT"]) \
        .replace("{{SERVICES}}", data["SERVICES"]) \
        .replace("{{CONTACT}}", data["CONTACT"])

    # Save output to client-specific folder
    output_path = f"client-sites/{client_id}/index.html"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(site_output)

    return output_path
