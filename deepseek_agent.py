import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

class ClaudeAgent:
    def __init__(self):
        self.llm = ChatAnthropic(
            model="claude-3-sonnet-20240229",  # or "claude-3-sonnet-20240229"
            temperature=0.7,
            max_tokens=1024,
            anthropic_api_key=os.getenv("sk-10a0cffbb30e42f0a1a18403dd9700e9")  # Set your API key in environment
        )
        self.memory = ConversationBufferMemory()
        self.chain = self._create_chain()

    def _create_chain(self):
        template = """You are a helpful AI assistant. Answer in detail.
        
        History:
        {history}
        Human: {input}
        Assistant:"""
        
        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=template
        )
        
        return ConversationChain(
            llm=self.llm,
            prompt=prompt,
            memory=self.memory,
            verbose=True
        )

    def chat(self, message):
        return self.chain.run(input=message)