import os

# TODO: overload


def get_tsv_with_header(input_file: str, output_dir: str = None, output_filename: str = None) -> str:
    if output_dir is None:
        output_dir = os.path.dirname(input_file) + r'\with_header'
    if output_filename is None:
        output_filename = os.path.basename(input_file)
    output_file = os.path.join(output_dir, output_filename)

    # 既にヘッダーが付与されたファイルが存在する場合はそのファイルパスを返す
    if os.path.exists(output_file):
        return output_file

    os.makedirs(output_dir, exist_ok=True)

    header = [
        'DURATION', 'SERVICE', 'SOURCE_BYTES', 'DESTINATION_BYTES', 'COUNT',
        'SAME_SRV_RATE', 'SERROR_RATE', 'SRV_SERROR_RATE', 'DST_HOST_COUNT',
        'DST_HOST_SRV_COUNT', 'DST_HOST_SAME_SRC_PORT_RATE', 'DST_HOST_SERROR_RATE',
        'DST_HOST_SRV_SERROR_RATE', 'FLAG', 'IDS_DETECTION', 'MALWARE_DETECTION',
        'ASHULA_DETECTION', 'LABEL', 'SOURCE_IP_ADDRESS', 'SOURCE_PORT_NUMBER',
        'DESTINATION_IP_ADDRESS', 'DESTINATION_PORT_NUMBER', 'START_TIME', 'DURATION_DUPLICATE'
    ]

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write('\t'.join(header) + '\n')
        outfile.write(infile.read())

    return output_file
