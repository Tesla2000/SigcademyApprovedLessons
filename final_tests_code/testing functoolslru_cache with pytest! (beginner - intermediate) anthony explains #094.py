import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the function we are implementing today?', 'What does the get_default_version function do?', 'How does the get_default_version function determine the default version?', 'What library are we using to check if an executable exists on the system?', 'How do we mock the shuttle.which function for testing purposes?', 'What is the purpose of using functools.lru_cache decorator in this context?', 'What is the purpose of using an LRU cache decorator in a function?', 'What issue can arise when testing a function with an LRU cache decorator?', 'What are two approaches to testing a function with an LRU cache decorator?', 'What special attribute is accessed when using double under wrapped in a function?', 'What happens when the inner function is accessed in a function with double under wrapped attribute?', 'What is the suggested approach to bypass the cache in a function?', 'What can be used before and after to clear the cache in a function?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the function we are implementing today?', 'What does the get_default_version function do?', 'How does the get_default_version function determine the default version?', 'What library are we using to check if an executable exists on the system?', 'How do we mock the shuttle.which function for testing purposes?', 'What is the purpose of using functools.lru_cache decorator in this context?', 'What is the purpose of using an LRU cache decorator in a function?', 'What issue can arise when testing a function with an LRU cache decorator?', 'What are two approaches to testing a function with an LRU cache decorator?', 'What special attribute is accessed when using double under wrapped in a function?', 'What happens when the inner function is accessed in a function with double under wrapped attribute?', 'What is the suggested approach to bypass the cache in a function?', 'What can be used before and after to clear the cache in a function?'], ['get_default_version', 'It determines the default version of Ruby based on whether both Ruby and Gem are globally available on the system.', "If both Ruby and Gem are globally available, it returns 'system'. Otherwise, it returns 'default'.", 'shuttle', 'We use the mock.patch.object decorator to temporarily make the shuttle.which function return specific values for testing.', 'To cache the results of the get_default_version function to improve performance when called repeatedly.', 'The purpose of using an LRU cache decorator in a function is to cache the result of the function so that it is only executed once in the context of the process, improving performance by avoiding redundant computations.', 'When testing a function with an LRU cache decorator, the function may always return the cached value, making it challenging to test different scenarios or inputs.', '1. Explicitly clear the cache in between each test run.\n2. Bypass the cache entirely by accessing the __wrapped__ attribute of the function.', 'The double under wrapped attribute of the function.', 'It bypasses the cache and goes directly into the inner function.', 'Using double under wrapped attribute.', 'cache clear.']))
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
