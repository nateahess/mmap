

![MMAP Logo](https://github.com/nahberry/mmap/blob/main/Resources/Images/mmap.PNG)

# MMAP
> "My Nmap"
> V 1.0  
> Built this for two reasons:  
> 1. Because I'm tired of remembering Nmap scans. Automation makes work easier.
> 2. I wanted to mess with ASCII art.


![GitHub last commit](https://img.shields.io/github/last-commit/nahberry/mmap)


## Overview

* MMAP is a simple menu tool for Nmap that allows you to quickly select scan types  
without having to remember every Nmap command.  
* By modifying the favorite commands that have been added you can quickly refer back to Nmap options   you use daily.   

I built this with intentions to modify it easily if my "go to" Nmap scans change.    
I've tried my best to comment the code so other's could modify it as well and make it their own.    
I may eventually work on adding a way to build a favorites list from inside the program (no promises).   

## Installation

> I'm not compiling this yet because I don't want to re-compile every time I modify scan types.    
> That being said, it's pretty simple to use.   

#### Prerequisites
- _Nmap_
- _Colorama_ (Python Module)
  *Optional.* I've added comments of what to remove if you're not using this.  
  This module is simply for coloring the ASCII art.  

#### Clone the Project

```

git clone https://github.com/nahberry/mmap

```

#### CD into the directory  

```

cd MMAP

```
#### Run the mmap.py file

```

python3 mmap.py

```

## Code Modifications

> As stated previously, favorites are built by modifying the code  
> currently. It is, however, fairly simple.  

#### Editing Favorites

* Go to [menu.py](https://github.com/nahberry/mmap/blob/main/menu.py) and change the favorites menu to reference the scans you  
want to add.  

* Move over to the [nmap.py](https://github.com/nahberry/mmap/blob/main/nmap.py) file and change/add your favorite scans.

```

favoriteOne = "-vv -n -p- -sV "
favoriteTwo = "-sV -oX "

```
> Format: set the "favoriteNumber" variable to the Nmap options you want to use for your command. Keep in mind the order of the options as this is printed directly to the console. Leave a trailing space at the end of the variable to allow for an IP Address to be added to the end.

* Head on over to the [favorites.py](https://github.com/nahberry/mmap/blob/main/favorites.py) file.

> Here you can add to the if/else statements that assign your favorite scans to the scanType variable. Add more if needed or change the existing one's.

### In Use
![mmapdemo](https://github.com/nahberry/mmap/blob/main/Resources/Images/mmapDemo.gif)

## That's all, folks!
