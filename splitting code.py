import os

def split_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        total_size = len(data)
        split_size = total_size // 2

        first_half = data[:split_size]
        second_half = data[split_size:]

        # write first half to new file
        with open(f"{file_path}.part1", 'w') as file1:
            file1.write(first_half)

        # write second half to new file
        with open(f"{file_path}.part2", 'w') as file2:
            file2.write(second_half)

if __name__ == '__main__':
    file_path = '/Users/san/Downloads/automatic_s3_uploader.py'
    split_file(file_path)
