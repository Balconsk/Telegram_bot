from config import openai_key
import openai
openai.api_key = openai_key


def prom2gpt(prompt, model="text-davinci-003", temperature=0.7, max_tokens=1000, top_p=1.0, ):
    """Sending a request to gpt"""
    response = openai.Completion.create(
        prompt=prompt,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p, )
    return {'text': response['choices'][0]['text'], 'token': response['usage']['total_tokens']}


def prom2dall_e(prompt, n=1, size="512x512"):
    """Sending a request to dall e"""
    response = openai.Image.create(prompt=prompt, n=n, size=size)
    return response['data'][0]['url']
