"""Copy full applicable notices into a fresh static Web license directory."""
from pathlib import Path
import argparse,hashlib,html,json,shutil
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]
def copy_notices(target):
    target=Path(target).resolve()
    if target.exists() and any(target.iterdir()):raise FileExistsError('Choose a new or empty license output directory')
    target.mkdir(parents=True,exist_ok=True);rows=[]
    sources=[ROOT/'LICENSE',ROOT/'THIRD_PARTY_NOTICES.md']+[p for p in (ROOT/'third_party').rglob('*')if p.is_file()]
    for source in sources:
        if source.is_symlink() or not source.resolve().is_relative_to(ROOT):raise ValueError('Unexpected external license path')
        rel=source.relative_to(ROOT);out=target/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,out)
        raw=source.read_bytes()
        if out.read_bytes()!=raw:raise ValueError('License byte mismatch')
        rows.append({'path':rel.as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
    items=''.join('<li><a href="'+quote(row['path'])+'">'+html.escape(row['path'])+'</a></li>'for row in rows)
    (target/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Licenses · BrainBoost Flutter</title><body><h1>Licenses and notices</h1><p>Project code, Flutter, Dart dependencies, Roboto font and build-tool notices retain their original terms.</p><ul>'+items+'</ul></body></html>',encoding='utf8')
    (target/'manifest.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
    return rows
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'build/web/licenses');a=p.parse_args();rows=copy_notices(a.output);print(json.dumps({'files':len(rows),'all_license_bytes_match_source':True}))
