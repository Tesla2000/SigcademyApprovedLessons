import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What command is being used to run the docker container in the provided scenario?', 'What is the purpose of running the command inside a docker container in this scenario?', 'What happens when rm -rf is executed inside the docker container with no preserve root?', 'How does the shell continue to function even after essential utilities like ls have been deleted?', 'What is mentioned as a way to potentially recover a broken container after running rm -rf /?', 'What is the purpose of exporting a container to a tar file?', 'What are some precautions to take before running commands that modify containers?', 'What command is used to extract the contents of a tar file?', 'How can the speaker copy directories from one container to another using Podman?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What command is being used to run the docker container in the provided scenario?', 'What is the purpose of running the command inside a docker container in this scenario?', 'What happens when rm -rf is executed inside the docker container with no preserve root?', 'How does the shell continue to function even after essential utilities like ls have been deleted?', 'What is mentioned as a way to potentially recover a broken container after running rm -rf /?', 'What is the purpose of exporting a container to a tar file?', 'What are some precautions to take before running commands that modify containers?', 'What command is used to extract the contents of a tar file?', 'How can the speaker copy directories from one container to another using Podman?'], ['podman run rmti ubuntu focal bash', 'To test the behavior of running rm -rf with no preserve root in a controlled environment without affecting the host machine.', 'It deletes a significant portion of the files in the container, including essential utilities like ls, but some files remain due to being special device files or mounted in a special way.', 'The shell has built-in functionalities that allow basic operations to be performed even without the specific executable files. Additionally, when an executable is loaded into memory, it can continue to run even if the file is deleted from disk.', 'Using another container to bootstrap the broken container back to a functional state.', 'Exporting a container to a tar file involves taking the root file system of the container and saving it as a tar archive. This allows for easy sharing, backup, or migration of the container.', 'Before running commands that modify containers, it is recommended to take precautions such as creating a snapshot of the virtual machine or container to ensure that the speaker can restore it in case of any issues.', "The command 'tar -xf <file.tar>' is used to extract the contents of a tar file. The 'x' flag stands for extract, 'f' flag specifies the file, and 'tar' is the command itself.", "You can copy directories from one container to another using the 'podman cp' command. For example, 'podman cp <source_container>:<source_path> <destination_container>:<destination_path>' can be used to copy directories between containers."]))
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
