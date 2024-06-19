import web
import time


def read_file_lines(file_path):
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            driver = web.create_driver()
            line = line.strip()
            web.download(driver, line)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    time.sleep(5)

# Example usage


def main():
    pass


if __name__ == "__main__":
    file_path = '/Users/ryanroth/Desktop/DJ Converter/djConverter/test.txt'
    read_file_lines(file_path)