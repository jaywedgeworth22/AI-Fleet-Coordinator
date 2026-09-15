import json, re, sys

path = sys.argv[1]
with open(path) as f:
    data = json.load(f)

results_str = data.get('results', '')
pag = data.get('pagination_info', '')

# Split on "### Result N of M"
chunks = re.split(r'### Result \d+ of \d+', results_str)
header = chunks[0]
print(header.strip()[:300])
print('PAGINATION:', pag)
print('=====')

for c in chunks[1:]:
    # Extract Channel, From, Time, Text (before "Context before")
    channel_m = re.search(r'Channel: (.*)', c)
    from_m = re.search(r'From: (.*)', c)
    time_m = re.search(r'Time: (.*)', c)
    text_m = re.search(r'Text:\s*(.*?)(?:\nContext before:|\nContext after:|\Z)', c, re.DOTALL)
    channel = channel_m.group(1).strip() if channel_m else '?'
    frm = from_m.group(1).strip() if from_m else '?'
    time = time_m.group(1).strip() if time_m else '?'
    text = text_m.group(1).strip() if text_m else ''
    text = text.replace('\n', ' | ')[:500]
    print(f'[{time}] {frm} in {channel}')
    print(f'  {text}')
    print()
