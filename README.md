# sterling-security-gen-ai
This Python Script prepares an input file to be ingested by an LLM trained model on Cybersecurity.
Splits a large text file into smaller chunks.

    Parameters:
    - input_folder: Path to the folder containing the input file.
    - output_folder: Path to the folder where output chunks will be saved.
    - input_filename: Name of the input text file.
    - chunk_size: Size of each chunk in bytes (default is 5 MB).