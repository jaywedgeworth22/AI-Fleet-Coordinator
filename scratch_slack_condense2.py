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

parts = re.split(r'=== Message from ', msgs)
blocks = []
for p in parts[1:]:
    blocks.append('=== Message from ' + p)

NOISE_MARKERS = ['CURSOR-BUGBOT', 'CURSOR-AUTOMATION', 'Incident resolved', 'has joined the channel',
                  'automation is enabled in this channel']

out_lines = []
noise_count = 0
kept = 0
for b in blocks:
    m_from = re.search(r'=== Message from (.*?) at (.*?) ===', b)
    m_ts = re.search(r'Message TS: ([0-9.]+)', b)
    sender = m_from.group(1) if m_from else '?'
    when = m_from.group(2) if m_from else '?'
    ts = m_ts.group(1) if m_ts else '?'
    body_match = re.split(r'Message TS: [0-9.]+\s*', b, maxsplit=1)
    body = body_match[1] if len(body_match) > 1 else b
    body = body.strip()

    if any(n in body for n in NOISE_MARKERS):
        noise_count += 1
        continue
    kept += 1
    thread_info = ''
    tm = re.search(r'(\d+) repl(y|ies)', body)
    if tm:
        thread_info = f' [THREAD:{tm.group(0)}]'
    firstline = body[:400].replace('\n', ' | ')
    out_lines.append(f'TS={ts} {when} FROM={sender[:45]}{thread_info}\n     {firstline}')

print(f'TOTAL BLOCKS: {len(blocks)}  KEPT: {kept}  NOISE_FILTERED: {noise_count}')
print(f'PAGINATION: {pag}')
print('---')
print('\n'.join(out_lines))
