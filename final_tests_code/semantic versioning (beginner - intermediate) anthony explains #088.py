import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What versioning approach does the speaker try to stick to?', 'What are the three components of a version in semantic versioning?', 'When is the major version incremented in semantic versioning?', 'What does incrementing the minor version indicate in semantic versioning?', 'What does the patch version typically represent in semantic versioning?', 'What is the significance of version 2.0 in semantic versioning?', 'According to semantic versioning, what is the purpose of declaring a public API?', 'Why are version numbers considered immutable in semantic versioning?', 'What is the exception to the versioning rules before version zero in semantic versioning?', 'What versioning scheme is being discussed in the text?', 'What is the difference between semantic versioning and zero versioning?', 'Give an example of a project that is using zero versioning.', 'Why is it mentioned that zero versioning may not always work as a versioning scheme?', 'What is calendar versioning?', 'How does calendar versioning differ from semantic versioning?', 'Give an example of a software using calendar versioning.']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What versioning approach does the speaker try to stick to?', 'What are the three components of a version in semantic versioning?', 'When is the major version incremented in semantic versioning?', 'What does incrementing the minor version indicate in semantic versioning?', 'What does the patch version typically represent in semantic versioning?', 'What is the significance of version 2.0 in semantic versioning?', 'According to semantic versioning, what is the purpose of declaring a public API?', 'Why are version numbers considered immutable in semantic versioning?', 'What is the exception to the versioning rules before version zero in semantic versioning?', 'What versioning scheme is being discussed in the text?', 'What is the difference between semantic versioning and zero versioning?', 'Give an example of a project that is using zero versioning.', 'Why is it mentioned that zero versioning may not always work as a versioning scheme?', 'What is calendar versioning?', 'How does calendar versioning differ from semantic versioning?', 'Give an example of a software using calendar versioning.'], ['Semantic versioning.', 'Major, minor, and patch.', 'When making incompatible changes.', 'Adding functionality without changing existing functionality.', 'Fixing functionality without breaking existing functionality.', 'It indicates that at least one incompatible change has been made.', 'To indicate breaking changes, new functionality, or fixes.', 'To prevent re-releasing new code using the same version number.', 'Before version zero, rules like breaking changes and functionality removal do not apply.', 'Semantic versioning and zero versioning', 'Semantic versioning follows a strict rule of incrementing version numbers based on the type of changes (major, minor, patch), while zero versioning allows breaking changes even in version 0.', 'The text editor mentioned in the text is sitting at version 0.0.16 and has had 16 releases with changing functionality.', 'It may be challenging to define what constitutes a breaking change, especially in cases like security fixes where fixing a bug may inadvertently break functionality for some users.', 'Calendar versioning is a popular way to version software where the version number tracks the date and time that the package was released. It does not necessarily indicate changes in the API compatibility, allowing for breaking changes in every release if desired. Versions are typically based on the year, month, or any other chosen format.', 'Calendar versioning tracks the release date and time of a package, while semantic versioning indicates the type of changes (major, minor, patch) in the software. Semantic versioning provides more information about the nature of the changes in each release, such as bug fixes, features, or breaking changes.', 'Ubuntu is an example of software that uses calendar versioning. For instance, version 20.04 of Ubuntu was released in April 2020.']))
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
