from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_text(documents):
    """
    This function takes a list of documents, and splits them into
    chunks of text suitable for embedding.

    The splitting is done by the RecursiveCharacterTextSplitter, which
    splits the text into chunks of size 700 characters, with an overlap
    of 80 characters between each chunk.

    Args:
        documents (list): A list of documents, where each document is a
            string of text.

    Returns:
        list: A list of chunks of text, where each chunk is a string of
            text.
    """

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=80)
    chunkedText = text_splitter.split_documents(documents)
    return chunkedText