import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of hashcash?', 'How can the speaker view all the executables that bash has cached?', 'How can the speaker make bash forget about the hash cache?', 'What is the issue being discussed in the text?', 'What happens to the hash cache when the virtual M is deactivated?', 'What is mentioned as the cause of the hashcrash in the text?', 'How can viewers reach out for additional explanations or questions according to the text?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of hashcash?', 'How can the speaker view all the executables that bash has cached?', 'How can the speaker make bash forget about the hash cache?', 'What is the issue being discussed in the text?', 'What happens to the hash cache when the virtual M is deactivated?', 'What is mentioned as the cause of the hashcrash in the text?', 'How can viewers reach out for additional explanations or questions according to the text?'], ['The purpose of hashcash is to remember the executables that the speaker run on the command line and store them in a cache to prevent path lookups, which can be potentially expensive.', "You can view all the executables that bash has cached by using the command 'hash -l'.", "You can make bash forget about the hash cache by using the command 'hash -r'.", 'The issue being discussed is about a pregnant hash and the activation and deactivation of virtualization.', 'When the virtual M is deactivated, the hash cache should have nothing in it.', 'The hashcrash is explained as a result of the activation and deactivation of virtualization.', 'Viewers can leave a comment below or reach out on various platforms for additional explanations or questions.']))
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
