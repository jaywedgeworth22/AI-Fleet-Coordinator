import json, re, sys

path = sys.argv[1]
with open(path) as f:
    raw = f.read()
try:
    data = json.loads(raw)
    msgs = data.get('messages', raw)
    pag = data.get('pagination_info', '')
except Exception:
    msgs = raw
    pag = ''

# Split into message blocks
parts = re.split(r'=== Message from ', msgs)
blocks = []
for p in parts[1:]:
    blocks.append('=== Message from ' + p)

KEYWORDS = ['FLEET', '->', 'Grok', 'RAG', 'rag', 'vector', 'Pinecone', 'pinecone',
            'embed', 'memory', 'Memory', 'handoff', 'Handoff', 'HANDOFF',
            'thread', 'claim', 'pickup', 'pick up', 'blocked', 'stuck',
            'duplicate', 'already did', 'someone else']

out_lines = []
for b in blocks:
    m_from = re.search(r'=== Message from (.*?) at (.*?) ===', b)
    m_ts = re.search(r'Message TS: ([0-9.]+)', b)
    sender = m_from.group(1) if m_from else '?'
    when = m_from.group(2) if m_from else '?'
    ts = m_ts.group(1) if m_ts else '?'
    # body = everything after the TS line
    body_match = re.split(r'Message TS: [0-9.]+\s*', b, maxsplit=1)
    body = body_match[1] if len(body_match) > 1 else b
    body = body.strip()
    flagged = any(k in body for k in KEYWORDS)
    thread_info = ''
    tm = re.search(r'(\d+) repl(y|ies)', body)
    if tm:
        thread_info = f' [THREAD:{tm.group(0)}]'
    marker = '**' if flagged else '  '
    firstline = body[:300].replace('\n', ' | ')
    out_lines.append(f'{marker} TS={ts} {when} FROM={sender[:40]}{thread_info}\n     {firstline}')

print(f'TOTAL BLOCKS: {len(blocks)}')
print(f'PAGINATION: {pag}')
print('---')
print('\n'.join(out_lines))
