from pathlib import Path
import base64,json,re
root=Path(__file__).resolve().parents[1]
pages={p.stem:p.read_text() for p in sorted((root/'src/pages').glob('*.html'))}
data={k:base64.b64encode(v.encode()).decode() for k,v in pages.items()}
titles={k:re.search(r'<title>(.*?)</title>',v,re.S).group(1) for k,v in pages.items()}
wrapper=(root/'src/wrapper.html').read_text()
result=wrapper.replace('__PAGE_DATA__',json.dumps(data,separators=(',',':'))).replace('__PAGE_TITLES__',json.dumps(titles,ensure_ascii=False,separators=(',',':')))
(root/'index.html').write_text(result)
print(f'Built {len(pages)} pages; {len(result.encode()):,} bytes')
