from config import openai_key
import openai
openai.api_key = openai_key


def prom2gpt(prom, model="text-davinci-003", temperature=0.7, max_tokens=1000, top_p=1.0, ):
    response = openai.Completion.create(
        prompt=prom,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p, )
    return response['choices'][0]['text']
