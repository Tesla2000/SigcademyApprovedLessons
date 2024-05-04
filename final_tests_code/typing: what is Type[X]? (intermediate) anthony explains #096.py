import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the main topic of the video?', 'What are the two functions mentioned in the video?', 'What does f1 function take as a parameter?', 'What does f2 function take as a parameter?', 'What is the difference between passing an instance of a class and passing the type of a class?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the main topic of the video?', 'What are the two functions mentioned in the video?', 'What does f1 function take as a parameter?', 'What does f2 function take as a parameter?', 'What is the difference between passing an instance of a class and passing the type of a class?'], ['The main topic of the video is the difference between type x and x in object-oriented programming.', 'The two functions mentioned are f1 and f2.', 'The f1 function takes an instance of a class as a parameter.', 'The f2 function takes the type of a class as a parameter.', 'Passing an instance of a class means passing a constructed version of the class, while passing the type of a class means passing any type that is either the class itself or a subclass of the class.']))
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
