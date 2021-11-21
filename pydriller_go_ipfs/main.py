from gettext import install
from pydriller import Repository
from github import Github



g = Github("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")

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


#  Complexity of the repo
for commit in Repository('../go-ipfs', from_tag=start_tag, to_tag=end_tag).traverse_commits():
    for m in commit.modified_files:
        print(
            "Author {}".format(commit.author.name),
            " modified {}".format(m.filename),
            " with a change type of {}".format(m.change_type.name),
            " and the complexity is {}".format(m.dmm_unit_complexity),
            " and the lines of code are {}".format(m.nloc),
            " and the methods of the code {}".format(m.methods),
        )


