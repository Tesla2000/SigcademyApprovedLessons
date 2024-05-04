import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What are we going to be talking about in this video?', 'What is the purpose of using parentheses in a regular expression?', 'What does the zeroth group represent in a regular expression match?', 'How can the speaker access positional groups in Python using a shortcut?', 'What is the syntax for defining a named capturing group in a regular expression?', 'What are the three types of captures in regular expressions?', 'How do the speaker define a named capture group in a regular expression?', 'What is a non-capturing group in a regular expression?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What are we going to be talking about in this video?', 'What is the purpose of using parentheses in a regular expression?', 'What does the zeroth group represent in a regular expression match?', 'How can the speaker access positional groups in Python using a shortcut?', 'What is the syntax for defining a named capturing group in a regular expression?', 'What are the three types of captures in regular expressions?', 'How do the speaker define a named capture group in a regular expression?', 'What is a non-capturing group in a regular expression?'], ['Capturing groups in regular expressions.', 'Parentheses denote a capturing group in a regular expression.', 'The zeroth group represents the entire string match in a regular expression.', 'In Python, the speaker can access positional groups using brackets as an alias for the group function.', 'The syntax for defining a named capturing group is ?P<name> in a regular expression.', 'The three types of captures in regular expressions are positional captures, named captures, and non-capturing captures.', 'A named capture group in a regular expression is defined using the syntax ?P<name>. This allows the speaker to access the captured group by its name in addition to its position.', 'A non-capturing group in a regular expression is denoted by the syntax (?:pattern). It allows the speaker to group patterns without capturing them, which can be useful for logical grouping without extracting the matched text.']))
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
