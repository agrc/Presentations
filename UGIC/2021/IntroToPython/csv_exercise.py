import csv
from pathlib import Path


def build_output_path(csv_path):

    working_dir = csv_path.parent
    output_dir = working_dir / 'output'
    output_dir.mkdir()
    out_path = output_dir / 'outfile.csv'

    return out_path


def read_csv(csv_path):
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

        return data


def write_csv(data, out_path):
    with open(out_path, 'wt', newline='', encoding='utf-8') as out_file:
        writer = csv.DictWriter(out_file, ['NAME', 'SHORTDESC', 'FIPS'],
                                extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)


def main():
    csv_path = Path(r'c:\temp\ugic\Utah_Municipal_Boundaries.csv')
    out_path = build_output_path(csv_path)
    data = read_csv(csv_path)
    write_csv(data, out_path)


if __name__ == '__main__':
    main()
