import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["Why does the speaker use 'head' in all caps when pushing branches?", "How does the speaker push a branch to a remote named 'origin' using the shortcut?", "Can the speaker use the 'head' shortcut with a different remote name?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["Why does the speaker use 'head' in all caps when pushing branches?", "How does the speaker push a branch to a remote named 'origin' using the shortcut?", "Can the speaker use the 'head' shortcut with a different remote name?"], ["The speaker uses 'head' in all caps as a shortcut to push the current branch to the remote named origin without having to type out the full branch name.", "The speaker uses the command 'git push origin head' to push the current branch to the remote named 'origin' without specifying the branch name explicitly.", "Yes, the speaker can use the 'head' shortcut with a different remote name by replacing 'origin' with the name of the desired remote when pushing a branch."]))
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
