import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the tool being discussed in the video?', 'What command is commonly used but not recommended in the video?', "What is the recommended replacement command for 'git add .' in the video?", "Why is 'git add -u' recommended over 'git add .' in the video?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the tool being discussed in the video?', 'What command is commonly used but not recommended in the video?', "What is the recommended replacement command for 'git add .' in the video?", "Why is 'git add -u' recommended over 'git add .' in the video?"], ['pre-commit', 'git add .', 'git add -u', 'git add -u only adds modified files that are already tracked by git, avoiding adding untracked files or sensitive information accidentally.']))
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
