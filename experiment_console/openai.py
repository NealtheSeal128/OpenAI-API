from openai import OpenAI
client = OpenAI()
ask = input("What would you like to ask GPT-5.6?")
response = client.responses.create(
    model="gpt-5.6",
    input=ask
)

print(response.output_text)