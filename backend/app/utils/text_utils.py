import re


def normalize_whitespace(text: str) -> str:
    #replace tabs with single space
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()

def remove_empty_lines(text: str) -> str:
    #removing empty lines
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)

def merge_broken_lines(text: str) -> str:
    #fixing broken lines
    return re.sub(r"(?<![.!?])\n(?!\n)", " ", text)

def remove_page_numbers(text: str) -> str:
    text = re.sub(r"\bPage\s+\d+\b", "", text, flags=re.IGNORECASE)
    return text

def clean_text(text: str) -> str:
    #apply all cleaning text
    text = normalize_whitespace(text)
    text = remove_empty_lines(text)
    text = merge_broken_lines(text)
    text = remove_page_numbers(text)

    return text.strip()