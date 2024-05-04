import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the concept being discussed in the video?', 'What is multiple assignment in Python?', 'How does unpacking work in Python?', 'Where can unpacking be used in Python?', 'What is the special meaning of a comma in context managers?', 'How can the speaker unpack values from a list using a star in Python?', "Is 'just an implementation detail' specified somewhere?", 'What has been unpacking?', 'Is unpacking multiple values or easily unpacking variables useful?', 'How can I reach out to the speaker for additional stuff?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the concept being discussed in the video?', 'What is multiple assignment in Python?', 'How does unpacking work in Python?', 'Where can unpacking be used in Python?', 'What is the special meaning of a comma in context managers?', 'How can the speaker unpack values from a list using a star in Python?', "Is 'just an implementation detail' specified somewhere?", 'What has been unpacking?', 'Is unpacking multiple values or easily unpacking variables useful?', 'How can I reach out to the speaker for additional stuff?'], ['The concept being discussed is multiple return values and unpacking in Python.', 'Multiple assignment in Python allows the speaker to assign multiple variables at once using a single statement with comma-separated values on the left-hand side and an iterable on the right-hand side.', 'Unpacking in Python allows the speaker to assign values from an iterable to multiple variables at once by using the comma operator. It is commonly used in functions to unpack multiple return values.', 'Unpacking can be used in assignments, loops, and other contexts in Python to assign values from iterables to multiple variables simultaneously.', 'The comma in context managers is used to indicate multiple context managers. However, in Python 3.9, this behavior will change slightly.', 'You can use a star followed by a variable name to unpack the remaining values from a list. This is known as generalized unpacking.', 'No, it is not specified anywhere.', 'The process or concept being discussed.', 'Yes, it can be useful in certain scenarios.', 'You can leave a comment below or reach out on various platforms.']))
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
