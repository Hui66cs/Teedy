import urllib.request
import re

req = urllib.request.Request("https://docs.pmd-code.org/latest/pmd_rules_java_design.html", headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8")

matches = re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>(.*?)(?=<h2|<h1|$)', html, re.DOTALL | re.IGNORECASE)

for m in matches:
    rule_id, rule_title, content = m.groups()
    if 'cyclomaticcomplexity' == rule_id.lower() or 'cyclomaticcomplexity' in content.lower() or 'wmc' in content.lower():
        text_content = re.sub(r'<[^>]+>', ' ', content)
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        print(f"Rule: {rule_title}\n{text_content[:800]}\n")
