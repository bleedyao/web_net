import json

with open('./articles.json', 'r') as f:
    dict = json.load(f)

with open('./readme.md', 'w') as f:
    for i, val in enumerate(dict['data']['list']):
        f.write('- [ ] ' + val['article_title'] + '\n')
