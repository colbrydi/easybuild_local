# MFEM build

The current error is an undefined reference to dpotrf_ which seems to be in the LAPACK library which weirdly is not intalled on the system.

/opt/software-current/2023.06/x86_64/generic/software/binutils/2.40-GCCcore-12.3.0/bin/ld: /opt/software-current/202
3.06/x86_64/generic/software/Hypre/2.29.0-foss-2023a/lib/libHYPRE.a(HYPRE_lobpcg.o): in function `dpotrf_interface':
HYPRE_lobpcg.c:(.text+0x175): undefined reference to `dpotrf_'


# QGIS build

A lot of missing depedancies.  I need to figure out how to add them. This is probably my next step on both projects. I need to instal LAPACK and a whole list of dependancies in QGIS


Qt5Webkit/5.212.0-alpha4-foss-2023a, GEOS/3.9.1-foss-20 23a, SQLite/3.43-foss-2023a, libspatialite/5.0.1-foss-2023a, libspatialindex/1.9.3-foss-2023a, Cartopy/0.20.3-foss-2023a, psycopg2/2.9.5-foss-2023a, GDAL/3.3.2-foss-2023a, Qwt/6.2.0-foss-2023a


# Add in test module to be laoded so users know they installed it correctly