import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the alternative to using `echo -e` for printing special characters like the tab character or newline in terminals?', 'What is the difference between hard quotes and soft quotes in bash?', 'How can the speaker input special characters like the tab character literally in a terminal?', 'What is the name for the action of pressing Ctrl V on the keyboard and then pressing any character to interpret it literally?', 'What character sequence can be used to insert a literal tab?', 'What is an example of a character sequence that can be used to escape a character?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the alternative to using `echo -e` for printing special characters like the tab character or newline in terminals?', 'What is the difference between hard quotes and soft quotes in bash?', 'How can the speaker input special characters like the tab character literally in a terminal?', 'What is the name for the action of pressing Ctrl V on the keyboard and then pressing any character to interpret it literally?', 'What character sequence can be used to insert a literal tab?', 'What is an example of a character sequence that can be used to escape a character?'], ['Using bling strings by putting a dollar sign in front of a hard quote.', 'Hard quotes (single quotes) do not interpret variables or special characters, while soft quotes (double quotes) do interpret variables and special characters.', 'You can use the literal character input by pressing ctrl V on your keyboard followed by the desired special character, such as tab.', 'Escape sequence', 'Ctrl V followed by Tab', 'Ctrl V followed by Escape']))
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
