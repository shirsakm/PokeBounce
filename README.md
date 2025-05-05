# Poke Bounce

## Usage

### Windows

1. Install [Python](https://www.python.org/downloads/) and [add it to PATH](https://realpython.com/add-python-to-path/).
2. [Download](https://github.com/kd8lvt/PokeBounce/archive/refs/heads/main.zip) or clone the repository.
3. Extract the `.zip` file into a folder, if applicable.
4. Open the folder in File Explorer, and type in `cmd` in the folder path to open a PowerShell prompt.
5. Install the required modules,
```
PS C:\game_folder> py -m pip install -r .\requirements.txt
```
6. Run the game,
```
PS C:\game_folder> py .\main.py
```
---
### Linux 
Requirements: A basic understanding of how to use a terminal emulator, and access to root privileges.  
> All of the following commands assume a Ubuntu-based distribution using the `bash` shell. Your experience may vary.

### Initial setup
You should only have to do the following one time, when first setting up the project.

1. Clone the repository (you may need to install `git` via your package manager)
> ```bash
> git clone https://github.com/kd8lvt/PokeBounce.git
> cd PokeBounce
> ```
2. Run the `install` script
> ```bash
> sudo ./install
> ```

### Updating
---
If you want to update the project to the latest codebase, simply run the `update` script
```bash
./update
```
---
### Running
Run the `run` script :)
```bash
./run
```
If you want to update the project before running it, you can do so without the `./update` script.
```bash
./run -u
```

# Credits
This project is far better than it otherwise would be, thanks to these fine folks 💜
- Original concept and codebase, for which this wouldn't exist without: [KingTheLuck](https://www.youtube.com/watch?v=1HLjGrxrzmo)
- Major overhauls & actually knowing python: [anonezumi](https://github.com/anonezumi/PokeBounce)
- Dragonite Icon: [ChocoFoxColin](https://www.weasyl.com/~chocofoxcolin/submissions/1411066/pokemon-icon-dragonite).
- All these fine folks - Join us!  
[![](https://dcbadge.limes.pink/api/server/z2F7HQ2Nk5?style=flat)](https://discord.gg/z2F7HQ2Nk5)