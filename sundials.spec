#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : sundials
Version  : 5.8.0
Release  : 40
URL      : https://github.com/LLNL/sundials/archive/v5.8.0/sundials-5.8.0.tar.gz
Source0  : https://github.com/LLNL/sundials/archive/v5.8.0/sundials-5.8.0.tar.gz
Summary  : Suite of Nonlinear and Differential/ALgebraic equation Solvers
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sundials-data = %{version}-%{release}
Requires: sundials-filemap = %{version}-%{release}
Requires: sundials-lib = %{version}-%{release}
Requires: sundials-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : openblas
BuildRequires : openmpi-dev
BuildRequires : python3

%description
SUNDIALS is a family of software packages implemented with the goal of providing
robust time integrators and nonlinear solvers that can easily be incorporated
into existing simulation codes. The primary design goals are to require minimal
information from the user, allow users to easily supply their own data structures
underneath the packages, and allow for easy incorporation of user-supplied linear
solvers and preconditioners.

%package data
Summary: data components for the sundials package.
Group: Data

%description data
data components for the sundials package.


%package dev
Summary: dev components for the sundials package.
Group: Development
Requires: sundials-lib = %{version}-%{release}
Requires: sundials-data = %{version}-%{release}
Provides: sundials-devel = %{version}-%{release}
Requires: sundials = %{version}-%{release}

%description dev
dev components for the sundials package.


%package filemap
Summary: filemap components for the sundials package.
Group: Default

%description filemap
filemap components for the sundials package.


%package lib
Summary: lib components for the sundials package.
Group: Libraries
Requires: sundials-data = %{version}-%{release}
Requires: sundials-license = %{version}-%{release}
Requires: sundials-filemap = %{version}-%{release}

%description lib
lib components for the sundials package.


%package license
Summary: license components for the sundials package.
Group: Default

%description license
license components for the sundials package.


%package staticdev
Summary: staticdev components for the sundials package.
Group: Default
Requires: sundials-dev = %{version}-%{release}

%description staticdev
staticdev components for the sundials package.


%prep
%setup -q -n sundials-5.8.0
cd %{_builddir}/sundials-5.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633813052
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%cmake .. -DBUILD_SHARED_LIBS=ON \
-DBUILD_STATIC_LIBS=ON \
-DBUILD_TESTING=ON \
-DMPI_ENABLE=OFF \
-DOPENMP_ENABLE=ON \
-DPTHREAD_ENABLE=ON \
-DF77_INTERFACE_ENABLE=OFF \
-DF2003_INTERFACE_ENABLE=OFF \
-DEXAMPLES_ENABLE_C=ON \
-DEXAMPLES_ENABLE_CXX=ON \
-DEXAMPLES_ENABLE_F90=OFF \
-DEXAMPLES_ENABLE_F77=OFF \
-DEXAMPLES_ENABLE_F2003=OFF \
-DEXAMPLES_INSTALL=ON \
-DEXAMPLES_INSTALL_PATH="/usr/share/sundials/examples" \
-DUSE_GENERIC_MATH=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64"
%cmake .. -DBUILD_SHARED_LIBS=ON \
-DBUILD_STATIC_LIBS=ON \
-DBUILD_TESTING=ON \
-DMPI_ENABLE=OFF \
-DOPENMP_ENABLE=ON \
-DPTHREAD_ENABLE=ON \
-DF77_INTERFACE_ENABLE=OFF \
-DF2003_INTERFACE_ENABLE=OFF \
-DEXAMPLES_ENABLE_C=ON \
-DEXAMPLES_ENABLE_CXX=ON \
-DEXAMPLES_ENABLE_F90=OFF \
-DEXAMPLES_ENABLE_F77=OFF \
-DEXAMPLES_ENABLE_F2003=OFF \
-DEXAMPLES_INSTALL=ON \
-DEXAMPLES_INSTALL_PATH="/usr/share/sundials/examples" \
-DUSE_GENERIC_MATH=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake .. -DBUILD_SHARED_LIBS=ON \
-DBUILD_STATIC_LIBS=ON \
-DBUILD_TESTING=ON \
-DMPI_ENABLE=OFF \
-DOPENMP_ENABLE=ON \
-DPTHREAD_ENABLE=ON \
-DF77_INTERFACE_ENABLE=OFF \
-DF2003_INTERFACE_ENABLE=OFF \
-DEXAMPLES_ENABLE_C=ON \
-DEXAMPLES_ENABLE_CXX=ON \
-DEXAMPLES_ENABLE_F90=OFF \
-DEXAMPLES_ENABLE_F77=OFF \
-DEXAMPLES_ENABLE_F2003=OFF \
-DEXAMPLES_INSTALL=ON \
-DEXAMPLES_INSTALL_PATH="/usr/share/sundials/examples" \
-DUSE_GENERIC_MATH=ON
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build
make test
popd
pushd clr-build-avx2
if grep -q 'avx2[^ ]*' /proc/cpuinfo ; then
    LD_LIBRARY_PATH=%{buildroot}/usr/lib64/haswell make test
fi
popd
pushd clr-build-avx512
if grep -q 'avx512[^ ]*' /proc/cpuinfo ; then
    LD_LIBRARY_PATH=%{buildroot}/usr/lib64/haswell/avx512_1 make test
fi
popd

%install
export SOURCE_DATE_EPOCH=1633813052
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sundials
cp %{_builddir}/sundials-5.8.0/LICENSE %{buildroot}/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44
cp %{_builddir}/sundials-5.8.0/src/arkode/LICENSE %{buildroot}/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44
cp %{_builddir}/sundials-5.8.0/src/cvode/LICENSE %{buildroot}/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44
cp %{_builddir}/sundials-5.8.0/src/cvodes/LICENSE %{buildroot}/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44
cp %{_builddir}/sundials-5.8.0/src/ida/LICENSE %{buildroot}/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44
cp %{_builddir}/sundials-5.8.0/src/idas/LICENSE %{buildroot}/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44
cp %{_builddir}/sundials-5.8.0/src/kinsol/LICENSE %{buildroot}/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44
pushd clr-build-avx2
%make_install_v3  || :
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build-avx512
%make_install_v4  || :
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/LICENSE

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/sundials/examples/arkode/CXX_serial/CMakeLists.txt
/usr/share/sundials/examples/arkode/CXX_serial/Makefile
/usr/share/sundials/examples/arkode/CXX_serial/README
/usr/share/sundials/examples/arkode/CXX_serial/ark_analytic_sys.cpp
/usr/share/sundials/examples/arkode/CXX_serial/ark_analytic_sys.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_heat2D.cpp
/usr/share/sundials/examples/arkode/CXX_serial/ark_heat2D.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt.cpp
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_0_-4.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_0_3_0_-10_0.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_0_4_1.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_0_5.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_1_-3_0_-10_0.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_1_-5.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_1_4.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_2_-5_0_-10.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_2_4_0_-10_0.out
/usr/share/sundials/examples/arkode/CXX_serial/ark_kpr_Mt_2_8_0_-10.out
/usr/share/sundials/examples/arkode/CXX_serial/plot_heat2D.py
/usr/share/sundials/examples/arkode/CXX_serial/plot_sol.py
/usr/share/sundials/examples/arkode/C_manyvector/CMakeLists.txt
/usr/share/sundials/examples/arkode/C_manyvector/Makefile
/usr/share/sundials/examples/arkode/C_manyvector/README
/usr/share/sundials/examples/arkode/C_manyvector/ark_brusselator1D_manyvec.c
/usr/share/sundials/examples/arkode/C_manyvector/ark_brusselator1D_manyvec.out
/usr/share/sundials/examples/arkode/C_manyvector/plot_brusselator1D.py
/usr/share/sundials/examples/arkode/C_openmp/CMakeLists.txt
/usr/share/sundials/examples/arkode/C_openmp/Makefile
/usr/share/sundials/examples/arkode/C_openmp/README
/usr/share/sundials/examples/arkode/C_openmp/ark_brusselator1D_omp.c
/usr/share/sundials/examples/arkode/C_openmp/ark_brusselator1D_omp.out
/usr/share/sundials/examples/arkode/C_openmp/ark_heat1D_omp.c
/usr/share/sundials/examples/arkode/C_openmp/ark_heat1D_omp.out
/usr/share/sundials/examples/arkode/C_openmp/plot_brusselator1D.py
/usr/share/sundials/examples/arkode/C_serial/CMakeLists.txt
/usr/share/sundials/examples/arkode/C_serial/Makefile
/usr/share/sundials/examples/arkode/C_serial/README
/usr/share/sundials/examples/arkode/C_serial/ark_KrylovDemo_prec.c
/usr/share/sundials/examples/arkode/C_serial/ark_KrylovDemo_prec.out
/usr/share/sundials/examples/arkode/C_serial/ark_analytic.c
/usr/share/sundials/examples/arkode/C_serial/ark_analytic.out
/usr/share/sundials/examples/arkode/C_serial/ark_analytic_mels.c
/usr/share/sundials/examples/arkode/C_serial/ark_analytic_mels.out
/usr/share/sundials/examples/arkode/C_serial/ark_analytic_nonlin.c
/usr/share/sundials/examples/arkode/C_serial/ark_analytic_nonlin.out
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator.c
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator.out
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator1D.c
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator1D.out
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator_1D_mri.c
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator_1D_mri.out
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator_fp.c
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator_fp.out
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator_mri.c
/usr/share/sundials/examples/arkode/C_serial/ark_brusselator_mri.out
/usr/share/sundials/examples/arkode/C_serial/ark_heat1D.c
/usr/share/sundials/examples/arkode/C_serial/ark_heat1D.out
/usr/share/sundials/examples/arkode/C_serial/ark_heat1D_adapt.c
/usr/share/sundials/examples/arkode/C_serial/ark_heat1D_adapt.out
/usr/share/sundials/examples/arkode/C_serial/ark_kpr_mri.c
/usr/share/sundials/examples/arkode/C_serial/ark_kpr_mri.out
/usr/share/sundials/examples/arkode/C_serial/ark_onewaycouple_mri.c
/usr/share/sundials/examples/arkode/C_serial/ark_onewaycouple_mri.out
/usr/share/sundials/examples/arkode/C_serial/ark_reaction_diffusion_mri.c
/usr/share/sundials/examples/arkode/C_serial/ark_reaction_diffusion_mri.out
/usr/share/sundials/examples/arkode/C_serial/ark_robertson.c
/usr/share/sundials/examples/arkode/C_serial/ark_robertson.out
/usr/share/sundials/examples/arkode/C_serial/ark_robertson_constraints.c
/usr/share/sundials/examples/arkode/C_serial/ark_robertson_constraints.out
/usr/share/sundials/examples/arkode/C_serial/ark_robertson_root.c
/usr/share/sundials/examples/arkode/C_serial/ark_robertson_root.out
/usr/share/sundials/examples/arkode/C_serial/ark_twowaycouple_mri.c
/usr/share/sundials/examples/arkode/C_serial/ark_twowaycouple_mri.out
/usr/share/sundials/examples/arkode/C_serial/plot_brusselator1D.py
/usr/share/sundials/examples/arkode/C_serial/plot_brusselator1D_FEM.py
/usr/share/sundials/examples/arkode/C_serial/plot_heat1D.py
/usr/share/sundials/examples/arkode/C_serial/plot_heat1D_adapt.py
/usr/share/sundials/examples/arkode/C_serial/plot_sol.py
/usr/share/sundials/examples/arkode/C_serial/plot_sol_log.py
/usr/share/sundials/examples/cvode/CXX_serial/CMakeLists.txt
/usr/share/sundials/examples/cvode/CXX_serial/Makefile
/usr/share/sundials/examples/cvode/CXX_serial/README
/usr/share/sundials/examples/cvode/CXX_serial/cv_heat2D.cpp
/usr/share/sundials/examples/cvode/CXX_serial/cv_heat2D.out
/usr/share/sundials/examples/cvode/CXX_serial/plot_heat2D.py
/usr/share/sundials/examples/cvode/C_openmp/CMakeLists.txt
/usr/share/sundials/examples/cvode/C_openmp/Makefile
/usr/share/sundials/examples/cvode/C_openmp/README
/usr/share/sundials/examples/cvode/C_openmp/cvAdvDiff_bnd_omp.c
/usr/share/sundials/examples/cvode/C_openmp/cvAdvDiff_bnd_omp.out
/usr/share/sundials/examples/cvode/serial/CMakeLists.txt
/usr/share/sundials/examples/cvode/serial/Makefile
/usr/share/sundials/examples/cvode/serial/README
/usr/share/sundials/examples/cvode/serial/cvAdvDiff_bnd.c
/usr/share/sundials/examples/cvode/serial/cvAdvDiff_bnd.out
/usr/share/sundials/examples/cvode/serial/cvAdvDiff_bndL.out
/usr/share/sundials/examples/cvode/serial/cvAnalytic_mels.c
/usr/share/sundials/examples/cvode/serial/cvAnalytic_mels.out
/usr/share/sundials/examples/cvode/serial/cvDirectDemo_ls.c
/usr/share/sundials/examples/cvode/serial/cvDirectDemo_ls.out
/usr/share/sundials/examples/cvode/serial/cvDisc_dns.c
/usr/share/sundials/examples/cvode/serial/cvDisc_dns.out
/usr/share/sundials/examples/cvode/serial/cvDiurnal_kry.c
/usr/share/sundials/examples/cvode/serial/cvDiurnal_kry.out
/usr/share/sundials/examples/cvode/serial/cvDiurnal_kry_bp.c
/usr/share/sundials/examples/cvode/serial/cvDiurnal_kry_bp.out
/usr/share/sundials/examples/cvode/serial/cvKrylovDemo_ls.c
/usr/share/sundials/examples/cvode/serial/cvKrylovDemo_ls.out
/usr/share/sundials/examples/cvode/serial/cvKrylovDemo_ls_0_1.out
/usr/share/sundials/examples/cvode/serial/cvKrylovDemo_ls_1.out
/usr/share/sundials/examples/cvode/serial/cvKrylovDemo_ls_2.out
/usr/share/sundials/examples/cvode/serial/cvKrylovDemo_prec.c
/usr/share/sundials/examples/cvode/serial/cvKrylovDemo_prec.out
/usr/share/sundials/examples/cvode/serial/cvParticle_dns.c
/usr/share/sundials/examples/cvode/serial/cvParticle_dns.out
/usr/share/sundials/examples/cvode/serial/cvPendulum_dns.c
/usr/share/sundials/examples/cvode/serial/cvPendulum_dns.out
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns.c
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns.out
/usr/share/sundials/examples/cvode/serial/cvRoberts_dnsL.out
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns_constraints.c
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns_constraints.out
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns_negsol.c
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns_negsol.out
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns_uw.c
/usr/share/sundials/examples/cvode/serial/cvRoberts_dns_uw.out
/usr/share/sundials/examples/cvode/serial/plot_cvParticle.py
/usr/share/sundials/examples/cvode/serial/plot_cvPendulum.py
/usr/share/sundials/examples/cvodes/C_openmp/CMakeLists.txt
/usr/share/sundials/examples/cvodes/C_openmp/Makefile
/usr/share/sundials/examples/cvodes/C_openmp/README
/usr/share/sundials/examples/cvodes/C_openmp/cvsAdvDiff_bnd_omp.c
/usr/share/sundials/examples/cvodes/C_openmp/cvsAdvDiff_bnd_omp.out
/usr/share/sundials/examples/cvodes/serial/CMakeLists.txt
/usr/share/sundials/examples/cvodes/serial/Makefile
/usr/share/sundials/examples/cvodes/serial/README
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_ASAi_bnd.c
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_ASAi_bnd.out
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_FSA_non.c
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_FSA_non_-sensi_sim_t.out
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_FSA_non_-sensi_stg_t.out
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_bnd.c
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_bnd.out
/usr/share/sundials/examples/cvodes/serial/cvsAdvDiff_bndL.out
/usr/share/sundials/examples/cvodes/serial/cvsAnalytic_mels.c
/usr/share/sundials/examples/cvodes/serial/cvsAnalytic_mels.out
/usr/share/sundials/examples/cvodes/serial/cvsDirectDemo_ls.c
/usr/share/sundials/examples/cvodes/serial/cvsDirectDemo_ls.out
/usr/share/sundials/examples/cvodes/serial/cvsDiurnal_FSA_kry.c
/usr/share/sundials/examples/cvodes/serial/cvsDiurnal_FSA_kry_-sensi_sim_t.out
/usr/share/sundials/examples/cvodes/serial/cvsDiurnal_FSA_kry_-sensi_stg_t.out
/usr/share/sundials/examples/cvodes/serial/cvsDiurnal_kry.c
/usr/share/sundials/examples/cvodes/serial/cvsDiurnal_kry.out
/usr/share/sundials/examples/cvodes/serial/cvsDiurnal_kry_bp.c
/usr/share/sundials/examples/cvodes/serial/cvsDiurnal_kry_bp.out
/usr/share/sundials/examples/cvodes/serial/cvsFoodWeb_ASAi_kry.c
/usr/share/sundials/examples/cvodes/serial/cvsFoodWeb_ASAi_kry.out
/usr/share/sundials/examples/cvodes/serial/cvsFoodWeb_ASAp_kry.c
/usr/share/sundials/examples/cvodes/serial/cvsFoodWeb_ASAp_kry.out
/usr/share/sundials/examples/cvodes/serial/cvsHessian_ASA_FSA.c
/usr/share/sundials/examples/cvodes/serial/cvsHessian_ASA_FSA.out
/usr/share/sundials/examples/cvodes/serial/cvsKrylovDemo_ls.c
/usr/share/sundials/examples/cvodes/serial/cvsKrylovDemo_ls.out
/usr/share/sundials/examples/cvodes/serial/cvsKrylovDemo_ls_1.out
/usr/share/sundials/examples/cvodes/serial/cvsKrylovDemo_ls_2.out
/usr/share/sundials/examples/cvodes/serial/cvsKrylovDemo_prec.c
/usr/share/sundials/examples/cvodes/serial/cvsKrylovDemo_prec.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_ASAi_dns.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_ASAi_dns.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_ASAi_dns_constraints.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_ASAi_dns_constraints.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_FSA_dns.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_FSA_dns_-sensi_sim_t.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_FSA_dns_-sensi_stg1_t.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_FSA_dns_Switch.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_FSA_dns_Switch.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_FSA_dns_constraints.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_FSA_dns_constraints_-sensi_stg1_t.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_dns.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_dns.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_dnsL.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_dns_constraints.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_dns_constraints.out
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_dns_uw.c
/usr/share/sundials/examples/cvodes/serial/cvsRoberts_dns_uw.out
/usr/share/sundials/examples/ida/C_openmp/CMakeLists.txt
/usr/share/sundials/examples/ida/C_openmp/Makefile
/usr/share/sundials/examples/ida/C_openmp/README
/usr/share/sundials/examples/ida/C_openmp/idaFoodWeb_bnd_omp.c
/usr/share/sundials/examples/ida/C_openmp/idaFoodWeb_bnd_omp.out
/usr/share/sundials/examples/ida/C_openmp/idaFoodWeb_kry_omp.c
/usr/share/sundials/examples/ida/C_openmp/idaFoodWeb_kry_omp.out
/usr/share/sundials/examples/ida/serial/CMakeLists.txt
/usr/share/sundials/examples/ida/serial/Makefile
/usr/share/sundials/examples/ida/serial/README
/usr/share/sundials/examples/ida/serial/idaAnalytic_mels.c
/usr/share/sundials/examples/ida/serial/idaAnalytic_mels.out
/usr/share/sundials/examples/ida/serial/idaFoodWeb_bnd.c
/usr/share/sundials/examples/ida/serial/idaFoodWeb_bnd.out
/usr/share/sundials/examples/ida/serial/idaFoodWeb_kry.c
/usr/share/sundials/examples/ida/serial/idaFoodWeb_kry.out
/usr/share/sundials/examples/ida/serial/idaHeat2D_bnd.c
/usr/share/sundials/examples/ida/serial/idaHeat2D_bnd.out
/usr/share/sundials/examples/ida/serial/idaHeat2D_kry.c
/usr/share/sundials/examples/ida/serial/idaHeat2D_kry.out
/usr/share/sundials/examples/ida/serial/idaKrylovDemo_ls.c
/usr/share/sundials/examples/ida/serial/idaKrylovDemo_ls.out
/usr/share/sundials/examples/ida/serial/idaKrylovDemo_ls_1.out
/usr/share/sundials/examples/ida/serial/idaKrylovDemo_ls_2.out
/usr/share/sundials/examples/ida/serial/idaRoberts_dns.c
/usr/share/sundials/examples/ida/serial/idaRoberts_dns.out
/usr/share/sundials/examples/ida/serial/idaSlCrank_dns.c
/usr/share/sundials/examples/ida/serial/idaSlCrank_dns.out
/usr/share/sundials/examples/idas/C_openmp/CMakeLists.txt
/usr/share/sundials/examples/idas/C_openmp/Makefile
/usr/share/sundials/examples/idas/C_openmp/README
/usr/share/sundials/examples/idas/C_openmp/idasFoodWeb_bnd_omp.c
/usr/share/sundials/examples/idas/C_openmp/idasFoodWeb_bnd_omp.out
/usr/share/sundials/examples/idas/C_openmp/idasFoodWeb_kry_omp.c
/usr/share/sundials/examples/idas/C_openmp/idasFoodWeb_kry_omp.out
/usr/share/sundials/examples/idas/serial/CMakeLists.txt
/usr/share/sundials/examples/idas/serial/Makefile
/usr/share/sundials/examples/idas/serial/README
/usr/share/sundials/examples/idas/serial/idasAkzoNob_ASAi_dns.c
/usr/share/sundials/examples/idas/serial/idasAkzoNob_ASAi_dns.out
/usr/share/sundials/examples/idas/serial/idasAkzoNob_dns.c
/usr/share/sundials/examples/idas/serial/idasAkzoNob_dns.out
/usr/share/sundials/examples/idas/serial/idasAnalytic_mels.c
/usr/share/sundials/examples/idas/serial/idasAnalytic_mels.out
/usr/share/sundials/examples/idas/serial/idasFoodWeb_bnd.c
/usr/share/sundials/examples/idas/serial/idasFoodWeb_bnd.out
/usr/share/sundials/examples/idas/serial/idasHeat2D_bnd.c
/usr/share/sundials/examples/idas/serial/idasHeat2D_bnd.out
/usr/share/sundials/examples/idas/serial/idasHeat2D_kry.c
/usr/share/sundials/examples/idas/serial/idasHeat2D_kry.out
/usr/share/sundials/examples/idas/serial/idasHessian_ASA_FSA.c
/usr/share/sundials/examples/idas/serial/idasHessian_ASA_FSA.out
/usr/share/sundials/examples/idas/serial/idasKrylovDemo_ls.c
/usr/share/sundials/examples/idas/serial/idasKrylovDemo_ls.out
/usr/share/sundials/examples/idas/serial/idasKrylovDemo_ls_1.out
/usr/share/sundials/examples/idas/serial/idasKrylovDemo_ls_2.out
/usr/share/sundials/examples/idas/serial/idasRoberts_ASAi_dns.c
/usr/share/sundials/examples/idas/serial/idasRoberts_ASAi_dns.out
/usr/share/sundials/examples/idas/serial/idasRoberts_FSA_dns.c
/usr/share/sundials/examples/idas/serial/idasRoberts_FSA_dns_-sensi_stg_t.out
/usr/share/sundials/examples/idas/serial/idasRoberts_dns.c
/usr/share/sundials/examples/idas/serial/idasRoberts_dns.out
/usr/share/sundials/examples/idas/serial/idasSlCrank_FSA_dns.c
/usr/share/sundials/examples/idas/serial/idasSlCrank_FSA_dns.out
/usr/share/sundials/examples/idas/serial/idasSlCrank_dns.c
/usr/share/sundials/examples/idas/serial/idasSlCrank_dns.out
/usr/share/sundials/examples/kinsol/C_openmp/CMakeLists.txt
/usr/share/sundials/examples/kinsol/C_openmp/Makefile
/usr/share/sundials/examples/kinsol/C_openmp/README
/usr/share/sundials/examples/kinsol/C_openmp/kinFoodWeb_kry_omp.c
/usr/share/sundials/examples/kinsol/C_openmp/kinFoodWeb_kry_omp.out
/usr/share/sundials/examples/kinsol/serial/CMakeLists.txt
/usr/share/sundials/examples/kinsol/serial/Makefile
/usr/share/sundials/examples/kinsol/serial/README
/usr/share/sundials/examples/kinsol/serial/kinAnalytic_fp.c
/usr/share/sundials/examples/kinsol/serial/kinAnalytic_fp.out
/usr/share/sundials/examples/kinsol/serial/kinFerTron_dns.c
/usr/share/sundials/examples/kinsol/serial/kinFerTron_dns.out
/usr/share/sundials/examples/kinsol/serial/kinFoodWeb_kry.c
/usr/share/sundials/examples/kinsol/serial/kinFoodWeb_kry.out
/usr/share/sundials/examples/kinsol/serial/kinKrylovDemo_ls.c
/usr/share/sundials/examples/kinsol/serial/kinKrylovDemo_ls.out
/usr/share/sundials/examples/kinsol/serial/kinLaplace_bnd.c
/usr/share/sundials/examples/kinsol/serial/kinLaplace_bnd.out
/usr/share/sundials/examples/kinsol/serial/kinLaplace_picard_bnd.c
/usr/share/sundials/examples/kinsol/serial/kinLaplace_picard_bnd.out
/usr/share/sundials/examples/kinsol/serial/kinLaplace_picard_kry.c
/usr/share/sundials/examples/kinsol/serial/kinLaplace_picard_kry.out
/usr/share/sundials/examples/kinsol/serial/kinRoberts_fp.c
/usr/share/sundials/examples/kinsol/serial/kinRoberts_fp.out
/usr/share/sundials/examples/kinsol/serial/kinRoboKin_dns.c
/usr/share/sundials/examples/kinsol/serial/kinRoboKin_dns.out
/usr/share/sundials/examples/nvector/C_openmp/CMakeLists.txt
/usr/share/sundials/examples/nvector/C_openmp/Makefile
/usr/share/sundials/examples/nvector/C_openmp/sundials_nvector.c
/usr/share/sundials/examples/nvector/C_openmp/test_nvector.c
/usr/share/sundials/examples/nvector/C_openmp/test_nvector.h
/usr/share/sundials/examples/nvector/C_openmp/test_nvector_openmp.c
/usr/share/sundials/examples/nvector/manyvector/CMakeLists.txt
/usr/share/sundials/examples/nvector/manyvector/Makefile
/usr/share/sundials/examples/nvector/manyvector/sundials_nvector.c
/usr/share/sundials/examples/nvector/manyvector/test_nvector.c
/usr/share/sundials/examples/nvector/manyvector/test_nvector.h
/usr/share/sundials/examples/nvector/manyvector/test_nvector_manyvector.c
/usr/share/sundials/examples/nvector/pthreads/CMakeLists.txt
/usr/share/sundials/examples/nvector/pthreads/Makefile
/usr/share/sundials/examples/nvector/pthreads/sundials_nvector.c
/usr/share/sundials/examples/nvector/pthreads/test_nvector.c
/usr/share/sundials/examples/nvector/pthreads/test_nvector.h
/usr/share/sundials/examples/nvector/pthreads/test_nvector_pthreads.c
/usr/share/sundials/examples/nvector/serial/CMakeLists.txt
/usr/share/sundials/examples/nvector/serial/Makefile
/usr/share/sundials/examples/nvector/serial/sundials_nvector.c
/usr/share/sundials/examples/nvector/serial/test_nvector.c
/usr/share/sundials/examples/nvector/serial/test_nvector.h
/usr/share/sundials/examples/nvector/serial/test_nvector_serial.c
/usr/share/sundials/examples/sunlinsol/band/CMakeLists.txt
/usr/share/sundials/examples/sunlinsol/band/Makefile
/usr/share/sundials/examples/sunlinsol/band/sundials_linearsolver.c
/usr/share/sundials/examples/sunlinsol/band/sundials_matrix.c
/usr/share/sundials/examples/sunlinsol/band/sundials_nvector.c
/usr/share/sundials/examples/sunlinsol/band/test_sunlinsol.c
/usr/share/sundials/examples/sunlinsol/band/test_sunlinsol.h
/usr/share/sundials/examples/sunlinsol/band/test_sunlinsol_band.c
/usr/share/sundials/examples/sunlinsol/dense/CMakeLists.txt
/usr/share/sundials/examples/sunlinsol/dense/Makefile
/usr/share/sundials/examples/sunlinsol/dense/sundials_linearsolver.c
/usr/share/sundials/examples/sunlinsol/dense/sundials_matrix.c
/usr/share/sundials/examples/sunlinsol/dense/sundials_nvector.c
/usr/share/sundials/examples/sunlinsol/dense/test_sunlinsol.c
/usr/share/sundials/examples/sunlinsol/dense/test_sunlinsol.h
/usr/share/sundials/examples/sunlinsol/dense/test_sunlinsol_dense.c
/usr/share/sundials/examples/sunlinsol/pcg/serial/CMakeLists.txt
/usr/share/sundials/examples/sunlinsol/pcg/serial/Makefile
/usr/share/sundials/examples/sunlinsol/pcg/serial/sundials_linearsolver.c
/usr/share/sundials/examples/sunlinsol/pcg/serial/sundials_nvector.c
/usr/share/sundials/examples/sunlinsol/pcg/serial/test_sunlinsol.c
/usr/share/sundials/examples/sunlinsol/pcg/serial/test_sunlinsol.h
/usr/share/sundials/examples/sunlinsol/pcg/serial/test_sunlinsol_pcg_serial.c
/usr/share/sundials/examples/sunlinsol/spbcgs/serial/CMakeLists.txt
/usr/share/sundials/examples/sunlinsol/spbcgs/serial/Makefile
/usr/share/sundials/examples/sunlinsol/spbcgs/serial/sundials_linearsolver.c
/usr/share/sundials/examples/sunlinsol/spbcgs/serial/sundials_nvector.c
/usr/share/sundials/examples/sunlinsol/spbcgs/serial/test_sunlinsol.c
/usr/share/sundials/examples/sunlinsol/spbcgs/serial/test_sunlinsol.h
/usr/share/sundials/examples/sunlinsol/spbcgs/serial/test_sunlinsol_spbcgs_serial.c
/usr/share/sundials/examples/sunlinsol/spfgmr/serial/CMakeLists.txt
/usr/share/sundials/examples/sunlinsol/spfgmr/serial/Makefile
/usr/share/sundials/examples/sunlinsol/spfgmr/serial/sundials_linearsolver.c
/usr/share/sundials/examples/sunlinsol/spfgmr/serial/sundials_nvector.c
/usr/share/sundials/examples/sunlinsol/spfgmr/serial/test_sunlinsol.c
/usr/share/sundials/examples/sunlinsol/spfgmr/serial/test_sunlinsol.h
/usr/share/sundials/examples/sunlinsol/spfgmr/serial/test_sunlinsol_spfgmr_serial.c
/usr/share/sundials/examples/sunlinsol/spgmr/serial/CMakeLists.txt
/usr/share/sundials/examples/sunlinsol/spgmr/serial/Makefile
/usr/share/sundials/examples/sunlinsol/spgmr/serial/sundials_linearsolver.c
/usr/share/sundials/examples/sunlinsol/spgmr/serial/sundials_nvector.c
/usr/share/sundials/examples/sunlinsol/spgmr/serial/test_sunlinsol.c
/usr/share/sundials/examples/sunlinsol/spgmr/serial/test_sunlinsol.h
/usr/share/sundials/examples/sunlinsol/spgmr/serial/test_sunlinsol_spgmr_serial.c
/usr/share/sundials/examples/sunlinsol/sptfqmr/serial/CMakeLists.txt
/usr/share/sundials/examples/sunlinsol/sptfqmr/serial/Makefile
/usr/share/sundials/examples/sunlinsol/sptfqmr/serial/sundials_linearsolver.c
/usr/share/sundials/examples/sunlinsol/sptfqmr/serial/sundials_nvector.c
/usr/share/sundials/examples/sunlinsol/sptfqmr/serial/test_sunlinsol.c
/usr/share/sundials/examples/sunlinsol/sptfqmr/serial/test_sunlinsol.h
/usr/share/sundials/examples/sunlinsol/sptfqmr/serial/test_sunlinsol_sptfqmr_serial.c
/usr/share/sundials/examples/sunmatrix/band/CMakeLists.txt
/usr/share/sundials/examples/sunmatrix/band/Makefile
/usr/share/sundials/examples/sunmatrix/band/sundials_matrix.c
/usr/share/sundials/examples/sunmatrix/band/sundials_nvector.c
/usr/share/sundials/examples/sunmatrix/band/test_sunmatrix.c
/usr/share/sundials/examples/sunmatrix/band/test_sunmatrix.h
/usr/share/sundials/examples/sunmatrix/band/test_sunmatrix_band.c
/usr/share/sundials/examples/sunmatrix/dense/CMakeLists.txt
/usr/share/sundials/examples/sunmatrix/dense/Makefile
/usr/share/sundials/examples/sunmatrix/dense/sundials_matrix.c
/usr/share/sundials/examples/sunmatrix/dense/sundials_nvector.c
/usr/share/sundials/examples/sunmatrix/dense/test_sunmatrix.c
/usr/share/sundials/examples/sunmatrix/dense/test_sunmatrix.h
/usr/share/sundials/examples/sunmatrix/dense/test_sunmatrix_dense.c
/usr/share/sundials/examples/sunmatrix/sparse/CMakeLists.txt
/usr/share/sundials/examples/sunmatrix/sparse/Makefile
/usr/share/sundials/examples/sunmatrix/sparse/sundials_matrix.c
/usr/share/sundials/examples/sunmatrix/sparse/sundials_nvector.c
/usr/share/sundials/examples/sunmatrix/sparse/test_sunmatrix.c
/usr/share/sundials/examples/sunmatrix/sparse/test_sunmatrix.h
/usr/share/sundials/examples/sunmatrix/sparse/test_sunmatrix_sparse.c
/usr/share/sundials/examples/sunnonlinsol/fixedpoint/CMakeLists.txt
/usr/share/sundials/examples/sunnonlinsol/fixedpoint/Makefile
/usr/share/sundials/examples/sunnonlinsol/fixedpoint/test_sunnonlinsol_fixedpoint.c
/usr/share/sundials/examples/sunnonlinsol/newton/CMakeLists.txt
/usr/share/sundials/examples/sunnonlinsol/newton/Makefile
/usr/share/sundials/examples/sunnonlinsol/newton/test_sunnonlinsol_newton.c

%files dev
%defattr(-,root,root,-)
/usr/include/arkode/arkode.h
/usr/include/arkode/arkode_arkstep.h
/usr/include/arkode/arkode_bandpre.h
/usr/include/arkode/arkode_bbdpre.h
/usr/include/arkode/arkode_butcher.h
/usr/include/arkode/arkode_butcher_dirk.h
/usr/include/arkode/arkode_butcher_erk.h
/usr/include/arkode/arkode_erkstep.h
/usr/include/arkode/arkode_ls.h
/usr/include/arkode/arkode_mristep.h
/usr/include/cvode/cvode.h
/usr/include/cvode/cvode_bandpre.h
/usr/include/cvode/cvode_bbdpre.h
/usr/include/cvode/cvode_diag.h
/usr/include/cvode/cvode_direct.h
/usr/include/cvode/cvode_ls.h
/usr/include/cvode/cvode_proj.h
/usr/include/cvode/cvode_spils.h
/usr/include/cvodes/cvodes.h
/usr/include/cvodes/cvodes_bandpre.h
/usr/include/cvodes/cvodes_bbdpre.h
/usr/include/cvodes/cvodes_diag.h
/usr/include/cvodes/cvodes_direct.h
/usr/include/cvodes/cvodes_ls.h
/usr/include/cvodes/cvodes_spils.h
/usr/include/ida/ida.h
/usr/include/ida/ida_bbdpre.h
/usr/include/ida/ida_direct.h
/usr/include/ida/ida_ls.h
/usr/include/ida/ida_spils.h
/usr/include/idas/idas.h
/usr/include/idas/idas_bbdpre.h
/usr/include/idas/idas_direct.h
/usr/include/idas/idas_ls.h
/usr/include/idas/idas_spils.h
/usr/include/kinsol/kinsol.h
/usr/include/kinsol/kinsol_bbdpre.h
/usr/include/kinsol/kinsol_direct.h
/usr/include/kinsol/kinsol_ls.h
/usr/include/kinsol/kinsol_spils.h
/usr/include/nvector/nvector_manyvector.h
/usr/include/nvector/nvector_openmp.h
/usr/include/nvector/nvector_pthreads.h
/usr/include/nvector/nvector_serial.h
/usr/include/sundials/LICENSE
/usr/include/sundials/NOTICE
/usr/include/sundials/sundials_band.h
/usr/include/sundials/sundials_config.h
/usr/include/sundials/sundials_dense.h
/usr/include/sundials/sundials_direct.h
/usr/include/sundials/sundials_export.h
/usr/include/sundials/sundials_fconfig.h
/usr/include/sundials/sundials_fnvector.h
/usr/include/sundials/sundials_futils.h
/usr/include/sundials/sundials_iterative.h
/usr/include/sundials/sundials_linearsolver.h
/usr/include/sundials/sundials_math.h
/usr/include/sundials/sundials_matrix.h
/usr/include/sundials/sundials_memory.h
/usr/include/sundials/sundials_mpi_types.h
/usr/include/sundials/sundials_nonlinearsolver.h
/usr/include/sundials/sundials_nvector.h
/usr/include/sundials/sundials_types.h
/usr/include/sundials/sundials_version.h
/usr/include/sunlinsol/sunlinsol_band.h
/usr/include/sunlinsol/sunlinsol_dense.h
/usr/include/sunlinsol/sunlinsol_pcg.h
/usr/include/sunlinsol/sunlinsol_spbcgs.h
/usr/include/sunlinsol/sunlinsol_spfgmr.h
/usr/include/sunlinsol/sunlinsol_spgmr.h
/usr/include/sunlinsol/sunlinsol_sptfqmr.h
/usr/include/sunmatrix/sunmatrix_band.h
/usr/include/sunmatrix/sunmatrix_dense.h
/usr/include/sunmatrix/sunmatrix_sparse.h
/usr/include/sunnonlinsol/sunnonlinsol_fixedpoint.h
/usr/include/sunnonlinsol/sunnonlinsol_newton.h
/usr/lib64/cmake/sundials/SUNDIALSConfig.cmake
/usr/lib64/cmake/sundials/SUNDIALSConfigVersion.cmake
/usr/lib64/cmake/sundials/SUNDIALSTargets-relwithdebinfo.cmake
/usr/lib64/cmake/sundials/SUNDIALSTargets.cmake
/usr/lib64/libsundials_arkode.so
/usr/lib64/libsundials_cvode.so
/usr/lib64/libsundials_cvodes.so
/usr/lib64/libsundials_generic.so
/usr/lib64/libsundials_ida.so
/usr/lib64/libsundials_idas.so
/usr/lib64/libsundials_kinsol.so
/usr/lib64/libsundials_nvecmanyvector.so
/usr/lib64/libsundials_nvecopenmp.so
/usr/lib64/libsundials_nvecpthreads.so
/usr/lib64/libsundials_nvecserial.so
/usr/lib64/libsundials_sunlinsolband.so
/usr/lib64/libsundials_sunlinsoldense.so
/usr/lib64/libsundials_sunlinsolpcg.so
/usr/lib64/libsundials_sunlinsolspbcgs.so
/usr/lib64/libsundials_sunlinsolspfgmr.so
/usr/lib64/libsundials_sunlinsolspgmr.so
/usr/lib64/libsundials_sunlinsolsptfqmr.so
/usr/lib64/libsundials_sunmatrixband.so
/usr/lib64/libsundials_sunmatrixdense.so
/usr/lib64/libsundials_sunmatrixsparse.so
/usr/lib64/libsundials_sunnonlinsolfixedpoint.so
/usr/lib64/libsundials_sunnonlinsolnewton.so

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-sundials

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsundials_arkode.so.4
/usr/lib64/libsundials_arkode.so.4.8.0
/usr/lib64/libsundials_cvode.so.5
/usr/lib64/libsundials_cvode.so.5.8.0
/usr/lib64/libsundials_cvodes.so.5
/usr/lib64/libsundials_cvodes.so.5.8.0
/usr/lib64/libsundials_generic.so.5
/usr/lib64/libsundials_generic.so.5.8.0
/usr/lib64/libsundials_ida.so.5
/usr/lib64/libsundials_ida.so.5.8.0
/usr/lib64/libsundials_idas.so.4
/usr/lib64/libsundials_idas.so.4.8.0
/usr/lib64/libsundials_kinsol.so.5
/usr/lib64/libsundials_kinsol.so.5.8.0
/usr/lib64/libsundials_nvecmanyvector.so.5
/usr/lib64/libsundials_nvecmanyvector.so.5.8.0
/usr/lib64/libsundials_nvecopenmp.so.5
/usr/lib64/libsundials_nvecopenmp.so.5.8.0
/usr/lib64/libsundials_nvecpthreads.so.5
/usr/lib64/libsundials_nvecpthreads.so.5.8.0
/usr/lib64/libsundials_nvecserial.so.5
/usr/lib64/libsundials_nvecserial.so.5.8.0
/usr/lib64/libsundials_sunlinsolband.so.3.8.0
/usr/lib64/libsundials_sunlinsoldense.so.3.8.0
/usr/lib64/libsundials_sunlinsolpcg.so.3.8.0
/usr/lib64/libsundials_sunlinsolspbcgs.so.3.8.0
/usr/lib64/libsundials_sunlinsolspfgmr.so.3.8.0
/usr/lib64/libsundials_sunlinsolspgmr.so.3.8.0
/usr/lib64/libsundials_sunlinsolsptfqmr.so.3.8.0
/usr/lib64/libsundials_sunmatrixband.so.3
/usr/lib64/libsundials_sunmatrixband.so.3.8.0
/usr/lib64/libsundials_sunmatrixdense.so.3
/usr/lib64/libsundials_sunmatrixdense.so.3.8.0
/usr/lib64/libsundials_sunmatrixsparse.so.3
/usr/lib64/libsundials_sunmatrixsparse.so.3.8.0
/usr/lib64/libsundials_sunnonlinsolfixedpoint.so.2.8.0
/usr/lib64/libsundials_sunnonlinsolnewton.so.2.8.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sundials/acc2df45ed3189e9c29543b93af0c99320daab44

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libsundials_arkode.a
/usr/lib64/libsundials_cvode.a
/usr/lib64/libsundials_cvodes.a
/usr/lib64/libsundials_generic.a
/usr/lib64/libsundials_ida.a
/usr/lib64/libsundials_idas.a
/usr/lib64/libsundials_kinsol.a
/usr/lib64/libsundials_nvecmanyvector.a
/usr/lib64/libsundials_nvecopenmp.a
/usr/lib64/libsundials_nvecpthreads.a
/usr/lib64/libsundials_nvecserial.a
/usr/lib64/libsundials_sunlinsolband.a
/usr/lib64/libsundials_sunlinsoldense.a
/usr/lib64/libsundials_sunlinsolpcg.a
/usr/lib64/libsundials_sunlinsolspbcgs.a
/usr/lib64/libsundials_sunlinsolspfgmr.a
/usr/lib64/libsundials_sunlinsolspgmr.a
/usr/lib64/libsundials_sunlinsolsptfqmr.a
/usr/lib64/libsundials_sunmatrixband.a
/usr/lib64/libsundials_sunmatrixdense.a
/usr/lib64/libsundials_sunmatrixsparse.a
/usr/lib64/libsundials_sunnonlinsolfixedpoint.a
/usr/lib64/libsundials_sunnonlinsolnewton.a
