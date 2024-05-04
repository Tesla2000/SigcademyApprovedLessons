import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What are the two tools mentioned for package management on Debian-like systems?', 'Which tool should be preferred for command-line interface usage?', 'Which tool should be preferred for scripts, including Dockerfiles?', "What does 'apt update' command do?", "How often should the speaker run 'apt update'?", "What does 'apt install' command do?", "What is the special expansion 'bang-bang' used for in the terminal?", 'What is the opposite of installing a package?', "What is the difference between 'remove' and 'purge' when uninstalling a package?", "How can the speaker uninstall a package using 'purge' in apt?", 'What command can the speaker use to remove packages that are no longer needed after uninstalling a package?', 'What command shows information about a package in Emacs?', 'How can the speaker list the files provided by a package in Emacs?', 'What command can be used to search for a package that provides a specific file in Emacs?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What are the two tools mentioned for package management on Debian-like systems?', 'Which tool should be preferred for command-line interface usage?', 'Which tool should be preferred for scripts, including Dockerfiles?', "What does 'apt update' command do?", "How often should the speaker run 'apt update'?", "What does 'apt install' command do?", "What is the special expansion 'bang-bang' used for in the terminal?", 'What is the opposite of installing a package?', "What is the difference between 'remove' and 'purge' when uninstalling a package?", "How can the speaker uninstall a package using 'purge' in apt?", 'What command can the speaker use to remove packages that are no longer needed after uninstalling a package?', 'What command shows information about a package in Emacs?', 'How can the speaker list the files provided by a package in Emacs?', 'What command can be used to search for a package that provides a specific file in Emacs?'], ['apt and apt-get', 'apt', 'apt-get', 'Downloads metadata describing all packages in the package archives', 'Once a day or before installing new packages', 'Installs a particular package', 'Expands to the entire previous command', 'Uninstalling a package', "'Remove' leaves behind configuration files while 'purge' removes all configuration files as well", "You can use 'sudo apt purge <package_name>' to uninstall a package using 'purge' in apt", "You can use 'sudo apt autoremove --purge' to remove packages that are no longer needed after uninstalling a package", 'd-bags -l', 'd-package -L', 'd-package -S']))
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
