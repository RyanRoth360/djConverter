import downloader
import argparse

def read_file_lines(file_path):
    driver = downloader.create_driver()
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            downloader.download(driver, line)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Youtube to MP3 mass converter')
    parser.add_argument('-f', '--file', default="links.txt", type=str, help='Path to the input file')
    parser.add_argument('-o', '--output', default="current_dir", type=str, help='Path to the input file')
    args = parser.parse_args()
    read_file_lines(args.file)