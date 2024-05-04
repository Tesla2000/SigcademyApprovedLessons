import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of parametrize in Pytest?', 'How does parametrize simplify writing tests in Pytest?', 'What are the key components of using parametrize in Pytest?', 'What is the purpose of the `parametrize` function in testing?', 'How can the speaker name parametrized tests using `pytest.param`?', 'What is a common pitfall to avoid when using `parametrize` in tests?', 'What is a special case of parameterizing with only a single parameter input x?', "What is the error code for the test case 'pi_test.raises(TypeError, square, input_x)'?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of parametrize in Pytest?', 'How does parametrize simplify writing tests in Pytest?', 'What are the key components of using parametrize in Pytest?', 'What is the purpose of the `parametrize` function in testing?', 'How can the speaker name parametrized tests using `pytest.param`?', 'What is a common pitfall to avoid when using `parametrize` in tests?', 'What is a special case of parameterizing with only a single parameter input x?', "What is the error code for the test case 'pi_test.raises(TypeError, square, input_x)'?"], ['The purpose of parametrize in Pytest is to simplify writing multiple test cases by allowing the user to specify a series of input values and expected outputs in a table format, which Pytest then uses to generate individual test cases automatically.', 'Parametrize simplifies writing tests in Pytest by allowing the user to define a single test function with input and expected output parameters, and then provide a table of input-output pairs using the parametrize decorator. Pytest automatically generates multiple test cases based on the provided input-output pairs.', 'The key components of using parametrize in Pytest are specifying the parameter names in the test function, providing a table of input-output pairs as arguments to the parametrize decorator, and letting Pytest generate individual test cases based on the input-output pairs.', 'The `parametrize` function in testing allows the speaker to define a list of parameter names and corresponding parameter sets to generate test cases with different input values.', 'You can use `pytest.param` to name parametrized tests by adding it before the parameter set and specifying the name using the `id` parameter. This helps in creating more readable and semantic test names.', 'A common pitfall to avoid when using `parametrize` in tests is adding logic to tests by attaching extra parameters to existing tests. This can lead to complex test implementations and make it harder to refactor and understand the test cases.', 'Using a single string as the parameter name and a single sequence for the test cases.', 'TypeError: square of input x']))
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
