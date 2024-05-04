import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['How did Anthony get started in open source?', 'What platforms does Anthony use for open source development?', 'What advice does Anthony give for beginners in open source?', 'How can beginners get started on open source projects?', 'How did the speaker get started working on open source projects?', 'Can the speaker explain your experience with PI test and how the speaker progressed in your contributions?', 'How did the speaker become a maintainer of the Flake8 project?', 'What advice do the speaker have for others looking to get involved in open source projects?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['How did Anthony get started in open source?', 'What platforms does Anthony use for open source development?', 'What advice does Anthony give for beginners in open source?', 'How can beginners get started on open source projects?', 'How did the speaker get started working on open source projects?', 'Can the speaker explain your experience with PI test and how the speaker progressed in your contributions?', 'How did the speaker become a maintainer of the Flake8 project?', 'What advice do the speaker have for others looking to get involved in open source projects?'], ['Anthony got started in open source by finding projects that he uses frequently and looking for easy or first-time contributor labeled issues to work on.', 'Anthony primarily uses GitHub for open source development, but also mentions GitLab as another popular platform.', 'Anthony advises beginners to start by finding projects they use frequently, looking for labeled issues to work on, and reaching out to maintainers for guidance.', "Beginners can get started on open source projects by creating a GitHub or GitLab account, finding projects they use frequently, looking for labeled issues, and following the project's contributing guidelines.", 'I got started by contributing small fixes to projects when I encountered bugs or issues. Over time, I started working on more features and eventually became a maintainer and core developer of some projects.', 'In mid-2018, I started working on more features in PI test and gradually increased my contributions. I was eventually added as a contributor and then elevated to a core developer. I started by fixing bugs and then moved on to adding new features.', "For Flake8, I noticed the project was inactive and offered to take on a maintainer role. I had experience with related tools and code linters, so I proposed to the previous maintainer to help push the project forward. I started by triaging and updating the issue tracker to understand the project's challenges and priorities.", 'Start by contributing small fixes or features to projects the speaker use. Offer to help maintain projects that the speaker have experience with and show your dedication by actively participating in issue triaging and code contributions. People are usually happy to add new contributors and reduce their workload.']))
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
