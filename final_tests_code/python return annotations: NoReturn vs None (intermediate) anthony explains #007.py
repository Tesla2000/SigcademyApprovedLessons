import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the difference between the return annotation `-> None` and `-> NoReturn`?', 'What are the two cases where the speaker would have `-> None` in Python functions?', 'Does Python insert an implicit return `None` at the end of every function?', "What is the purpose of 'constant' in programming?", "What does 'return' do in programming?", "What is the difference between 'return' and 'pop' in programming?", 'What are some topics the speaker plan to cover in future videos?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the difference between the return annotation `-> None` and `-> NoReturn`?', 'What are the two cases where the speaker would have `-> None` in Python functions?', 'Does Python insert an implicit return `None` at the end of every function?', "What is the purpose of 'constant' in programming?", "What does 'return' do in programming?", "What is the difference between 'return' and 'pop' in programming?", 'What are some topics the speaker plan to cover in future videos?'], ['The return annotation `-> None` is used to indicate that a function returns nothing, while the return annotation `-> NoReturn` is used to signify that the function will never return, even implicitly. `NoReturn` is special and is applicable in cases where the function always raises an exception, calls a function that replaces the current process, or loops forever without returning. `None` is used for functions that do not return anything, while `NoReturn` is used for functions that will never return under any circumstances.', 'Functions with no return statements and functions that explicitly return `None`.', 'Yes, Python inserts an implicit return `None` at the end of every function that does not have a return statement.', "The 'constant' keyword is used to declare a variable whose value cannot be changed throughout the program.", "The 'return' keyword is used to exit a function and return a value back to the caller.", "In programming, 'return' is used to exit a function and return a value, while 'pop' is used to remove and return the top element from a stack data structure.", 'The speaker plans to cover type annotations and disassembler in more detail in future videos. They also welcome suggestions for additional video topics.']))
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
