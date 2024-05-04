import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What are the two ways the user mentioned for making commit messages before learning the new tip?', 'What is the new tip the user learned for making commit messages easier?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What are the two ways the user mentioned for making commit messages before learning the new tip?', 'What is the new tip the user learned for making commit messages easier?'], ["1. Using 'git commit -m <commit message>'\n2. Leaving out the -m flag to open the text editor for adding more contents to the body of the commit message.", 'Specifying the -m flag more than once to fill in the body of the commit message without opening the text editor.']))
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
