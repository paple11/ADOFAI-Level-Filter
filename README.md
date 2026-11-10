# ADOFAI Level Filter

ADOFAI(`.adofai`) 레벨에서 지정된 이벤트만 남기고 불필요한 이벤트와 장식을 제거하는 Python 스크립트입니다.

필터링된 레벨은 별도의 폴더에 저장되며, 음악 파일도 자동으로 복사됩니다.

## 주요 기능

- 지정된 25종의 이벤트만 유지
- 나머지 이벤트 자동 제거
- 트랙 스타일 및 색상 초기화
- 모든 장식(`decorations`) 제거
- 음악 파일(`.mp3`, `.ogg`, `.wav`, `.flac`) 자동 복사
- JSON 및 JSON5 파싱 지원
- 여러 레벨 파일 중 원하는 파일 선택
- 원본 레벨 파일 유지

## 설치

**요구 사항**
- Python 3
- `json5` 라이브러리

필요한 라이브러리를 설치합니다.

```bash
pip install json5
```

## 사용 방법

**1. 스크립트 실행**

Python 파일을 `filter.py`로 저장했다고 가정합니다.

```bash
python filter.py
```

**2. 레벨 폴더 경로 입력**

```text
레벨 파일이 있는 폴더 경로를 입력하세요:
```

예시:

```text
sample/2021 (기본 테스트)
```

`.adofai` 파일이 들어 있는 폴더 경로를 입력합니다.

**3. 레벨 선택**

폴더에 여러 `.adofai` 파일이 있으면 선택 메뉴가 표시됩니다.

```text
====================
1. Level\main.adofai
2. Level\test.adofai
====================
필터링할 레벨을 선택하세요(번호로 입력):
```

파일이 하나라면 자동으로 선택됩니다.

**4. 결과 확인**

완료된 레벨은 `Filtered` 폴더에 저장됩니다.

## 출력 구조

```text
sample/
└── 2021 (기본 테스트)/
    ├── main.adofai
    ├── music.ogg
    └── Filtered/
        ├── main_filtered.adofai
        └── music.ogg
```

원본 파일은 유지되며, 필터링된 레벨에는 `_filtered` 접미사가 붙습니다.

## 유지되는 이벤트

다음 이벤트는 제거하지 않습니다.

```text
SetSpeed
Twirl
SetHitsound
SetPlanetRotation
Pause
SetPlanetSize
MoveTrack
PositionTrack
MoveCamera
Hold
MultiPlanet
FreeRoam
ScaleMargin
ScaleRadius
PlaySound
AnimateTrack
RepeatEvents
Checkpoint
KillPlayer
AutoPlayTiles
Multitap
FreeRoamTwirl
FreeRoamRemove
TileDimensions
Hide
SetInputEvent
```

이 목록에 없는 모든 `actions` 이벤트는 제거됩니다.

## 변경되는 설정

| 설정 | 변경 값 |
|---|---|
| `trackStyle` | `Standard` |
| `trackColor` | `debb7bff` |
| `backgroundColor` | `000000` |
| `trackColorType` | `Single` |
| `decorations` | `[]` |

그 외 설정은 기본적으로 유지됩니다.

## 주의 사항

- 필터링으로 인해 일부 레벨 연출이나 동작이 달라질 수 있습니다.
- `backup.adofai`는 선택 대상에서 제외됩니다.
- 지정한 폴더의 최상위 `.adofai` 파일만 검색합니다.
- 원본 레벨 파일은 수정하지 않지만, 동일한 이름의 결과 파일이 이미 존재하면 덮어씁니다.
- 음악 파일은 원본 레벨과 같은 폴더에 있는 파일만 복사합니다.
- 결과 파일은 공백과 들여쓰기를 최소화한 JSON 형식으로 저장됩니다.
