Run packages individually using:
    conda install -y package_name=version (without build info)

Packages that didn't install correctly:
    conda install -y gcc=4.8.5
        conda install -c nlesc gcc
    conda install -y jupyter_contrib_core=0.3.3
        pip install  jupyter_contrib_core=0.3.3
    conda install -y jupyter_contrib_nbextensions=0.5.1
        pip install jupyter-contrib-nbextensions
    conda install -y jupyter_highlight_selected_word=0.2
        pip install jupyter_highlight_selected_word
    conda install -y jupyter_latex_envs=1.4.4
        pip install jupyter_latex_envs=1.4.4
    conda install -y jupyter_nbextensions_configurator=0.4.1
        pip install jupyter_nbextensions_configurator==0.4.1
    conda install -y libcxxabi=4.0.1
        conda install -c conda-forge libcxxabi        
    conda install -y llvm-openmp=4.0.1
        conda install -c conda-forge llvm-openmp


Then export new environment file:
conda env export --no-build > linux_env.yml

Then execute:
conda env create -f linux_env.yml


Error:
    Collecting python-graphviz==0.11 (from -r /home/ben/Desktop/flatiron/section_1/linux_env_build/condaenv.w48qf9x0.requirements.txt (line 40))

    Pip subprocess error:
    ERROR: Could not find a version that satisfies the requirement python-graphviz==0.11 (from -r /home/ben/Desktop/flatiron/section_1/linux_env_build/condaenv.w48qf9x0.requirements.txt (line 40)) (from versions: none)
    ERROR: No matching distribution found for python-graphviz==0.11 (from -r /home/ben/Desktop/flatiron/section_1/linux_env_build/condaenv.w48qf9x0.requirements.txt (line 40))


    CondaEnvException: Pip failed

Fixed by s/python-graphviz/graphviz


Unresolved error:
ERROR: keras 2.2.4 has requirement keras-applications>=1.0.6, but you'll have keras-applications 1.0.4 which is incompatible.
ERROR: keras 2.2.4 has requirement keras-preprocessing>=1.0.5, but you'll have keras-preprocessing 1.0.2 which is incompatible.
