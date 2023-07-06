import openai
openai.api_key = "<your_api_key>"

prompt = "Hello, how are you?"
model = "text-davinci-002"
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=50
)

print(response.choices[0].text)
