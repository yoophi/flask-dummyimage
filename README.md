# DummyImage

dummy image 를 만들 수 있는 서비스입니다.

## 실행방법

### 설치

```bash
uv sync
```

### 실행

```bash
uv run flask --app app run --debug
```

서버가 `http://localhost:5000` 에서 시작됩니다.

## 지원하는 URL

| URL | 설명 |
|-----|------|
| `/dummyimage/dummyimage` | 기본 320x320 정방형 이미지 |
| `/dummyimage/dummyimage/<size>` | 지정한 크기의 정방형 이미지 |
| `/dummyimage/dummyimage/<width>x<height>` | 가로/세로 크기를 지정한 이미지 |

### 예시

```
http://localhost:5000/dummyimage/dummyimage
http://localhost:5000/dummyimage/dummyimage/200
http://localhost:5000/dummyimage/dummyimage/640x480
http://localhost:5000/dummyimage/dummyimage/640x480?text=Hello
http://localhost:5000/dummyimage/dummyimage/640x480?bg_color=red&text_color=white
```

### QueryString 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `text` | 이미지에 표시할 글씨 | `가로x세로` (예: `640x480`) |
| `bg_color` | 배경 색상 | `yellow` |
| `text_color` | 글씨 색상 | `black` |
| `border_color` | 테두리 색상 | `silver` |
| `border` | 테두리 표시 여부 | `True` |
| `zoom` | 글씨를 이미지에 가득 차게 표시 | `True` |
| `fontsize` | 글꼴 크기 (`zoom=True` 시 무시됨) | `20` |
| `debug` | 텍스트 영역 표시 | `False` |

색상은 색상명(예: `red`, `white`) 또는 `!` 접두사를 붙인 hex 값(예: `!FF0000`, `!F00`)을 사용할 수 있습니다.

## Flask 프로젝트에서 사용하기

```python
from flask import Flask
from flask_dummyimage import DummyImage

app = Flask(__name__)
DummyImage(app)
```

또는

```python
from flask import Flask
from flask_dummyimage import DummyImage

app = Flask(__name__)
dummy_image = DummyImage()
dummy_image.init_app(app)
```
