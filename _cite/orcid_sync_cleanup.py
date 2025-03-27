import yaml
from pathlib import Path

# 读取 YAML 文件
def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 保存 YAML 文件
def save_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

# 路径设置
citations_path = Path("_data/citations.yaml")
sources_path = Path("_data/sources.yaml")

# 加载 citations.yaml 和 sources.yaml
citations = load_yaml(citations_path)
manual_sources = load_yaml(sources_path)

# 获取 ORCID 自动同步的条目 ID 列表（通常来自 orcid.yaml，但都最终进入 citations）
orcid_ids = set(c["id"] for c in citations if c.get("file", "").startswith("orcid"))

# 1. 移除 preprint 类型的 ORCID 条目
citations = [c for c in citations if not (c.get("type") == "preprint" and c.get("file", "").startswith("orcid"))]

# 2. 删除已经同步到 ORCID 的手动条目
remaining_sources = [s for s in manual_sources if s.get("id") not in orcid_ids]

# 保存处理后的结果
save_yaml(citations_path, citations)
save_yaml(sources_path, remaining_sources)

print("✅ Cleanup done: removed preprints and duplicate manual entries found in ORCID.")