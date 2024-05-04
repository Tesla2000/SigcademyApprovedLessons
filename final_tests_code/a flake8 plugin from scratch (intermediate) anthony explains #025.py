import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the plugin being developed in the video?', 'What specific behavior does the plugin aim to guard against?', 'What tools are being installed to help develop the plugin?', 'What is the name of the Flake8 plugin being developed in the video?', 'What is the name of the plugin class?', 'What are the two minimum attributes required for the plugin class?', 'How do the speaker retrieve the version from packaging metadata?', 'What attributes need to be set up for the plugin?', 'What is the argument called that represents a single file in a code base in the plugin?', "What does the 'run' generator return in the plugin?", "What is the purpose of the helper function 'results' in the code snippet?", 'What does the code snippet do after constructing the plugin and tree arguments?', "What is the purpose of the 'test trivial case' in the code snippet?", "What is the purpose of the 'test incorrect named arguments' in the code snippet?", 'What class does the visitor extend from?', 'What method in the visitor class is used to visit a call node in the AST?', 'Why is it recommended to call self.generic_visit() at the end of visit methods?', 'What state does the visitor class need to keep track of?', 'What error message is yielded when encountering the specific issue in the visit_call method?', 'What are we looking for in the code snippet?', 'What condition are we checking for the keyword argument?', 'What type of value are we checking for in the code snippet?', 'How do we check if all keys in the dictionary are strings?', 'How do we check if a string is an identifier?', 'What do we append to the tuple if the conditions are met?', 'What adjustment did we make to fix the test?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the plugin being developed in the video?', 'What specific behavior does the plugin aim to guard against?', 'What tools are being installed to help develop the plugin?', 'What is the name of the Flake8 plugin being developed in the video?', 'What is the name of the plugin class?', 'What are the two minimum attributes required for the plugin class?', 'How do the speaker retrieve the version from packaging metadata?', 'What attributes need to be set up for the plugin?', 'What is the argument called that represents a single file in a code base in the plugin?', "What does the 'run' generator return in the plugin?", "What is the purpose of the helper function 'results' in the code snippet?", 'What does the code snippet do after constructing the plugin and tree arguments?', "What is the purpose of the 'test trivial case' in the code snippet?", "What is the purpose of the 'test incorrect named arguments' in the code snippet?", 'What class does the visitor extend from?', 'What method in the visitor class is used to visit a call node in the AST?', 'Why is it recommended to call self.generic_visit() at the end of visit methods?', 'What state does the visitor class need to keep track of?', 'What error message is yielded when encountering the specific issue in the visit_call method?', 'What are we looking for in the code snippet?', 'What condition are we checking for the keyword argument?', 'What type of value are we checking for in the code snippet?', 'How do we check if all keys in the dictionary are strings?', 'How do we check if a string is an identifier?', 'What do we append to the tuple if the conditions are met?', 'What adjustment did we make to fix the test?'], ['The purpose of the plugin is to prevent passing keyword arguments using a dictionary in Python function calls.', 'The plugin aims to guard against passing keyword arguments using a dictionary in Python function calls, and only allow passing keyword arguments individually.', 'The tools being installed are Flake8, pytest, and astpretty.', "The Flake8 plugin is named 'flake8-no-like-named-arguments'.", 'flake8_named_arguments', 'name and version', "importlib.metadata.version('flake8_named_arguments')", 'Name and version attributes', 'tree', 'A tuple of (int, int, str, type)', "The purpose of the 'results' helper function is to take in a string of the AST and return a set of results.", 'After constructing the plugin and tree arguments, the code snippet creates a set of results by running the plugin on the AST tree.', "The purpose of the 'test trivial case' is to ensure that an empty file does not result in any errors, and the set of results should be empty.", "The purpose of the 'test incorrect named arguments' is to check for cases where named arguments should not use certain syntax, and to verify that the plugin correctly identifies and handles such cases.", 'ast.NodeVisitor', 'visit_call', 'To ensure the recursion continues and all nodes are visited in the AST.', 'A list of tuples containing line number and column offset information.', 'FN100: All arguments in **kwargs should have identifiers.', "We are looking for keywords where the argument is 'None' and the value is a dictionary.", "We are checking if the keyword argument is 'None'.", 'We are checking if the value is a dictionary.', "We check if all keys are of type 'str'.", "We use the built-in method 'isidentifier()' on Python strings.", 'We append the line number and column offset of the node.', 'We adjusted the column offset by adding 1 to it.']))
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
