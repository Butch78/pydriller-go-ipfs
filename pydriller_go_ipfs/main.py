from pydriller import Repository
from github import Github
import json
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional



g = Github("ADD_YOUR_OWN_API_KEY")

# STEP 1: Go to https://github.com/ipfs/go-ipfs


# STEP 2: Decide on granularity of the project
# Files for now as we can identify the modified files easily



# STEP 3:
#  List of all the Entities of the repository:
# repo = g.get_repo("ipfs/go-ipfs")
# contents = repo.get_contents("")
# while contents:
#     file_content = contents.pop(0)
#     if file_content.type == "dir":
#         contents.extend(repo.get_contents(file_content.path))
#     else:
#         print(file_content)

# Modified files refrence 
#  https://pydriller.readthedocs.io/en/latest/modifiedfile.html


# STEP 4: 
# Decide on the complexity of the project you want to measure
# Cyclomatic complexity has been implemented in pydriller it relies on Lizard: https://github.com/terryyin/lizard
# How is it used in pydriller: https://pydriller.readthedocs.io/en/latest/deltamaintainability.html
# It measures 
#  - the number of functions
#  - the nloc (number of lines of code without comments)
#  - token count of the functions
#  - parameter count of the functions


# STEP 5:
# Timeframe 
start_tag =  'v0.5.0'
end_tag = 'v0.10.0'
# Might tweak the timeframe to be more specific if needed
# Futher explanation will be needed to be added

# STEP 6:
# Measure the complexity of the project and number of changes 
# Merge this information to identify the hot spots of the project



class Modified_Files(BaseModel):
    Files: dict = None


class File(BaseModel):
    file_name: str
    commits: Optional[list]


class Commit(BaseModel):
    commit_id: Optional[str]
    nloc: Optional[int]
    complexity: Optional[int]


commit_count = 0
number_of_changes = 0
# Empty list to store the changes

all_files = Modified_Files(Files={})

for commit in Repository('../go-ipfs', from_tag=start_tag, to_tag=end_tag).traverse_commits():
    commit_count += 1

    for m in commit.modified_files:
        if m.filename.endswith(".go"):
            number_of_changes += 1

            #  Check there isn't a file with the same name in the dictionary already
            if m.filename in all_files.Files:
                #  If there is, add the commit to the list of commits
                if m.complexity is not None or m.nloc is not None:
                    all_files.Files[m.filename].commits.append(Commit(commit_id=commit.hash, nloc=m.nloc, complexity=m.complexity))
            else:
                #  If not, create a new file with the commit

                all_files.Files[m.filename] = File(file_name=m.filename, commits=[Commit(commit_id=commit.hash, nloc=m.nloc, complexity=m.complexity)])

        
            
#  Export Files Dictionary to a json file

print_files = jsonable_encoder(all_files)

with open('files.json', 'w') as outfile:
    json.dump(print_files, outfile)

# Import Dictionary string from the json file



with open('files.json') as json_file:
    Files = json.load(json_file)
    modified_Files =Modified_Files(**Files)






# STEP 7: Visualization of the Hot Spots



# STEP 8: Analysis of 6 of the Hot Spots
# a) Complexity trend analysis
# b) Manaul analysis of the entity names and content
