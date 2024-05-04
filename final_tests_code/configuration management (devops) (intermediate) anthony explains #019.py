import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is configuration management?', 'What is Puppet?', 'How does configuration management software work?', 'What is the purpose of using configuration management software?', 'What is the name of the package that needs to be ensured at the latest version?', 'What configuration management software is being used in this setup?', "What is the name of the class where the package 'neo fetch' is being added?", 'What configuration management software is being discussed in the text?', 'Why did the author choose Puppet over other configuration management software?', 'What is the benefit of using a code formatter in Puppet?', 'What type of puppet setup do the speaker have?', 'How is your puppet setup configured in a masterless setup?', 'What is the purpose of the run puppet script in your setup?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is configuration management?', 'What is Puppet?', 'How does configuration management software work?', 'What is the purpose of using configuration management software?', 'What is the name of the package that needs to be ensured at the latest version?', 'What configuration management software is being used in this setup?', "What is the name of the class where the package 'neo fetch' is being added?", 'What configuration management software is being discussed in the text?', 'Why did the author choose Puppet over other configuration management software?', 'What is the benefit of using a code formatter in Puppet?', 'What type of puppet setup do the speaker have?', 'How is your puppet setup configured in a masterless setup?', 'What is the purpose of the run puppet script in your setup?'], ['Configuration management is a process of managing and maintaining the software and settings on a computer system to ensure it is in a desired state.', 'Puppet is a configuration management software written in Ruby that allows users to define the desired state of their systems using code and apply that configuration to the systems.', 'Configuration management software takes a set of code that describes the desired state of a system, such as installed packages and file configurations, and applies that code to the system to ensure it matches the specified state.', 'The purpose of using configuration management software is to automate the process of setting up and maintaining computer systems, ensuring consistency and efficiency in managing software and configurations across multiple machines.', 'neo fetch', 'Puppet', 'packages::neo_fetch', 'Puppet', "The author chose Puppet because of their familiarity with it from previous experience, as well as Puppet's support for linters and code formatters, which allows for static checks and code formatting.", 'The code formatter in Puppet allows for automatic formatting of code, reducing the need to manually adjust whitespace and ensuring consistent styling across manifests.', 'I have a headless setup, which is different from the typical setup in larger organizations where there is a puppet master controlling every node in the cluster.', 'My puppet setup is configured by a run puppet script written in Python. This script installs puppet and puppet modules in the home directory, sets up environment variables, and invokes puppet against site.pp.', 'The run puppet script installs puppet, puppet modules, and sets up environment variables to manage configurations in a masterless puppet setup.']))
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
