# automation
This framework is based on Python3.6, selenium for python and chromedriver.
To simplify the job, it includes a conda environment shoestore based on bash
profile under mac OSX (shoestore env is compatible on macOS Big Sur and up). 
However, since python, selenium and chromedriver is multiplatform, this 
framework might be used on any OS. 
If this framework is executed without the conda environment shoestore or in a different OS than macOS, then 
be aware of extra setup might be needed and also read the docstring on Launcher.py

STEPS TO SETUP SHOESTORE ENV AND AUTOMATION FRAMEWORK ON MAC
1. [OPTIONAL] Just execute this step if homebrew is not installed and you want to install it.
In terminal execute:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. [OPTIONAL] Just execute this step if anaconda is not installed.
In terminal execute:
```
brew install --cask anaconda
```
3. Open bash profile and add anaconda PATH at the end of the file. In terminal:
```
nano ~/.bashrc


export PATH="/usr/local/anaconda3/bin:$PATH"
```
4. Save the changes and close bash profile
5. Execute this command in terminal to refresh recent changes:
```
source ~/.bashrc
```
6. Execute this other command in terminal:
```
conda init bash
```
7. Clone the automation framework repository, In terminal:
```
git clone https://github.com/richardeus1/automation.git
```
8. Go inside recent repository cloned. In terminal:
```
cd automation
```
9. We are going to create the shoestore environment by using requirements file.
In terminal:
```
conda env create -f environment.yml
```
10. Now is time to activate the shoestore environment. In terminal:
```
conda activate shoestore
```
11. Launch the automation tool. In terminal:
```
python Launcher.py
```
12. [OPTIONAL] If error permission appear. Then in terminal:
```
sudo chmod +x Launcher.py
```
