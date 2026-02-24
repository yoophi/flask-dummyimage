# Flask-DummyImage

Placeholder 이미지를 생성하는 Flask 확장입니다. 개발 및 디자인 프로토타이핑 시 원하는 크기, 색상, 텍스트의 더미 이미지를 즉시 만들 수 있습니다.

## 요구사항

- Python >= 3.9
- [uv](https://docs.astral.sh/uv/) (패키지 매니저)

## 설치 및 실행

```bash
uv sync
uv run flask --app app run --debug
```

서버가 `http://localhost:5000` 에서 시작됩니다.

## URL 패턴

| URL | 설명 |
|-----|------|
| `/dummyimage/dummyimage` | 기본 320x320 정방형 이미지 |
| `/dummyimage/dummyimage/<size>` | 지정한 크기의 정방형 이미지 (예: `/200`) |
| `/dummyimage/dummyimage/<width>x<height>` | 가로/세로 크기를 지정한 이미지 (예: `/640x480`) |

### 예시

```
http://localhost:5000/dummyimage/dummyimage
http://localhost:5000/dummyimage/dummyimage/200
http://localhost:5000/dummyimage/dummyimage/640x480
http://localhost:5000/dummyimage/dummyimage/640x480?text=Hello
http://localhost:5000/dummyimage/dummyimage/640x480?bg_color=red&text_color=white
```

### 쿼리 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `text` | 이미지에 표시할 텍스트 | `<width>x<height>` (예: `640x480`) |
| `bg_color` | 배경 색상 | `yellow` |
| `text_color` | 텍스트 색상 | `black` |
| `border_color` | 테두리 색상 | `silver` |
| `border` | 테두리 표시 여부 | `True` |
| `zoom` | 텍스트를 이미지에 맞게 자동 확대 | `True` |
| `fontsize` | 글꼴 크기 (`zoom=True`일 때 무시됨) | `20` |
| `debug` | 텍스트 영역 표시 | `False` |

### 색상 지정

- 색상명: `red`, `white`, `grey69` 등
- Hex 값: `!` 접두사 + hex 코드 (예: `!FF0000`, `!F00`)

## Flask 프로젝트에 통합하기

```python
from flask import Flask
from flask_dummyimage import DummyImage

app = Flask(__name__)
DummyImage(app)
```

또는 팩토리 패턴을 사용하는 경우:

```python
from flask import Flask
from flask_dummyimage import DummyImage

app = Flask(__name__)
dummy_image = DummyImage()
dummy_image.init_app(app)
```

## 라이선스

MIT
