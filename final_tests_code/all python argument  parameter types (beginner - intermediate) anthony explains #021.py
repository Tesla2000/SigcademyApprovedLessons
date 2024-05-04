import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What are the different types of arguments in Python?', 'What is the value of X when calling the function with arguments 1, 2, 3?', 'What happens if the speaker try to pass a named argument when calling the function with positional arguments?', 'How can the speaker create named only arguments in the function?', 'What is the convention for collecting all positional arguments in a function?', 'How do the speaker collect all named arguments in a function?', 'What are the various types of arguments in Python?', 'When would the speaker use normal arguments in Python functions?', 'In what scenarios would the speaker use collection arguments in Python functions?', 'Can the speaker provide an example of using collection arguments in Python functions?', 'When are named-only arguments commonly used in Python functions?', 'What is the purpose of positional-only arguments in Python functions?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What are the different types of arguments in Python?', 'What is the value of X when calling the function with arguments 1, 2, 3?', 'What happens if the speaker try to pass a named argument when calling the function with positional arguments?', 'How can the speaker create named only arguments in the function?', 'What is the convention for collecting all positional arguments in a function?', 'How do the speaker collect all named arguments in a function?', 'What are the various types of arguments in Python?', 'When would the speaker use normal arguments in Python functions?', 'In what scenarios would the speaker use collection arguments in Python functions?', 'Can the speaker provide an example of using collection arguments in Python functions?', 'When are named-only arguments commonly used in Python functions?', 'What is the purpose of positional-only arguments in Python functions?'], ['1. Normal arguments\n2. Default arguments\n3. Named only default arguments\n4. Positional only arguments', 'X is a tuple containing the values 1, 2, and 3.', "It will raise an error saying 'unexpected keyword argument X'.", "By using the slash (/) syntax to indicate positional only arguments, followed by the named only arguments like 'Y' in this case.", "The convention is to use '*args' to collect all positional arguments.", "By using '**kwargs' to collect all named arguments into a dictionary.", 'The various types of arguments in Python are positional-only arguments, normal arguments, defaulted normal arguments, extra positional arguments, required named-only arguments, defaulted named-only arguments, and leftover named arguments.', 'Normal arguments are commonly used in functions that do not require any special handling of arguments. They are the most common type of arguments used in Python functions.', 'Collection arguments, such as collecting extra positional arguments or leftover named arguments, are useful in functions that need to pass through their arguments to other functions without explicitly defining each argument.', 'One example of using collection arguments is when writing subprocess routines where the subprocess API requires an interval as the first argument. By using collection arguments, like collecting extra positional arguments or leftover named arguments, the speaker can simplify the function call and pass along the necessary arguments.', 'Named-only arguments are often used in functions with a large number of parameters, boolean parameters, or arguments that might be easily confused based on order. They provide clarity and flexibility in function calls.', 'Positional-only arguments were introduced in Python 3.8 to allow defining arguments that can only be passed positionally and not as keyword arguments. They are useful for defining APIs where argument names may need to be refactored later.']))
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
