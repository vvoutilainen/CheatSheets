# Cheat sheet for building and running Latex in VSCode

Updated 2021-08-11.

Tested on a Windows 10 machine. The plugin for VSCode is [LaTeX-Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop). See installation and usage instructions in [Github](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install). See also [Writing LaTeX Documents In Visual Studio Code With LaTeX Workshop](https://medium.com/@rcpassos/writing-latex-documents-in-visual-studio-code-with-latex-workshop-d9af6a6b2815) and [VS Code as LaTeX editor](https://danmackinlay.name/notebook/vs_code_for_latex.html).

## Steps to install

 - We use Miktex Latex distribution. Download and install it. **Make sure the installation goes into path with no white spaces in folder names!**
 - MikTeX does not ship with Pearl, so we need to separately download it as the default command for building LaTeX projects `latexmk` requires it. We download *Strawberry Perl* from [here](https://www.perl.org/get.html).
 - Install [LaTeX-Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) plugin to VSCode.
 - Open the example file, select Tex sidebar, and try building the file.
 - Install VSCode plugin [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).
 - Optional: install linter *chktex*. For instructions how to install it see [here](https://github.com/SublimeLinter/SublimeLinter-chktex#linter-installation).
   - Install *cygwin*. When asked which packages to install, make sure to choose from Category *Devel* the following (newest version of each): `make`.
   - Download *chktex* version 1.7.6 from [here](https://www.ctan.org/pkg/chktex?lang=en).
     - Newest version available from git as instructed [here](https://www.nongnu.org/chktex/). This however does not include *config* file in the same way as the packaged one (only*config.in* which I do not know how to use).
   - Put folder *chktex/chktex* under the home directory of cygwin: *cygwin/home/<username>*. Make sure you have launched the cygwin bash once for the folder to appear.
   - Fix [this bug](https://bugs.gentoo.org/attachment.cgi?id=578854&action=diff) by manually adding this line to *ChkTeX.tex.in*: `\usepackage[latin1]{inputenc}`.
   - Run installations commands as explained:
     - `cd C:`
     - `cd cygwin64/home/<USER>/chktex`
     - `./configure`
     - `make`
     - `make install`
   - Save resulting *chktex.exe* as well as *cygwin1.dll* in a directory which is registered in the PATH environment variable (e.g. *C:/MiKTeX/miktex/bin/x64/*.)

## Usage

 - Quite straightforward!
