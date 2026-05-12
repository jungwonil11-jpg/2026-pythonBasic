# Python 자습 프로젝트

## 강사 정보
- upstream: https://github.com/nohssam/2026-pythonBasic

## 브랜치 전략
| 브랜치 | 역할 | 규칙 |
|--------|------|------|
| main   | 강사 코드 미러 | 자습 작업 금지. 강사 싱크 전용. |
| study  | 자습 작업 공간 | 모든 자습·실습·주석 여기에. |

- 매일 작업은 study 브랜치에서만 함
- `.claude/`, `CLAUDE.md`, `CLAUDE.local.md` 는 study에만 존재 (main에 commit 금지)
- 싱크 흐름: `/강사싱크` → main에 강사 코드 → study에 머지
