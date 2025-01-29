import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.llms import DeepSeek

class DeepSeekAgent:
    def __init__(self):
        self.llm = DeepSeek(
            base_url="https://api.deepseek.com/v1",
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            model="deepseek-chat",
            temperature=0.7
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