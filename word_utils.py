def count_words_in_files(file_list, word, case_sensitive):
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