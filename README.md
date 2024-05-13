# Maze Solver - A [boot.dev](https://boot.dev) Project

A maze generator and solver from [boot.dev](https://boot.dev) Python track.

## Usage

Update the variables in `main.py` to configure the maze (all values are pixel units):

```python
# size of the application window
WINDOW_X = 800
WINDOW_Y = 600
# size of the maze
NUM_ROWS = 10
NUM_COLS = 10
# location of maze in window
ORIGIN_X = 0
ORIGN_Y = 0
# size of cells
CELL_WIDTH = 50
CELL_HEIGHT = 50
```

Run the program: `python main.py`

## Develop

This repo contains a [devcontainer](https://code.visualstudio.com/docs/devcontainers/create-dev-container) to support isolated dev environment with all required languages and tooling.

Prereqs for using devcontainer ([Getting Started Guide](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)):

- VSCode
- [VSCode Remote Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Docker

The [devcontainer](.devcontainer/devcontainer.json) that contains:

- Python
- Golang
- [bootdev cli](https://github.com/bootdotdev/bootdev)
- a few VSCode extensions%