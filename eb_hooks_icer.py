# Modified from EESSI hooks
# Hooks to customize how EasyBuild installs software in EESSI
# see https://docs.easybuild.io/en/latest/Hooks.html
import os
import re

from easybuild.tools.build_log import print_msg

def parse_hook(self, *args, **kwargs):
    """
    For OpenMPI, add env variables to avoid libfabric issues, see also:
    https://github.com/easybuilders/easybuild-easyconfigs/issues/20233

    For R, make sure extensions are installed prefixed with
    R_LIBS_USER=/dev/null to make sure local extensions aren't picked
    up
    """
    if self.name == 'NVHPC':
        self.log.info("[parse hook] Adding extra qdlib LD_LIBRARY_PATH in module file")
        self['modextrapaths']['LD_LIBRARY_PATH'] = 'Linux_x86_64/%(version)s/compilers/extras/qd/lib/'
    if self.name == 'OpenMPI':
        self.log.info("[parse hook] Adding environment variables to bypass libfabric")
        self['modextravars'] = {
            'OMPI_MCA_btl': '^uct,ofi',
            'OMPI_MCA_pml': 'ucx',
            'OMPI_MCA_mtl': '^ofi'
        }
    if self.name == 'R' or self.name.startswith('R-bundle-'):
        if self['exts_default_options']:
            self['exts_default_options']['preinstallopts'] = \
                    "R_LIBS_USER=/dev/null %s" % self['exts_default_options'].get('preinstallopts', '')

def post_ready_hook(self, *args, **kwargs):
    """
    Post-ready hook: limit parallellism for selected builds, because they require a lot of memory per used core.
    """
    # 'parallel' easyconfig parameter is set via EasyBlock.set_parallel in ready step based on available cores.
    # here we reduce parallellism to only use half of that for selected software,
    # to avoid failing builds/tests due to out-of-memory problems
    if self.name in ['TensorFlow', 'libxc', 'PyTorch']:
        parallel = self.cfg['parallel']
        if parallel > 1:
            self.cfg['parallel'] = parallel // 2
            msg = "limiting parallelism to %s (was %s) for %s to avoid out-of-memory failures during building/testing"
            print_msg(msg % (self.cfg['parallel'], parallel, self.name), log=self.log)

def pre_configure_hook(self, *args, **kwargs):
    if self.name == 'OpenMPI':
        self.log.info("[pre-configure hook] Adding --with-slurm --with-pmi options")
        self.cfg['configopts'] += " --with-slurm --with-pmi=/usr --with-pmi-libdir=/lib/x86_64-linux-gnu "
