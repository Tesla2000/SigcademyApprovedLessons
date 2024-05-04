import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What are some of the tools mentioned in the video for working with file modes and permissions?', 'How are mode bits represented on the file system?', "What does the 'chmod 750' command do in terms of file permissions?", 'What is the purpose of the group permission in Linux file permissions?', "How can the speaker change the group of a file in Linux using the 'chgrp' command?", "What is the significance of the 'read', 'write', and 'execute' permissions in Linux file permissions?", "Why is it important to be cautious when setting file permissions to allow 'write' access for 'other' users in Linux?", "What is the purpose of the 'umask' command in Linux file permissions?", 'What is the common umask value mentioned in the text?', 'What happens when umask is set to 000?', 'What happens when umask is set to 002?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What are some of the tools mentioned in the video for working with file modes and permissions?', 'How are mode bits represented on the file system?', "What does the 'chmod 750' command do in terms of file permissions?", 'What is the purpose of the group permission in Linux file permissions?', "How can the speaker change the group of a file in Linux using the 'chgrp' command?", "What is the significance of the 'read', 'write', and 'execute' permissions in Linux file permissions?", "Why is it important to be cautious when setting file permissions to allow 'write' access for 'other' users in Linux?", "What is the purpose of the 'umask' command in Linux file permissions?", 'What is the common umask value mentioned in the text?', 'What happens when umask is set to 000?', 'What happens when umask is set to 002?'], ["The tools mentioned in the video for working with file modes and permissions are 'touch', 'makedir', 'ls -al', 'chmod', and 'umask'.", 'Mode bits are represented on the file system using a series of read, write, and execute permissions for the owner, group, and others. Each triplet of permissions represents the owner, group, and others, respectively.', "The 'chmod 750' command sets the file permissions to allow the owner to read, write, and execute the file (7), the group to read and execute the file (5), and others to have no permissions (0).", 'The group permission in Linux file permissions determines which users in a specific group can access and modify a file. It allows users who are part of the same group as the file to have specific permissions on that file.', "You can change the group of a file in Linux using the 'chgrp' command followed by the new group name and the file name. For example, 'sudo chgrp pc_runner file.txt' will change the group of 'file.txt' to 'pc_runner'.", "The 'read' permission allows a user to view the contents of a file, the 'write' permission allows a user to modify the contents of a file, and the 'execute' permission allows a user to run the file as a program. These permissions can be set for the owner of the file, the group, and other users.", "It is important to be cautious when setting file permissions to allow 'write' access for 'other' users in Linux because it means that any user on the system can modify the file. This can lead to security risks and unauthorized changes to important files.", "The 'umask' command in Linux file permissions is used to set default permissions for newly created files. It specifies which permission bits should not be set when a new file is created. The umask value is subtracted from the default permissions to determine the actual permissions of the new file.", '002', 'It gives write permission to other users.', 'It leaves the write bit and does not have the write bit for others.']))
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
