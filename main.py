from ast import main
import re


# Sample Resume
resume_text = """
Hamrin
Python Developer

Skills:
Python, FastAPI, SQL, Machine Learning

Education:
Bachelor's Degree in Computer Science.

Experience:
Developed REST APIs using FastAPI.
Worked with SQL databases and Python programming.
Interested in Artificial Intelligence and Natural Language Processing.
"""


# STEP 1: Document Ingestion
def ingest_resume(text):
    return text.strip()


# STEP 2: Fixed-Size Chunking
def fixed_size_chunking(text, chunk_size=100):
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


# STEP 3: Sentence-Based Chunking
def sentence_based_chunking(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [sentence for sentence in sentences if sentence]


# STEP 4: Overlapping Chunking
def overlapping_chunking(text, chunk_size=100, overlap=20):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start = end - overlap

    return chunks


# STEP 5: Search Relevant Resume Information
def search_resume(chunks, query):
    results = []

    for chunk in chunks:
        if query.lower() in chunk.lower():
            results.append(chunk.strip())

    return results


# Main Program
if __name__ == "__main__":
    document = ingest_resume(resume_text)

    fixed_chunks = fixed_size_chunking(document)
    sentence_chunks = sentence_based_chunking(document)
    overlapping_chunks = overlapping_chunking(document)

    query = input("Enter a skill or keyword to search: ")

    print("\n========== AI RESUME FINDER ==========")
    print("Search Query:", query)

    strategies = {
        "Fixed-Size Chunking": fixed_chunks,
        "Sentence-Based Chunking": sentence_chunks,
        "Overlapping Chunking": overlapping_chunks,
    }

    print("\n========== RETRIEVAL COMPARISON ==========")
    print(f"{'Strategy':<25} {'Total Chunks':<15} {'Matches':<10}")
    print("-" * 50)

    for name, chunks in strategies.items():
        results = search_resume(chunks, query)

        print(f"{name:<25} {len(chunks):<15} {len(results):<10}")

        print(f"\n--- {name} ---")

        if results:
            for result in results:
                print("Result:", result)
        else:
            print("No matching information found.")



