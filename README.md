# Directory to help do local EASYBUILD installs in the current directory
Here is a good source of EasyBuild config files <https://github.com/easybuilders/easybuild-easyconfigs>
<https://gitlab.msu.edu/icer/docs/staffdocs/-/blob/mkdocs/docs/UbuntuCompute/editing_easyconfigs.md?ref_type=heads>

Local configs: /opt/software-current/2023.06/x86_64/generic/software/EasyBuild/4.9.1/easybuild/easyconfigs/

1. Grab an existing file
```eb --copy-ec --try-toolchain-version=2023a --try-update-deps FILENAME.eb```

2. Install the easybuild config file locally using my local repository.
```
source activate_easybuild_local
eb --parallel=8 --robot ./easyconfigs/FILENAME.eb
```
3. Install the easybuild config globally using the software_layer repository.
```
cd ../software-layer/
source activate_easybuild_icer
source dirk_activate_easybuild_icer
eb --parallel=8 --robot ../local/easyconfig/FILENAME.eb
```
4. Add easybuild to the easystack as a pull request.
```
export PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring
export EASYBUILD_GITHUB_USER=$USER
git pull
eb --github-user colbrydi --preview-pr --pr-target-account MSU-ICER ../local/easyconfig/FILENAME.eb
```
5. Install add the pullrequest number to the easystack.
```
vim ./easystack/
```



