import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is Test Driven Development (TDD)?', 'Do the speaker practice Test Driven Development (TDD)?', 'What is the purpose of writing tests in Test-Driven Development (TDD)?', 'Why is it important for a test to fail before fixing the code?', 'How can the speaker handle different cases based on the length of the input in a function?', 'When is it recommended to apply Test-Driven Development (TDD)?', 'What are some tools or techniques that can be leveraged when writing tests for code?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is Test Driven Development (TDD)?', 'Do the speaker practice Test Driven Development (TDD)?', 'What is the purpose of writing tests in Test-Driven Development (TDD)?', 'Why is it important for a test to fail before fixing the code?', 'How can the speaker handle different cases based on the length of the input in a function?', 'When is it recommended to apply Test-Driven Development (TDD)?', 'What are some tools or techniques that can be leveraged when writing tests for code?'], ['Test Driven Development (TDD) is a software development approach where tests are written before the actual code implementation. The idea is to write tests that define the desired behavior of the code, then write the code to pass those tests.', 'Yes, I practice Test Driven Development in my software development process. It helps me focus on writing simpler and more testable code by writing tests first.', 'The purpose of writing tests in Test-Driven Development (TDD) is to drive the implementation of the code by first writing tests that define the desired behavior, then writing the code to make those tests pass.', 'It is important for a test to fail before fixing the code because a failing test ensures that the test is actually testing the desired behavior. If the test passes before any code changes, it may indicate that the test is not thorough enough or that the implementation is incorrect.', 'You can handle different cases based on the length of the input in a function by using conditional statements, such as if-else blocks, to check the length of the input and execute different code paths accordingly. This allows the function to handle different scenarios based on the length of the input.', 'It is recommended to apply TDD when the speaker know exactly what the speaker want to do and have an idea of how to do it, or in bug fixing situations. TDD may not be a good idea when the speaker are unsure about the design of your program, as it can constrict the speaker into a specific interface that makes refactoring difficult. Additionally, tests that are too specific about implementation details can also be a drawback of TDD.', 'Some tools and techniques that can be leveraged when writing tests for code include code coverage analysis tools, mutation testing, property-based testing, and parametrized testing. These tools help ensure that tests cover all edge cases, validate behavior, and improve the quality of the codebase.']))
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
