import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the difference between single quotes and double quotes in Python strings?', 'What is the recommendation regarding using single quotes or double quotes in Python strings according to Pepe de?', 'When would the speaker deviate from using single quotes or double quotes in Python strings?', 'Why does the speaker prefer single quotes in Python strings?', 'What recommendation does the speaker give for maintaining consistency in code bases with multiple contributors?', 'What is the name of the tool that replaces double quoted strings with single quoted strings?', 'What is the option in Black that prevents it from rewriting strings in either direction?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the difference between single quotes and double quotes in Python strings?', 'What is the recommendation regarding using single quotes or double quotes in Python strings according to Pepe de?', 'When would the speaker deviate from using single quotes or double quotes in Python strings?', 'Why does the speaker prefer single quotes in Python strings?', 'What recommendation does the speaker give for maintaining consistency in code bases with multiple contributors?', 'What is the name of the tool that replaces double quoted strings with single quoted strings?', 'What is the option in Black that prevents it from rewriting strings in either direction?'], ['There is no difference between single quotes and double quotes in Python strings. Both are equivalent and can be used interchangeably.', 'Pepe de, the official style guide of Python, recommends picking either single quotes or double quotes and sticking to it for consistency. There is no preference between the two as long as the speaker are consistent.', 'You may deviate from using single quotes or double quotes in Python strings if the content of your string includes the other quote character. In such cases, it is recommended to use the quote character that avoids the need for escape sequences.', 'The speaker prefers single quotes in Python strings because it avoids the need to press the shift key, which can help in avoiding typos. This preference is based on personal choice and does not have a significant impact on the code.', 'The speaker recommends using a code formatter, such as Black, to ensure consistency in coding style, including the use of single or double quotes in strings. Code formatters help maintain uniformity in code bases with multiple contributors.', 'Double Quote String Fixer', 'skip_strings_normalization']))
    chat = langchain_openai.ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
    chat_answer = chat.invoke(
        [
            langchain_core.messages.SystemMessage(content="You will be given question, reference answer pair and users answer. "
                                  'You have to decide if the answer is correct. '
                                  'If it is respond with a single work "Correct" otherwise return a hint about the answer. '),
            langchain_core.messages.SystemMessage(content='The question: ' + question + '\n'
                                  'The reference answer: ' + reference_answers[question]),
            langchain_core.messages.HumanMessage(
                content=answer
            )
        ]
    ).content
    if chat_answer.startswith("Correct"):
        return True
    return chat_answer
