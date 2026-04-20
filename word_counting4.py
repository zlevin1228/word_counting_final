# Word Counting Project INST126
# Import + Setup
import os
# Processing Files and Completing Word Counting Results WITH A FUNCTION
from word_utils import count_words_in_files

# Gets Directory
current_dir = os.getcwd()
print("Current Working Directory:\n" + current_dir)



# Gets File And/Or Directory

while True:
        path = input("\nEnter a directory path or file name: ")
        # File is opened and contents are read
        if path == "":
            print("Error: File/path name cannot be blank.")
            continue
        if os.path.isfile(path):
            file_list = [path]
            break
        elif os.path.isdir(path):
            file_list = []
            for f in os.listdir(path):
                entire_path = os.path.join(path, f)
                if os.path.isfile(entire_path):
                    file_list.append(entire_path)
            if not file_list:
                print("Error: There were no files found in the directory.")
                continue
            break
        else: 
            print("Error: File or directory does not exist. Please try again.")


# Get User Input
word = input("Enter the word to count: ")

# Decides Whether Word Should Be Case-Sensitive or Case-Insensitive
choice = input("Should the search be case sensitive/insensitive? (yes/no): ").lower()

if choice == "yes":
    case_sensitive = True
    sensitivity = "(Case-Sensitive)"
elif choice == "no":
    case_sensitive = False
    sensitivity = "(Case-Insensitive)"
else:
   print("Invalid choice. The default is Case-Insensitive.")
   case_sensitive = False
   sensitivity = "(Case-Insensitive)"

# Printing the Results
results, total_count = count_words_in_files(file_list, word, case_sensitive)

for file_path in results:
    print(f"'{word}' {sensitivity} found {results[file_path]} times in: {file_path}")     

if len(file_list) > 1:
    print("\nTotal occurrences across all files: " + str(total_count))

# Saving the Results to Another File
with open("wordcount_results.txt", "w") as output_file:
    for file_path in results:
        output_file.write(f"'{word}' {sensitivity} found {results[file_path]} times in: {file_path}\n")
    if len(file_list) > 1:
        output_file.write("\nTotal occurrences across all files: " + str(total_count))

# Display Results/Final Message
print("\nResults saved to wordcount_results.txt")
