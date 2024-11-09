import os
from .traffic_attributes import TrafficAttr


def get_tsv_with_header(input_file: str, output_path: str | None = None) -> str:
    '''
    tsvファイルにヘッダーを追加して保存する
    Args:
        input_file (str): ヘッダーを追加する元のTSVファイルのパス。
        output_path (str | None): 出力ファイルのパス。Noneの場合は、入力ファイルと同じディレクトリに 'with_header' ディレクトリを作成し、その中に保存。

    Returns:
        str: ヘッダーが追加された出力ファイルのパス。
    '''
    if output_path is None:
        output_path = os.path.join(os.path.dirname(input_file), 'with_header', os.path.basename(input_file))

    # 既にヘッダーが付与されたファイルが存在する場合はそのファイルパスを返す
    if os.path.exists(output_path):
        return output_path

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    header = TrafficAttr.get_attribute_name_list()

    with open(input_file, 'r') as infile, open(output_path, 'w') as outfile:
        outfile.write('\t'.join(header) + '\n')
        outfile.write(infile.read())

    return output_path


def main():
    print('ヘッダーを挿入するTSVファイルのパスを入力してください...')
    input_file = input()
    path = get_tsv_with_header(input_file)
    print(f'Saved {path}')


if __name__ == '__main__':
    main()
