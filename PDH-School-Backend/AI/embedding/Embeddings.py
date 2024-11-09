import logging
from docLoader import load_pdf
from docSplitter import split_text
from vector_db.PineConeDB import retriever
logging.basicConfig(level=logging.INFO)

def embedding_function(file_path):
    """
    Embeds the contents of a PDF file into the retriever.

    This function takes a file path to a PDF file, loads it, splits it into individual pages,
    and embeds the text content of each page into the retriever.

    Args:
        file_path (str): Path to the PDF file

    Returns:
        None
    """
    documents = load_pdf(file_path)
    chunkedText = split_text(documents)
    
    texts = [doc.page_content for doc in chunkedText]
    
    if texts:
        retriever.add_texts(texts)
        logging.info("Texts successfully added to the retriever.")
    else:
        logging.error("No text content found in the documents.")
