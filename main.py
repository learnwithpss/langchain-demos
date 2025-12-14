import os

from dotenv import find_dotenv, load_dotenv

load_dotenv()


def main():
    # load_dotenv(find_dotenv())
    print("Hello from langchain-course!")
    print("OPENAI_API_KEY:", os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
