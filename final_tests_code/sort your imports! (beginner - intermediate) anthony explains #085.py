import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['Why are imports in that particular style?', 'How do the speaker ensure that imports stay in that style?', 'What tool is being discussed in the text?', 'What is the purpose of using this tool?', 'How is the tool integrated into the workflow?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['Why are imports in that particular style?', 'How do the speaker ensure that imports stay in that style?', 'What tool is being discussed in the text?', 'What is the purpose of using this tool?', 'How is the tool integrated into the workflow?'], ['The imports are in a particular style with one import per line, even if importing multiple items from the same module. This style helps reduce merge conflicts when multiple developers are working on the codebase.', "The tool 'reorder python imports' is used to format imports to the specified style. It separates imports into standard library, third-party, and first-party imports, and splits 'from' imports. This tool helps maintain consistency and reduces the chance of merge conflicts.", 'reorder python imports', 'To organize and reorder Python imports in a codebase', 'It is run through pre-commit, which is a linter code formatter framework']))
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
