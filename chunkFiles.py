import os

def chunk_large_text_file(input_folder, output_folder, input_filename, chunk_size=4.8*1024*1024):
    """
    Splits a large text file into smaller chunks.

    Parameters:
    - input_folder: Path to the folder containing the input file.
    - output_folder: Path to the folder where output chunks will be saved.
    - input_filename: Name of the input text file.
    - chunk_size: Size of each chunk in bytes (default is 5 MB).
    """
    input_folder = 'input'
    output_folder = 'output'

    input_filepath = os.path.join(input_folder, input_filename)

    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_number = 1
    current_output_size = 0

    # Prepare the first output file
    output_filename = f"chunk_{output_file_number}.txt"
    output_filepath = os.path.join(output_folder, output_filename)
    output_file = open(output_filepath, 'w', encoding='utf-8')

    with open(input_filepath, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line_size = len(line.encode('utf-8'))
            # Check if adding the line would exceed the chunk size
            if current_output_size + line_size > chunk_size:
                output_file.close()
                output_file_number += 1
                current_output_size = 0
                # Prepare a new output file
                output_filename = f"chunk_{output_file_number}.txt"
                output_filepath = os.path.join(output_folder, output_filename)
                output_file = open(output_filepath, 'w', encoding='utf-8')

            output_file.write(line)
            current_output_size += line_size

    output_file.close()
    print(f"File has been split into {output_file_number} chunks.")

# Example usage:
input_folder = ''
output_folder = 'output'
#input_filename = 'airspace.txt'
input_filename = 'secureproxy-SFTP_MFA_Netmap.SFTP_MFA_InboundNode.txt'
chunk_large_text_file(input_folder, output_folder, input_filename)
