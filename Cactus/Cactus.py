import re
from collections import Counter

def extract_numbers(text):
    """Extract all numbers from the text."""
    return [int(num) for num in re.findall(r'\b\d+\b', text)]

def find_number_positions(text):
    """Find positions of all numbers in the text."""
    return [match.start() for match in re.finditer(r'\b\d+\b', text)]

def detect_anagrams(words):
    """Detect anagrams from a list of words."""
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in word_dict:
            word_dict[sorted_word] = []
        word_dict[sorted_word].append(word)
    # Filter out anagrams with single words or numbers
    return {word: anagram_list for word, anagram_list in word_dict.items() if len(anagram_list) > 1 and not word.isdigit()}

def detect_fibonacci(numbers):
    """Detect Fibonacci sequences from a list of numbers."""
    if not numbers:
        return []
    
    fib = [0, 1]
    while fib[-1] < max(numbers):
        fib.append(fib[-1] + fib[-2])
    
    return sorted(set(num for num in numbers if num in fib))

def detect_geometric(numbers):
    """Detect geometric sequences from a list of numbers."""
    if not numbers:
        return []
    
    numbers = sorted(set(numbers))
    geo_sequences = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            ratio = numbers[j] / numbers[i]
            if ratio == int(ratio):
                ratio = int(ratio)
                sequence = [numbers[i]]
                current = numbers[i]
                while True:
                    next_val = current * ratio
                    if next_val in numbers:
                        sequence.append(next_val)
                        current = next_val
                    else:
                        break
                if len(sequence) > 2:  # Filter out sequences with fewer than three elements
                    geo_sequences.add(tuple(sequence))
    
    return [list(seq) for seq in geo_sequences]

def detect_custom_sequences(numbers):
    """Detect custom sequences from a list of numbers."""
    if not numbers:
        return []
    
    custom_sequences = []
    
    # Triangular numbers sequence
    triangular_numbers = set()
    n = 1
    while (t := n * (n + 1) // 2) <= max(numbers):
        triangular_numbers.add(t)
        n += 1
    if triangular_numbers:
        custom_sequences.append(sorted(set(num for num in numbers if num in triangular_numbers)))
    
    # Square numbers sequence
    square_numbers = set()
    n = 1
    while (s := n * n) <= max(numbers):
        square_numbers.add(s)
        n += 1
    if square_numbers:
        custom_sequences.append(sorted(set(num for num in numbers if num in square_numbers)))
    
    return custom_sequences

def extract_keywords(text):
    """Extract and count specific keywords from the text."""
    keywords = ['python', 'great', 'libraries']
    word_list = re.findall(r'\b\w+\b', text.lower())
    keyword_counts = Counter(word for word in word_list if word in keywords)
    return keyword_counts

def write_results(file_path, numbers, positions, anagrams, fib_sequences, geo_sequences, custom_sequences, keyword_counts):
    """Write results to a text file."""
    with open(file_path, 'w') as f:
        f.write("Extracted Numbers: {}\n".format(numbers))
        f.write("Positions in Text: {}\n".format(positions))
        f.write("\nAnagrams:\n")
        for word, anagram_list in anagrams.items():
            f.write(f"{word}: {anagram_list}\n")
        
        f.write("\nGeometric Sequences:\n")
        for seq in geo_sequences:
            f.write(f"{seq}\n")
        
        f.write("\nFibonacci Sequences:\n")
        f.write(f"{fib_sequences}\n")
        
        f.write("\nCustom Sequences:\n")
        for seq in custom_sequences:
            f.write(f"{seq}\n")
        
        f.write("\nKeyword Counts:\n")
        for keyword, count in keyword_counts.items():
            f.write(f"{keyword}: {count}\n")

def write_html_results(file_path, numbers, positions, anagrams, fib_sequences, geo_sequences, custom_sequences, keyword_counts):
    """Write results to an HTML file."""
    with open(file_path, 'w') as f:
        f.write("<html><body>\n")
        f.write("<h1>Cactus Output</h1>\n")
        f.write("<h2>Extracted Numbers:</h2><p>{}</p>\n".format(numbers))
        f.write("<h2>Positions in Text:</h2><p>{}</p>\n".format(positions))
        f.write("<h2>Anagrams:</h2>\n")
        for word, anagram_list in anagrams.items():
            f.write(f"<p><strong>{word}:</strong> {anagram_list}</p>\n")
        
        f.write("<h2>Geometric Sequences:</h2>\n")
        for seq in geo_sequences:
            f.write(f"<p>{seq}</p>\n")
        
        f.write("<h2>Fibonacci Sequences:</h2>\n")
        f.write(f"<p>{fib_sequences}</p>\n")
        
        f.write("<h2>Custom Sequences:</h2>\n")
        for seq in custom_sequences:
            f.write(f"<p>{seq}</p>\n")
        
        f.write("<h2>Keyword Counts:</h2>\n")
        for keyword, count in keyword_counts.items():
            f.write(f"<p><strong>{keyword}:</strong> {count}</p>\n")
        
        f.write("</body></html>")

def main():
    file_path = input("Enter the path to the text file: ")
    
    with open(file_path, 'r') as file:
        text = file.read()
    
    numbers = extract_numbers(text)
    positions = find_number_positions(text)
    
    words = re.findall(r'\b\w+\b', text.lower())
    anagrams = detect_anagrams(words)
    
    fib_sequences = detect_fibonacci(numbers)
    geo_sequences = detect_geometric(numbers)
    custom_sequences = detect_custom_sequences(numbers)
    
    keyword_counts = extract_keywords(text)
    
    output_path = 'C:\\Users\\Kliea\\Documents\\Development\\Python\\Cactus\\output.txt'
    html_output_path = 'C:\\Users\\Kliea\\Documents\\Development\\Python\\Cactus\\output.html'
    
    write_results(output_path, numbers, positions, anagrams, fib_sequences, geo_sequences, custom_sequences, keyword_counts)
    write_html_results(html_output_path, numbers, positions, anagrams, fib_sequences, geo_sequences, custom_sequences, keyword_counts)
    
    print(f"Output saved to: {output_path}")
    print(f"HTML output saved to: {html_output_path}")

if __name__ == "__main__":
    main()
