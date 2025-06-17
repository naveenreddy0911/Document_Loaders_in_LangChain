from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser

url=["https://www.amazon.in/Chetak-Bajaj-Electric-Scooter-charger/dp/B0DQL1MQR1/?_encoding=UTF8&pd_rd_w=uelGt&content-id=amzn1.sym.c85c0650-724c-4a64-8a0b-9f7c03c0cd7d&pf_rd_p=c85c0650-724c-4a64-8a0b-9f7c03c0cd7d&pf_rd_r=KB56Y0PJ0TKQJ5E40F3Z&pd_rd_wg=59jjS&pd_rd_r=aebf2a80-4047-4dc6-84dc-37d72cb2337b&ref_=pd_hp_d_btf_ls_gwc_pc_en4_&th=1","https://google.com"]

loader=WebBaseLoader(url)

docs=loader.load()

print(docs)