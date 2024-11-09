from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path):
    """
    Loads a PDF file and converts it into a list of documents.

    Args:
        file_path (str): Path to the PDF file

    Returns:
        list[Document]: List of documents, where each document is a text
            representation of a page from the PDF file
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents
