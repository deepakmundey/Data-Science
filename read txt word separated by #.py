def display_words_with_separator():
    file=open('Practice Text Document.txt', 'r')
    lines=file.readlines()
    for line in file:
        words = line.split()
        print("#".join(words))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
display_words_with_separator():
