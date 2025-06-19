# loaders in LangChain

This repository demonstrates how to use **loaders** in LangChain to efficiently and uniformly load different types of documents from CSVs and PDFs to text files and web pages into your pipeline for further processing.
Loaders streamline the process of retrieving and transforming documents into a format that LangChain components can work with, regardless of their original format or storage location.

## 📄 File Descriptions

- `CSVLoader.py`  Shows how to **load CSV files** into LangChain documents.

- `DirectoryLoader.py`  Loads all files from a directory at once, useful for large batches of documents.

- `PyPDFLoader.py`  Initializes a PDF loader to extract text from PDF files.

- `TextLoader.py`  Loads **simple text files** (like `.txt`) into LangChain documents.

- `WebBaseLoader.py`  Loads content directly from a **web page's URL**.

## Environment Variables
To use this project, you need to set API keys in a `.env` file in the root directory.

### 📄 .env file format

```env
OPENAI_API_KEY="your_openai_key"
ANTHROPIC_API_KEY="your_anthropic_key"
GOOGLE_API_KEY="your_google_key"
HUGGINGFACEHUB_API_KEY="your_huggingfacehub_key"
```

### Dont have closed-source API key ? 
Refer to the repo [**Models_in_LangChain**](https://github.com/naveenreddy0911/Models_in_LangChain) for using open-sourced Hugging Face chat models (via API or locally).
