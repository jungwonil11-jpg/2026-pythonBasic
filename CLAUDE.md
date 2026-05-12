# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

## 파일 실행
```powershell
python day01\ex01_print.py
```

## 코드 구조
수업일별 폴더(`day01/`, `day02/`, ...)에 예제 파일(`ex01_*.py`, `ex02_*.py`, ...)을 순서대로 작성.
강사 화면을 보고 그대로 베끼는 방식으로 수업 진행.

## 코딩 규칙
- 강사 코드를 그대로 옮길 때는 주석 포함하여 원본 그대로 유지
- `str`을 변수명으로 쓰는 등 강사 코드의 스타일이 lint 경고를 유발해도 수정하지 않음
