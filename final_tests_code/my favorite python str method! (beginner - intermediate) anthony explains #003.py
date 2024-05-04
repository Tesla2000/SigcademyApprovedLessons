import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the topic of the video?', 'What imaginary problem is being used to explain the string class method?', 'What method from the string class is being discussed in the video?', 'What is the purpose of using the partition method in Python?', 'What is the difference between partition and rpartition methods in Python?', 'How can the partition method be used to simplify code logic in string manipulation?', 'What is an example where the speaker might want to use partition to search for a file extension or the entire file name?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the topic of the video?', 'What imaginary problem is being used to explain the string class method?', 'What method from the string class is being discussed in the video?', 'What is the purpose of using the partition method in Python?', 'What is the difference between partition and rpartition methods in Python?', 'How can the partition method be used to simplify code logic in string manipulation?', 'What is an example where the speaker might want to use partition to search for a file extension or the entire file name?'], ['Explaining the favorite method on the string class in Python and ways to use it in different situations.', 'Sorting requirements in a requirement text file.', 'The partition method.', 'The partition method in Python is used to split a string into three parts based on a specified separator. It returns a tuple containing the part before the separator, the separator itself, and the part after the separator.', 'The partition method searches for the separator from the left-hand side of the string, while the rpartition method searches for the separator from the right-hand side of the string.', 'By using the partition method, the speaker can avoid complex branching logic in string manipulation tasks. It allows the speaker to split a string based on a separator and handle different cases more efficiently.', 'You can use partition to search for a file extension or the entire file name in cases where a file name may contain multiple dots or when the speaker want to handle cases where the file does not have an extension.']))
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
