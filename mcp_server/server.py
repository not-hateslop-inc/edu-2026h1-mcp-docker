import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP

ROOT = (Path(__file__).parent / "notices").resolve()
mcp = FastMCP("hs-notices", host="0.0.0.0", port=8000)

@mcp.tool()
def list_notices() -> list[str]:
    """사내 공지 id 목록을 돌려준다."""
    return sorted(p.stem for p in ROOT.glob("*.md"))

@mcp.tool()
def read_notice(notice_id: str) -> str:
    """공지 본문을 읽는다. notice_id는 list_notices 결과 값만 쓴다."""
    p = (ROOT / f"{notice_id}.md").resolve()
    if ROOT not in p.parents or not p.exists():
        raise ValueError("없는 공지입니다")
    return p.read_text(encoding="utf-8")

@mcp.resource("notices://latest")
def latest() -> str:
    files = sorted(ROOT.glob("*.md"))
    return files[-1].read_text(encoding="utf-8") if files else ""

if __name__ == "__main__":
    mcp.run(transport=os.getenv("MCP_TRANSPORT", "stdio"))
