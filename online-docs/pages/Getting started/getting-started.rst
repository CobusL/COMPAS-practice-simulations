Getting started
===============

To start using COMPAS, `git clone` the code, install dependencies and build COMPAS:

::

    git clone https://github.com/TeamCOMPAS/COMPAS


Install dependencies
--------------------

COMPAS requires a ``C++`` compiler, and the ``gsl``, ``boost``, and ``hdf5`` libraries.  ``Python`` is required for the COMPAS post-processing tools.


.. tabs::

   .. tab:: Linux

    For Ubuntu, type::

        sudo apt-get install g++ libboost-all-dev libgsl-dev libhdf5-serial-dev

    For Fedora::

        sudo dnf install gcc boost-devel gsl gsl-devel hdf5-devel

    For RHEL or CentOS::

        sudo yum install gcc boost-devel gsl gsl-devel hdf5-devel


   .. tab:: MacOS

    It is strongly recommended to update to the latest version of macOS through the App Store. You can find what macOS version you are
    using by clicking on the Apple symbol on the top left of your screen and clicking "About This Mac".

    The next step is to install or update Xcode. You can find it directly in the App Store or at `Xcode <https://developer.apple.com/xcode/>`__\ .
    Note: Xcode installation requires around 20 GB of disk space. If you are low on disk space, you may consider installing a ``C++``
    compiler directly.

    Once Xcode is installed, open a Terminal, and execute the following command to install the required command line developer tools::

        xcode-select --install

    Next, you need to install several extra libraries and python modules. Popular ways of installing them are via package managers MacPorts and Homebrew.
    We give instructions for installing ``gsl``, ``boost``, and ``hdf5`` with Homebrew. To install Homebrew, run::

        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    If the installation was successful, the following should run without error::

        brew --version

    Now install ``gsl``, ``boost``, and ``hdf5`` using Homebrew by running::

        brew install gsl
        brew install boost
        brew install hdf5


Building COMPAS
---------------

We first need to define an environment variable for the root directory of COMPAS in your shell start-up file for COMPAS to run properly. For example,
if you use bash as your shell, open `~/.bashrc` with a text editor and put in the following::

    export COMPAS_ROOT_DIR=~/codes/COMPAS

where `~/codes` should be replaced with the path to the directory where you cloned the COMPAS repository. For this to take effect, either restart your
bash session or run::

    source ~/.bashrc

If your shell is ``zsh`` (which is the default of macOS 10.15), set the environment variable as above in `~/.zshrc` instead of `~/.bashrc`. If your shell
is ``csh``, set the environment variable in `~/.cshrc` using::

    setenv COMPAS_ROOT_DIR ~/codes/COMPAS

Tip: you can check whether you have correctly defined the environment variable and whether its been active by typing into your terminal the command::

    ECHO $COMPAS_ROOT_DIR

This should return the directory location of the COMPAS folder (i.e. "~/codes/COMPAS").



Now go to the COMPAS source code directory::

    cd $COMPAS_ROOT_DIR/src

In this directory you will find the file ``Makefile``, which includes the following text to inform the compiler of the location of header files, and
the linker of the location of library files, for each of the dependencies ``gsl``, ``boost``, and ``hdf5``:

::

    # gsl directories
    GSLINCDIR := /include
    GSLLIBDIR := /lib

    # boost directories
    BOOSTINCDIR := /include
    BOOSTLIBDIR := /lib

    # hdf5 directories
    HDF5INCDIR := /usr/include/hdf5/serial
    HDF5LIBDIR := /usr/lib/x86_64-linux-gnu/hdf5/serial

The locations given in ``Makefile`` may not match the locations of the files on your system.


If you installed the packages with Homebrew, the package files are likely to be found in /usr/local/opt (in directories gsl, boost, and hdf5 respectively),
but if they are not found there you will need to use Homebrew, or some other method, to locate the files.  e.g. for ``boost`` using Homebrew::

    brew info boost
    boost: stable 1.72.0 (bottled), HEAD
    Collection of portable C++ source libraries
    https://www.boost.org/
    /usr/local/Cellar/boost/1.72.0 (14,466 files, 648.5MB) *
    ...

Note the path, which in this case is `/usr/local/Cellar/boost/1.72.0` - you will use it when you build the COMPAS executable.  Repeat this for ``gsl`` and
``hdf5``, ensuring you locate the paths to the header files and library files.

Assuming here that the locations of the header and library files in ``Makefile`` for ``gsl`` and ``hdf5`` are correct for your system, but the locations for
``boost`` are not, build the COMPAS executable (compile and link) by typing::

    make -f Makefile BOOSTINCDIR=/usr/local/Cellar/boost/1.72.0/include BOOSTLIBDIR=/usr/local/Cellar/boost/1.72.0/lib

The build process will run much faster if multiple processors/cores are available. To build the COMPAS executable using (e.g.) 4 cores, type::

    make -j 4 -f Makefile BOOSTINCDIR=/usr/local/Cellar/boost/1.72.0/include BOOSTLIBDIR=/usr/local/Cellar/boost/1.72.0/lib

Note that both ``make`` commands shown above will conduct incremental builds: they will only compile source files that have changed. To ensure a clean build
in which all source files are compiled, type::

    make clean
    make -j 4 -f Makefile BOOSTINCDIR=/usr/local/Cellar/boost/1.72.0/include BOOSTLIBDIR=/usr/local/Cellar/boost/1.72.0/lib

The `clean` option instructs ``make`` to remove all existing object files (.o), and the COMPAS executable.  A subsequent ``make`` is then forced to compile
all source files and link the resultant object files (and external libraries) into a new executable.

Note that rather than type the ``make`` command each time you want to build COMPAS, you could create a file containing the ``make`` command, and execute that
file to build COMPAS.

Once built, the executable can be tested with, e.g.::

    ./COMPAS -v

which will display the code version.

See :doc:`../Developer guide/Developer build/COMPAS-local-build` for a detailed description of ``Makefile`` functionality.


:bolditalictext:`A note for Mac users:`

If you are using MacOS and running into linking issues with the boost libraries, try::

    make clean
    make CPP=clang++ -j$(sysctl -n hw.ncpu)

In some Mac installations, the GNU C++ compiler is not installed how we might expect, so trying to compile and link with ``clang++`` might help.


Installing python utilities
---------------------------

You can use pip to install the `compas_python_utils`

::

    pip install .


Use `-e .[dev]` to install in development mode (i.e. editable mode) and include the development dependencies.

::

    pip install -e .[dev]



Next steps
----------
Once you have completed the steps shown above, you're ready to run COMPAS. The :doc:`COMPAS User Guide <../User guide/user-guide>`
explains in detail how to run COMPAS, but to check that COMPAS is installed correctly, and to get a taste of what running COMPAS looks
like, you could try the :doc:`COMPAS Tutorial <../User guide/Running COMPAS/running-compas>`.

