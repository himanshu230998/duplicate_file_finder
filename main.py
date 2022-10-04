import os
import squence_matcher
import utils


processing_steps = set()
character_string = ""


github_repo_input = input("Enter your github Repository \n").strip()
source_file_input = input("Enter your github source file \n").strip()

is_file_to_be_preprocessed = input("Do you want to preprocess files. Enter Y/N (Default = N) \n").upper()

if is_file_to_be_preprocessed == 'Y':
    processing_string = input("Enter the processing options. \n 1. keep only alphabet \n 2. lower the alphabets \n 3. replace character \n")
    if '1' in processing_string:
        processing_steps.add(1)
    if '2' in processing_string:
        processing_steps.add(2)
    if '3' in processing_string:
        processing_steps.add(3)
        character_string = input("Enter all the character string to be removed \n")
elif is_file_to_be_preprocessed!='N':
    print("wrong input (only Y/N)")
    is_file_to_be_preprocessed = 'N'

github_repo = github_repo_input
source_file = source_file_input

print("Please wait ... ")

# github_repo = r"C:\Users\hs230\AndroidStudioProjects\Udacity_Android_Training_Material_App"
# source_file = r"C:\Users\hs230\AndroidStudioProjects\Udacity_Android_Training_Material_App\AndroidTrivia\app\src\main\AndroidManifest.xml"
with open(source_file, 'r') as file:
    source_file_content = file.read()
    if is_file_to_be_preprocessed == 'Y':
        source_file_content = utils.preprocessing_operation(source_file_content, processing_steps, character_string)


def breadth_first_file_scan(root) :
    dirs = [root]
    # while we has directories to scan
    while len(dirs) :
        nextDirs = []
        for parent in dirs :
            # scan each dir
            for file in os.listdir(parent):
                # if there is a directory, then save for next itertion
                file_path = os.path.join(parent, file)
                if os.path.isdir(file_path) :
                    nextDirs.append(file_path)
                else :
                    yield file_path
        dirs = nextDirs


all_file_list = []
def walk_bfs(path):
    for file in breadth_first_file_scan(path) :
        all_file_list.append(file)
walk_bfs(github_repo)

if len(all_file_list)==0:
    print("There is no file in this directory")
else:
    ans = []
    for file in all_file_list:
        similarity_score = squence_matcher.sequence_matcher_similarity(file, source_file_content, is_file_to_be_preprocessed, processing_steps, character_string)
        ans.append([file, similarity_score])
    ans.sort(key = lambda x: -x[1])

    if ans[0][1]>50:
        for x,y in ans:
            if y>50:
                print("File "+ x+ " has similarity score " + str(y) )
            else:
                break
    else:
        print("There is no file whose similarity is more than 50%")



