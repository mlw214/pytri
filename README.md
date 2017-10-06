<p align="center">
 <?xml version="1.0" standalone="no"?>
<svg width="400" height="250" version="1.1" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="f2" x="0" y="0" width="100%" height="100%">
            <feOffset result="offOut" in="SourceGraphic" dx="0" dy="0" />
            <feGaussianBlur result="blurOut" in="offOut" stdDeviation="0.8" />
            <feBlend in="SourceGraphic" in2="blurOut" mode="normal" />
        </filter>
    </defs>
    <g transform="scale(3) translate(0,0)" filter="url(#f2)">
        <mask id="hole">
            <polygon points="5 60 80 35 132 50 60 75" stroke="transparent" fill="white" />
            <polygon points="20 60 80 40 120 50 60 70" stroke="transparent" id="mask" fill="black" />
        </mask>
        <polygon points="5 60 80 35 132 50 60 75" stroke="transparent" fill="white" opacity="1" mask="url(#hole") />
        <g>
            <polygon points="20 50 80 30 120 40 60 60" stroke="transparent" fill="magenta" opacity=0.7 />
            <polygon points="27 47.5 20 50 60 60 120 40 114 38.5 60.5 56" stroke="transparent" fill="blue" opacity=0.9 />
        </g>
        <polygon points="20 40 80 20 120 30 60 50" stroke="transparent" fill="yellow" opacity=0.7 />
        <g>
            <polygon points="20 30 80 10 120 20 60 40" stroke="transparent" fill="cyan" opacity=0.7 />
            <polygon points="27 28.5 20 30 60 40 120 20 114 18.5 60.5 36" stroke="transparent" fill="blue" opacity=0.9 />
            <polygon points="20 30 26 31.2 86 11 80 10" stroke="transparent" fill="blue" opacity=0.9 />
        </g>
</g>
</svg>
 <h1 align="center" fontsize="3em">pytri</h1>
</p>

<p align="center">
    <span>A python wrapper for <a href="https://github.com/jhuapl-boss/substrate">substrate</a>.</span><br />
    <a href="https://circleci.com/gh/j6k4m8/pytri"><img alt="CircleCI" src="https://circleci.com/gh/j6k4m8/pytri.svg?style=svg" /></a>
</p>

## Installation and Configuration
- Clone the repository.
```shell
git clone https://github.com/j6k4m8/pytri.git
```
- Install all dependencies.
```shell
pip3 install -r requirements.txt
```

## Usage

```python
from pytri import Visualizer, GraphLayer

V = Visualizer()

V.add_layer(
    GraphLayer(data={
        "nodes": [{}, {}, {}],
        "edges": [[0, 1], [1, 2], [2, 0]]
    })
)

V.show()
```
