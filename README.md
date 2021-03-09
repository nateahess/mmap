

![MMAP Logo](https://github.com/nahberry/mmap/blob/main/Resources/Images/mmap.PNG)

# MMAP
> "My Nmap" - Simple Nmap Scripting with Python
> V 1.0
> Built this for two reasons:  
> 1. Because I'm tired of remembering Nmap scans.
> 2. I wanted to mess with ASCII art.  


![GitHub last commit](https://img.shields.io/github/last-commit/nahberry/mmap)


## Overview

* MMAP is a simple menu tool/script for Nmap that allows you to quickly select scan types  
without having to remember every Nmap command.  
* By modifying the favorite commands that have been added you can quickly refer back to the Nmap options you use daily.   

I've tried my best to comment the code so other's could modify it as well and make it their own.     

## Installation

> I'm not compiling this because it's basically a glorified script.
> You can use it by cloning the project   

#### Prerequisites
- _Nmap_ (obviously)
- _Colorama_ (Python Module)
  *Optional.*   This module is simply for coloring the ASCII art.   
  I've commented out all of the Colorama code,  
  but feel free to install the module and use it!  
  I've notated everything in the code comments.  


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

> I've tried keeping it fairly simple to modify and add commands.
> You'll find more information in the code itself as well.

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

## In Use
![mmapdemo](https://github.com/nahberry/mmap/blob/main/Resources/Images/mmapDemo.gif)
