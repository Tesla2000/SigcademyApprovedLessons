import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the first approach to string formatting that was mentioned?', 'What is the concatenation operator in Python?', 'What is the problem with concatenation based string formatting for floating-point numbers?', 'What is the purpose of the string template approach in Python?', 'What is the purpose of using string templates in Python?', 'What is the substitute method used for in Python string templates?', 'What is the format specifier used for in Python string formatting?', 'What is the modulo operator (%) used for in Python string formatting?', 'What is the new format introduced in Python 2 that got an upgrade in Python 3?', 'What is the format that uses braced substitutions instead of percent-based substitutions in Python?', 'Which format allows for accessing attributes of objects directly in the string?', 'Which format is recommended if targeting Python 3.6 or above for string formatting?', 'What is a cool feature of F strings in Python 3.6 or above?', 'How can the speaker maintain consistency in using F strings in Python code?', 'What tool has the speaker written for upgrading format string types in Python code?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the first approach to string formatting that was mentioned?', 'What is the concatenation operator in Python?', 'What is the problem with concatenation based string formatting for floating-point numbers?', 'What is the purpose of the string template approach in Python?', 'What is the purpose of using string templates in Python?', 'What is the substitute method used for in Python string templates?', 'What is the format specifier used for in Python string formatting?', 'What is the modulo operator (%) used for in Python string formatting?', 'What is the new format introduced in Python 2 that got an upgrade in Python 3?', 'What is the format that uses braced substitutions instead of percent-based substitutions in Python?', 'Which format allows for accessing attributes of objects directly in the string?', 'Which format is recommended if targeting Python 3.6 or above for string formatting?', 'What is a cool feature of F strings in Python 3.6 or above?', 'How can the speaker maintain consistency in using F strings in Python code?', 'What tool has the speaker written for upgrading format string types in Python code?'], ['Concatenation based string formatting', 'The plus (+) operator', "There isn't a direct way to format floating-point numbers, but it can be achieved using the format built-in function.", 'The purpose of string templates is to provide a way for string substitution using dollar sign ($) placeholders.', 'String templates in Python are used for formatting strings with placeholders that can be replaced with values at runtime.', 'The substitute method is used to replace placeholders in a string template with actual values.', 'The format specifier in Python string formatting is used to specify how a value should be formatted when inserted into a string template.', 'The modulo operator (%) in Python string formatting is used to insert values into a string template by mapping them to placeholders.', 'dot format', 'format', 'dot format', 'f strings', 'You can put an equal sign at the end of an F string to show the expression and its value for debugging.', 'Find a linter or code formatter that can automatically upgrade different format string types, such as converting percent format to dot format and then to F strings.', 'PI upgrade']))
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
