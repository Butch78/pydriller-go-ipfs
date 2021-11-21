
from pydriller import Repository


# Number of Commits
# print(len([commit for commit in Repository('https://github.com/ishepard/pydriller').traverse_commits()]))

# Unique Authors using a Set
# authors = set([commit.author.email for commit in Repository('https://github.com/ishepard/pydriller').traverse_commits()])
# print(authors)


# Unique File using a Set
# modilfy_files = set([commit.modifications.new_path for commit in Repository('https://github.com/ishepard/pydriller').traverse_commits()])
# print(modilfy_files)

mods = set()

for commit in Repository('https://github.com/ishepard/pydriller').traverse_commits():
    for mod in commit.modifications:
        new_path = mod.new_path
        mods.add(new_path)

print(mods)


# for commit in Repository('https://github.com/ishepard/pydriller').traverse_commits():
#     # print(commit.hash)
#     # print(commit.msg)
#     # print(commit.author.name)

#     authors.append(commit.author.name)
#     authors

#     for file in commit.modified_files:
#         print(file.filename, ' has changed')

