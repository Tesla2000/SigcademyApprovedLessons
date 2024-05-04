import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["Why did the speaker use the 'use fixtures' decorator in pytest instead of the normal way of using fixtures?", 'What tool is being discussed in the text?', 'What does Pilot complain about when running on a specific file?', 'What is the reason for using static analysis tools according to the text?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["Why did the speaker use the 'use fixtures' decorator in pytest instead of the normal way of using fixtures?", 'What tool is being discussed in the text?', 'What does Pilot complain about when running on a specific file?', 'What is the reason for using static analysis tools according to the text?'], ["The speaker used the 'use fixtures' decorator in pytest instead of the normal way of using fixtures because it seems to be a little bit nicer on static analysis tools. The argument in the function was completely unused, which many IDEs and other tools would flag as an error unless they knew about pytest's specific magical behavior. The 'use fixtures' decorator enables the fixture but doesn't pass it into the function, which helps avoid confusion for static analysis tools.", 'Pilot', 'Pilot complains about redefining an outer name and having an unused argument.', 'The reason for using static analysis tools is to identify issues like redefining names and unused arguments.']))
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
