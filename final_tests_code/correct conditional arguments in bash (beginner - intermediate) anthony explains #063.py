import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the shebang in a bash script?', "What does 'set -euo pipefail' do in a bash script?", 'Why is it recommended to avoid using if statements in bash scripts?', "What is the purpose of the 'test' command in bash?", 'What is the issue with not quoting variables in bash scripts?', 'What is the problem with not quoting certain variables in a bash script?', 'What is the recommended solution to avoid issues with spaces in variables in bash scripts?', 'What is the purpose of using a dollar sign and star in bash scripting?', 'How can the speaker properly handle conditional arguments in bash scripting?', 'What does the set -u command do in bash scripting?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the shebang in a bash script?', "What does 'set -euo pipefail' do in a bash script?", 'Why is it recommended to avoid using if statements in bash scripts?', "What is the purpose of the 'test' command in bash?", 'What is the issue with not quoting variables in bash scripts?', 'What is the problem with not quoting certain variables in a bash script?', 'What is the recommended solution to avoid issues with spaces in variables in bash scripts?', 'What is the purpose of using a dollar sign and star in bash scripting?', 'How can the speaker properly handle conditional arguments in bash scripting?', 'What does the set -u command do in bash scripting?'], ['The shebang (#!) at the beginning of a bash script specifies the path to the interpreter that should be used to execute the script. It makes the script executable from the command line.', "'set -euo pipefail' is a set of options that enable a strict mode for bash scripting. '-e' terminates the process if any command exits with a non-zero status, '-u' causes bash to exit if an undefined variable is used, 'o pipefail' makes the entire pipe fail if any command in a pipe sequence fails, and 'x' shows every command as it runs.", "It is recommended to avoid using if statements in bash scripts because bash's syntax for conditionals can be complex and error-prone. Using a more high-level scripting language like Python is often preferred for better readability and maintainability.", "The 'test' command in bash is used to evaluate expressions and return a success or failure status. It is often used within conditional statements like if statements to perform tests on files, strings, and other conditions.", 'Not quoting variables in bash scripts can lead to word splitting and globbing issues, especially when the variable contains spaces or special characters. It is recommended to always quote variables to ensure proper handling of their values.', 'The problem with not quoting certain variables in a bash script is that if the variable contains spaces, it will get split into multiple arguments instead of being treated as a single argument.', 'The recommended solution is to use arrays in bash to store and pass arguments, ensuring that variables with spaces are treated as a single argument.', 'The dollar sign and star combination is used to reference all positional parameters passed to a script or function in bash. It is a way to access all the arguments passed to the script or function.', 'To properly handle conditional arguments in bash scripting, the speaker should always quote variable things to prevent argument splatting. This ensures that the arguments are treated as single entities and not split into multiple arguments. Additionally, using proper quoting helps avoid errors and ensures the script behaves as expected.', "The set -u command in bash scripting, also known as set -o nounset, enables the 'unbound variable' option. When this option is set, attempting to expand an unset variable will result in an error, indicating that the variable is unbound. This helps catch potential errors caused by referencing unset variables in the script."]))
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
