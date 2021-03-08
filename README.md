

![MMAP Logo](https://github.com/nahberry/mmap/Resources/Images/mmap.png)

# MMAP
> "My Nmap"
> V 1.0
> Built this for two reasons:
> 1. Because I'm tired of remembering Nmap scans. Automation makes work easier.
> 2. I wanted to mess with ASCII art.

## Overview

MMAP (My Nmap) is a simple menu tool for Nmap that allows you to quickly select scan types without    
having to remember every Nmap command. By modifying the favorite commands that have been added    
you can quickly refer back to Nmap options you use daily.   

I built this with intentions to modify it easily if my "go to" Nmap scans change.    
I've tried my best to comment the code so other's could modify it as well and make it their own.    
I may eventually work on adding a way to build a favorites list from inside the program (no promises).   

## Installation

I'm not compiling this yet because I don't want to re-compile every time I modify scan types.   
That being said, it's pretty simple to use.   

#### Prerequisites
- Nmap   
- Colorama Python Module  
  Optional. I've added comments of what to remove if you're not using this.  
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
