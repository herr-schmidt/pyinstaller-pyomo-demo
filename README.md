# pyinstaller-pyomo-demo
Short tutorial on how to package a Python + Pyomo into an executable file.

Folder `scripts` contains the following files:

* `concrete.py` (1)
* `pp.py` (2)
* `hook-pyomo.environ.py` (3)

(1) contains a simple concrete model defined using Pyomo. Two imports are specified:

* `import pp` and
* `import pyomo.environ as pyo`

The former is only used to import a dummy function which just performs a print - as defined in (2) - whereas the latter is needed to actually use Pyomo (modeling + calling a solver). Both package `pyomo.environ` and module `pp.py` need to be packaged by PyInstaller, but for the first one we must specify
every hidden import it depends on. This is done by using hook file (3). Further info about hidden imports' management via hook files can be found [here](https://pyinstaller.readthedocs.io/en/stable/hooks.html).

An .exe file for our application can be generated using the command 

<mark>`python -m PyInstaller --additional-hooks-dir=. concrete.py --onefile --name pyomo-app`</mark>

where:

* `--additional-hooks-dir` specifies where to find hook files;
* `concrete.py` is the script we want to make an executable of;
* `--onefile` specifies that we want a _single_ .exe file to be generated in our `dist` folder (`dist` will contain our "deliverable" application). If such option is not provided, then `dist` will contain _many_ other files in addition to the executable one;
* `--name` specifies the name given to the generated executable file, in this case `pyomo-app.exe`.

**Remark**: after `pyomo-app.exe` has been generated, we need to copy and paste an executable of the solver we are using under its same directory (`dist`). In this example, the specified solver is [Ipopt](https://coin-or.github.io/Ipopt/).
Binaries can be found right [here](https://www.coin-or.org/download/binary/Ipopt/).

For more detailed info about PyInstaller, check its [manual](https://pyinstaller.readthedocs.io/en/stable/).