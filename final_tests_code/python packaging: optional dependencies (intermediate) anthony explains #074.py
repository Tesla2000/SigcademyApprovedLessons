import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the key used to set up optional requirements in setup tools?', 'How do the speaker select an extra when working with a package?', 'What is the purpose of the video?', 'How do the speaker specify required dependencies in setup tools?', 'What are extras in setup tools used for?', 'How can the speaker specify extras in setup tools?', 'Can the speaker provide an example of using extras in setup tools?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the key used to set up optional requirements in setup tools?', 'How do the speaker select an extra when working with a package?', 'What is the purpose of the video?', 'How do the speaker specify required dependencies in setup tools?', 'What are extras in setup tools used for?', 'How can the speaker specify extras in setup tools?', 'Can the speaker provide an example of using extras in setup tools?'], ["The key used to set up optional requirements in setup tools is 'extras_require'.", "To select an extra when working with a package, the speaker use brackets with the extra name. For example, 'pip install .[flask]' to install the 'flask' extra.", 'The video is about optional dependencies in Python packaging, specifically focusing on how to set up optional requirements in setup tools.', "Required dependencies in setup tools are specified using the 'install_requires' option, which is a list of package names that need to be installed.", 'Extras in setup tools are used to define optional dependencies that are only needed in certain development environments or for specific features.', 'Extras can be specified using the options.extras_require ini section in setup.cfg, where the speaker define different extra types and their corresponding dependencies.', "Sure! An example of using extras in setup tools is specifying 'testing' as an extra, which pulls in testing requirements like pytest, mock, and hypothesis when installing the package with that extra."]))
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
