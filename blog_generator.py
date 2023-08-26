from dotenv import dotenv_values
import openai

config = dotenv_values('blog_generator.env')

openai.api_key = config['api_key']

def generate_blog(paragraphic_topic):
    response = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = 'Write a paragraph about the following topic: ' + paragraphic_topic,
        max_tokens = 400,
        temperature = 0.7
    )

    retrieve_blog = response.choices[0].text
    return retrieve_blog
    
keep_writing = True

while keep_writing:
    answer = input('Write a paragrah? Y for Yes, anything other character for no.')
    while keep_writing:
        if answer == 'Y':
            paragraph_topic = input('What should the topic of this blog post be?')
            print(generate_blog(paragraph_topic))
        else:
            False


generate_blog('Who is the most hated president in the history of the United States?')
