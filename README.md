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

### Linux 

### Debian-based distributions

> [!WARNING]
> All of the following commands were run on a Ubuntu-based distribution using the `bash` shell. Your experience may vary.

Requirements: A basic understanding of how to use a terminal emulator, and access to root privileges.

#### Initial setup

Install `git` if not already installed,
```bash
sudo apt install git-all
```
1. Clone the repository,
```bash
git clone https://github.com/kd8lvt/PokeBounce.git
cd PokeBounce
```
2. Run the `install` script,
```bash
./install
```

> [!NOTE]
> You should only have to do the setup once, when setting up the project for the first time.

#### Running
Run the `run` script :)
```bash
./run
```

If you want to update the project before running it, you can do so with the `-u` or `--update` flag,
```bash
./run -u
```

#### Updating

If you want to update the project to the latest codebase, simply run the `update` script,
```bash
./update
```

### Mac
I don't own any Apple products, but if someone wants to figure out the steps to run it, feel free to contribute and open a PR :)  

##  Credits
This project is far better than it otherwise would be, thanks to these fine folks 💜
- Original concept and codebase, for which this wouldn't exist without: [KingTheLuck](https://www.youtube.com/watch?v=1HLjGrxrzmo)
- Major codebase overhaul: [anonezumi](https://github.com/anonezumi/PokeBounce)
- Refactoring and significant contributions: [kd8lvt](https://github.com/kd8lvt/PokeBounce)
- Dragonite Icon: [ChocoFoxColin](https://www.weasyl.com/~chocofoxcolin/submissions/1411066/pokemon-icon-dragonite).
- All these fine folks - Join us!  
[![](https://dcbadge.limes.pink/api/server/z2F7HQ2Nk5?style=flat)](https://discord.gg/z2F7HQ2Nk5)
