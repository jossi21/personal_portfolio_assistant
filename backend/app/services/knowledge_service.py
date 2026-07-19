from pathlib import Path

# define the path of my personal data 
KNOWLEDGE_PATH = Path("app/knowledge")

# define the function which read files inside that define data
def load_knowledge()-> str:
    knowledge = ""

    for file in KNOWLEDGE_PATH.glob("*.md"):
        knowledge += file.read_text()

    return knowledge


if __name__ == "__main__":
    print(load_knowledge())