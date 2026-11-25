# edu-2026h1-mcp-docker

2026 상반기 11·12회차 실습 저장소입니다.

- EDU-2026-H1-11 MCP 기초 (2026-05-14)
- EDU-2026-H1-12 Docker로 실습 환경 배포 (2026-05-21)

| 경로 | 회차 | 내용 |
| --- | --- | --- |
| `mcp_server/server.py` | 11 | FastMCP로 만든 사내 공지 검색 서버 |
| `mcp_server/notices/` | 11 | 공지 샘플 |
| `mcp_config.example.json` | 11 | AI 도구에 연결하는 설정 |
| `Dockerfile` | 12 | 서버를 컨테이너로 |
| `docker-compose.yml` | 12 | streamable-http로 띄우기 |

## 실행

```bash
pip install -r requirements.txt
python mcp_server/server.py                  # stdio
docker compose up --build                    # http://localhost:8000/mcp
```

5/23 워크숍(사내 AI 실무 워크숍)은 이 저장소의 Docker 환경을 사용합니다.
