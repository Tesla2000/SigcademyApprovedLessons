import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the functools module in Python?', 'What does the LRU cache decorator do in Python?', 'How can the speaker adjust the size of the cache using the LRU cache decorator?', 'What happens when the cache size is exceeded in the LRU cache decorator?', 'What is the purpose of an LRU cache?', 'How can the speaker create a global singleton-like function using an LRU cache?', 'How can the speaker access the underlying function of a function decorated with an LRU cache for testing purposes?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the functools module in Python?', 'What does the LRU cache decorator do in Python?', 'How can the speaker adjust the size of the cache using the LRU cache decorator?', 'What happens when the cache size is exceeded in the LRU cache decorator?', 'What is the purpose of an LRU cache?', 'How can the speaker create a global singleton-like function using an LRU cache?', 'How can the speaker access the underlying function of a function decorated with an LRU cache for testing purposes?'], ['The functools module in Python provides higher-order functions and operations on callable objects.', 'The LRU cache decorator in Python caches the results of a function based on the least recently used principle, allowing for faster access to previously computed results.', "You can adjust the size of the cache by specifying the 'maxsize' parameter when decorating a function with the LRU cache decorator. This parameter determines the maximum number of results to cache.", 'When the cache size is exceeded in the LRU cache decorator, the least recently used results are evicted from the cache to make room for new results.', 'An LRU (Least Recently Used) cache is used to store a limited number of items and evict the least recently used item when the cache is full. This helps in optimizing memory usage and improving performance by keeping frequently accessed items in the cache.', 'You can create a global singleton-like function by using an LRU cache with a max size of 1. This ensures that only one value is stored in the cache, making subsequent calls to the function return the same cached value. This pattern is useful for caching expensive computations or values that do not change.', 'You can access the underlying function of a function decorated with an LRU cache by accessing the double-underscore wrapped attribute. This allows the speaker to bypass the cache and directly call the original function for testing or validation purposes.']))
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
