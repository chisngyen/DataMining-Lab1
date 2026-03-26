"""Convert py-percent script to ipynb. Usage: python convert.py input.py"""
import json, re, sys

path = sys.argv[1]
out_path = path.replace('.py', '.ipynb')

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

parts = re.split(r'^# %%(.*)$', content, flags=re.MULTILINE)
cells = []
i = 0
while i < len(parts):
    if i == 0:
        text = parts[0].strip()
        if text:
            cells.append({'cell_type': 'code', 'source': [l+'\n' for l in text.split('\n')], 'metadata': {}, 'outputs': [], 'execution_count': None})
        i += 1
    else:
        marker = parts[i].strip()
        code = parts[i+1] if i+1 < len(parts) else ''
        lines = code.split('\n')
        while lines and lines[0].strip() == '': lines = lines[1:]
        while lines and lines[-1].strip() == '': lines = lines[:-1]
        source = [l+'\n' for l in lines[:-1]] + [lines[-1]] if lines else []
        if '[markdown]' in marker:
            md = []
            for l in source:
                lc = l.rstrip('\n')
                if lc.startswith('# '): md.append(lc[2:]+'\n')
                elif lc == '#': md.append('\n')
                else: md.append(l)
            if md: md[-1] = md[-1].rstrip('\n')
            cells.append({'cell_type': 'markdown', 'source': md, 'metadata': {}})
        else:
            cells.append({'cell_type': 'code', 'source': source, 'metadata': {}, 'outputs': [], 'execution_count': None})
        i += 2

nb = {
    'nbformat': 4, 'nbformat_minor': 5,
    'metadata': {
        'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
        'language_info': {'name': 'python', 'version': '3.11.0'}
    },
    'cells': cells
}

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
print(f'OK: {out_path}')
