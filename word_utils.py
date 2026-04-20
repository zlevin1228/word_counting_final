def count_words_in_files(file_list, word, case_sensitive):
    """
    Counts occurrences of a given word across multiple text files.

    Parameters:
        file_list (list): List of file paths to search through
        word (str): Word to search for in the files
        case_sensitive (bool): If True, matches exact case; if False, ignores case

    Returns:
        tuple: (dictionary with file-wise counts, total count across all files)
    """
    total_count = 0
    results = {}

    for file_path in file_list:
        try:
            with open(file_path, mode="r") as file_pipeline:
                contents = file_pipeline.read()

                if not case_sensitive:
                    contents = contents.casefold()
                    searched_word = word.casefold()
                else:
                    searched_word = word

                count = contents.count(searched_word)
                total_count += count
                results[file_path] = count

        except FileNotFoundError:
            results[file_path] = "ERROR: File not found"

    return results, total_count

# ----------------------------
# TEST CASES FOR FUNCTION

# Test 1: Basic case (single file, case-sensitive)
# files = ["test1.txt"]
# word = "Hello"
# case_sensitive = True
# print(count_words_in_files(files, word, case_sensitive))


# Test 2: Case-insensitive search
# files = ["test1.txt"]
# word = "hello"
# case_sensitive = False
# print(count_words_in_files(files, word, case_sensitive))


# Test 3: File not found handling
# files = ["fakefile.txt"]
# word = "test"
# case_sensitive = True
# print(count_words_in_files(files, word, case_sensitive))