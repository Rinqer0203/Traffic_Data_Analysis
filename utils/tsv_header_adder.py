import os
from .traffic_attributes import TrafficAttr


def get_tsv_with_header(input_file: str, output_dir: str | None = None, output_filename: str | None = None) -> str:
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(input_file), 'with_header')
    if output_filename is None:
        output_filename = os.path.basename(input_file)
    output_file = os.path.join(output_dir, output_filename)

    # 既にヘッダーが付与されたファイルが存在する場合はそのファイルパスを返す
    if os.path.exists(output_file):
        return output_file

    os.makedirs(output_dir, exist_ok=True)
    header = TrafficAttr.get_attribute_name_list()

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write('\t'.join(header) + '\n')
        outfile.write(infile.read())

    return output_file


def main():
    print('ヘッダーを挿入するTSVファイルのパスを入力してください...')
    input_file = input()
    path = get_tsv_with_header(input_file)
    print(f'Saved {path}')


if __name__ == '__main__':
    main()
