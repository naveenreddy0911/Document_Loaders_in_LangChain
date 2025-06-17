from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template='Summarize the following:\n{pdf}',
    input_variables=['pdf']
)

parser=StrOutputParser()

loader=DirectoryLoader(
    path="path/to/directory",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.load()

chain=prompt|model|parser

result=chain.invoke({'pdf':docs})

print(result)