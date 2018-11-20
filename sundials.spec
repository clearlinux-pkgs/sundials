#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sundials
Version  : 3.2.1
Release  : 12
URL      : https://github.com/LLNL/sundials/archive/v3.2.1.tar.gz
Source0  : https://github.com/LLNL/sundials/archive/v3.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sundials-lib = %{version}-%{release}
Requires: sundials-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : glibc-dev
BuildRequires : openblas
BuildRequires : openmpi-dev
BuildRequires : python3

%description
KINSOL
Release 3.2.1, Oct 2018
Aaron Collier, Alan C. Hindmarsh, Radu Serban, and Carol S. Woodward
Center for Applied Scientific Computing, LLNL

%package dev
Summary: dev components for the sundials package.
Group: Development
Requires: sundials-lib = %{version}-%{release}
Provides: sundials-devel = %{version}-%{release}

%description dev
dev components for the sundials package.


%package lib
Summary: lib components for the sundials package.
Group: Libraries
Requires: sundials-license = %{version}-%{release}

%description lib
lib components for the sundials package.


%package license
Summary: license components for the sundials package.
Group: Default

%description license
license components for the sundials package.


%prep
%setup -q -n sundials-3.2.1
pushd ..
cp -a sundials-3.2.1 buildavx2
popd
pushd ..
cp -a sundials-3.2.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542756772
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1542756772
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sundials
cp LICENSE %{buildroot}/usr/share/package-licenses/sundials/LICENSE
cp src/arkode/LICENSE %{buildroot}/usr/share/package-licenses/sundials/src_arkode_LICENSE
cp src/cvode/LICENSE %{buildroot}/usr/share/package-licenses/sundials/src_cvode_LICENSE
cp src/cvodes/LICENSE %{buildroot}/usr/share/package-licenses/sundials/src_cvodes_LICENSE
cp src/ida/LICENSE %{buildroot}/usr/share/package-licenses/sundials/src_ida_LICENSE
cp src/idas/LICENSE %{buildroot}/usr/share/package-licenses/sundials/src_idas_LICENSE
cp src/kinsol/LICENSE %{buildroot}/usr/share/package-licenses/sundials/src_kinsol_LICENSE
pushd clr-build-avx512
%make_install_avx512  || :
popd
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/examples/arkode/C_serial/CMakeLists.txt
/usr/examples/arkode/C_serial/Makefile
/usr/examples/arkode/C_serial/README
/usr/examples/arkode/C_serial/ark_KrylovDemo_prec.c
/usr/examples/arkode/C_serial/ark_KrylovDemo_prec.out
/usr/examples/arkode/C_serial/ark_analytic.c
/usr/examples/arkode/C_serial/ark_analytic.out
/usr/examples/arkode/C_serial/ark_analytic_nonlin.c
/usr/examples/arkode/C_serial/ark_analytic_nonlin.out
/usr/examples/arkode/C_serial/ark_brusselator.c
/usr/examples/arkode/C_serial/ark_brusselator.out
/usr/examples/arkode/C_serial/ark_brusselator1D.c
/usr/examples/arkode/C_serial/ark_brusselator1D.out
/usr/examples/arkode/C_serial/ark_brusselator_fp.c
/usr/examples/arkode/C_serial/ark_brusselator_fp.out
/usr/examples/arkode/C_serial/ark_heat1D.c
/usr/examples/arkode/C_serial/ark_heat1D.out
/usr/examples/arkode/C_serial/ark_heat1D_adapt.c
/usr/examples/arkode/C_serial/ark_heat1D_adapt.out
/usr/examples/arkode/C_serial/ark_robertson.c
/usr/examples/arkode/C_serial/ark_robertson.out
/usr/examples/arkode/C_serial/ark_robertson_root.c
/usr/examples/arkode/C_serial/ark_robertson_root.out
/usr/examples/arkode/C_serial/plot_brusselator1D.py
/usr/examples/arkode/C_serial/plot_brusselator1D_FEM.py
/usr/examples/arkode/C_serial/plot_heat1D.py
/usr/examples/arkode/C_serial/plot_heat1D_adapt.py
/usr/examples/arkode/C_serial/plot_sol.py
/usr/examples/arkode/C_serial/plot_sol_log.py
/usr/examples/cvode/serial/CMakeLists.txt
/usr/examples/cvode/serial/Makefile
/usr/examples/cvode/serial/README
/usr/examples/cvode/serial/cvAdvDiff_bnd.c
/usr/examples/cvode/serial/cvAdvDiff_bnd.out
/usr/examples/cvode/serial/cvDirectDemo_ls.c
/usr/examples/cvode/serial/cvDirectDemo_ls.out
/usr/examples/cvode/serial/cvDisc_dns.c
/usr/examples/cvode/serial/cvDisc_dns.out
/usr/examples/cvode/serial/cvDiurnal_kry.c
/usr/examples/cvode/serial/cvDiurnal_kry.out
/usr/examples/cvode/serial/cvDiurnal_kry_bp.c
/usr/examples/cvode/serial/cvDiurnal_kry_bp.out
/usr/examples/cvode/serial/cvKrylovDemo_ls.c
/usr/examples/cvode/serial/cvKrylovDemo_ls.out
/usr/examples/cvode/serial/cvKrylovDemo_prec.c
/usr/examples/cvode/serial/cvKrylovDemo_prec.out
/usr/examples/cvode/serial/cvRoberts_dns.c
/usr/examples/cvode/serial/cvRoberts_dns.out
/usr/examples/cvode/serial/cvRoberts_dns_constraints.c
/usr/examples/cvode/serial/cvRoberts_dns_constraints.out
/usr/examples/cvode/serial/cvRoberts_dns_negsol.c
/usr/examples/cvode/serial/cvRoberts_dns_negsol.out
/usr/examples/cvode/serial/cvRoberts_dns_uw.c
/usr/examples/cvode/serial/cvRoberts_dns_uw.out
/usr/examples/cvodes/serial/CMakeLists.txt
/usr/examples/cvodes/serial/Makefile
/usr/examples/cvodes/serial/README
/usr/examples/cvodes/serial/cvsAdvDiff_ASAi_bnd.c
/usr/examples/cvodes/serial/cvsAdvDiff_ASAi_bnd.out
/usr/examples/cvodes/serial/cvsAdvDiff_FSA_non.c
/usr/examples/cvodes/serial/cvsAdvDiff_bnd.c
/usr/examples/cvodes/serial/cvsAdvDiff_bnd.out
/usr/examples/cvodes/serial/cvsDirectDemo_ls.c
/usr/examples/cvodes/serial/cvsDirectDemo_ls.out
/usr/examples/cvodes/serial/cvsDiurnal_FSA_kry.c
/usr/examples/cvodes/serial/cvsDiurnal_kry.c
/usr/examples/cvodes/serial/cvsDiurnal_kry.out
/usr/examples/cvodes/serial/cvsDiurnal_kry_bp.c
/usr/examples/cvodes/serial/cvsDiurnal_kry_bp.out
/usr/examples/cvodes/serial/cvsFoodWeb_ASAi_kry.c
/usr/examples/cvodes/serial/cvsFoodWeb_ASAi_kry.out
/usr/examples/cvodes/serial/cvsFoodWeb_ASAp_kry.c
/usr/examples/cvodes/serial/cvsFoodWeb_ASAp_kry.out
/usr/examples/cvodes/serial/cvsHessian_ASA_FSA.c
/usr/examples/cvodes/serial/cvsHessian_ASA_FSA.out
/usr/examples/cvodes/serial/cvsKrylovDemo_ls.c
/usr/examples/cvodes/serial/cvsKrylovDemo_ls.out
/usr/examples/cvodes/serial/cvsKrylovDemo_prec.c
/usr/examples/cvodes/serial/cvsKrylovDemo_prec.out
/usr/examples/cvodes/serial/cvsRoberts_ASAi_dns.c
/usr/examples/cvodes/serial/cvsRoberts_ASAi_dns.out
/usr/examples/cvodes/serial/cvsRoberts_ASAi_dns_constraints.c
/usr/examples/cvodes/serial/cvsRoberts_ASAi_dns_constraints.out
/usr/examples/cvodes/serial/cvsRoberts_FSA_dns.c
/usr/examples/cvodes/serial/cvsRoberts_FSA_dns_Switch.c
/usr/examples/cvodes/serial/cvsRoberts_FSA_dns_Switch.out
/usr/examples/cvodes/serial/cvsRoberts_FSA_dns_constraints.c
/usr/examples/cvodes/serial/cvsRoberts_dns.c
/usr/examples/cvodes/serial/cvsRoberts_dns.out
/usr/examples/cvodes/serial/cvsRoberts_dns_constraints.c
/usr/examples/cvodes/serial/cvsRoberts_dns_constraints.out
/usr/examples/cvodes/serial/cvsRoberts_dns_uw.c
/usr/examples/cvodes/serial/cvsRoberts_dns_uw.out
/usr/examples/ida/serial/CMakeLists.txt
/usr/examples/ida/serial/Makefile
/usr/examples/ida/serial/README
/usr/examples/ida/serial/idaFoodWeb_bnd.c
/usr/examples/ida/serial/idaFoodWeb_bnd.out
/usr/examples/ida/serial/idaFoodWeb_kry.c
/usr/examples/ida/serial/idaFoodWeb_kry.out
/usr/examples/ida/serial/idaHeat2D_bnd.c
/usr/examples/ida/serial/idaHeat2D_bnd.out
/usr/examples/ida/serial/idaHeat2D_kry.c
/usr/examples/ida/serial/idaHeat2D_kry.out
/usr/examples/ida/serial/idaKrylovDemo_ls.c
/usr/examples/ida/serial/idaKrylovDemo_ls.out
/usr/examples/ida/serial/idaRoberts_dns.c
/usr/examples/ida/serial/idaRoberts_dns.out
/usr/examples/ida/serial/idaSlCrank_dns.c
/usr/examples/ida/serial/idaSlCrank_dns.out
/usr/examples/idas/serial/CMakeLists.txt
/usr/examples/idas/serial/Makefile
/usr/examples/idas/serial/README
/usr/examples/idas/serial/idasAkzoNob_ASAi_dns.c
/usr/examples/idas/serial/idasAkzoNob_ASAi_dns.out
/usr/examples/idas/serial/idasAkzoNob_dns.c
/usr/examples/idas/serial/idasAkzoNob_dns.out
/usr/examples/idas/serial/idasFoodWeb_bnd.c
/usr/examples/idas/serial/idasFoodWeb_bnd.out
/usr/examples/idas/serial/idasHeat2D_bnd.c
/usr/examples/idas/serial/idasHeat2D_bnd.out
/usr/examples/idas/serial/idasHeat2D_kry.c
/usr/examples/idas/serial/idasHeat2D_kry.out
/usr/examples/idas/serial/idasHessian_ASA_FSA.c
/usr/examples/idas/serial/idasHessian_ASA_FSA.out
/usr/examples/idas/serial/idasKrylovDemo_ls.c
/usr/examples/idas/serial/idasKrylovDemo_ls.out
/usr/examples/idas/serial/idasRoberts_ASAi_dns.c
/usr/examples/idas/serial/idasRoberts_ASAi_dns.out
/usr/examples/idas/serial/idasRoberts_FSA_dns.c
/usr/examples/idas/serial/idasRoberts_dns.c
/usr/examples/idas/serial/idasRoberts_dns.out
/usr/examples/idas/serial/idasSlCrank_FSA_dns.c
/usr/examples/idas/serial/idasSlCrank_FSA_dns.out
/usr/examples/idas/serial/idasSlCrank_dns.c
/usr/examples/idas/serial/idasSlCrank_dns.out
/usr/examples/kinsol/serial/CMakeLists.txt
/usr/examples/kinsol/serial/Makefile
/usr/examples/kinsol/serial/README
/usr/examples/kinsol/serial/kinFerTron_dns.c
/usr/examples/kinsol/serial/kinFerTron_dns.out
/usr/examples/kinsol/serial/kinFoodWeb_kry.c
/usr/examples/kinsol/serial/kinFoodWeb_kry.out
/usr/examples/kinsol/serial/kinKrylovDemo_ls.c
/usr/examples/kinsol/serial/kinKrylovDemo_ls.out
/usr/examples/kinsol/serial/kinLaplace_bnd.c
/usr/examples/kinsol/serial/kinLaplace_bnd.out
/usr/examples/kinsol/serial/kinLaplace_picard_bnd.c
/usr/examples/kinsol/serial/kinLaplace_picard_bnd.out
/usr/examples/kinsol/serial/kinRoberts_fp.c
/usr/examples/kinsol/serial/kinRoberts_fp.out
/usr/examples/kinsol/serial/kinRoboKin_dns.c
/usr/examples/kinsol/serial/kinRoboKin_dns.out
/usr/examples/nvector/serial/CMakeLists.txt
/usr/examples/nvector/serial/Makefile
/usr/examples/nvector/serial/sundials_nvector.c
/usr/examples/nvector/serial/test_nvector.c
/usr/examples/nvector/serial/test_nvector.h
/usr/examples/nvector/serial/test_nvector_serial.c
/usr/examples/sunlinsol/band/CMakeLists.txt
/usr/examples/sunlinsol/band/Makefile
/usr/examples/sunlinsol/band/sundials_linearsolver.c
/usr/examples/sunlinsol/band/sundials_matrix.c
/usr/examples/sunlinsol/band/sundials_nvector.c
/usr/examples/sunlinsol/band/test_sunlinsol.c
/usr/examples/sunlinsol/band/test_sunlinsol.h
/usr/examples/sunlinsol/band/test_sunlinsol_band.c
/usr/examples/sunlinsol/dense/CMakeLists.txt
/usr/examples/sunlinsol/dense/Makefile
/usr/examples/sunlinsol/dense/sundials_linearsolver.c
/usr/examples/sunlinsol/dense/sundials_matrix.c
/usr/examples/sunlinsol/dense/sundials_nvector.c
/usr/examples/sunlinsol/dense/test_sunlinsol.c
/usr/examples/sunlinsol/dense/test_sunlinsol.h
/usr/examples/sunlinsol/dense/test_sunlinsol_dense.c
/usr/examples/sunlinsol/pcg/serial/CMakeLists.txt
/usr/examples/sunlinsol/pcg/serial/Makefile
/usr/examples/sunlinsol/pcg/serial/sundials_linearsolver.c
/usr/examples/sunlinsol/pcg/serial/sundials_nvector.c
/usr/examples/sunlinsol/pcg/serial/test_sunlinsol.c
/usr/examples/sunlinsol/pcg/serial/test_sunlinsol.h
/usr/examples/sunlinsol/pcg/serial/test_sunlinsol_pcg_serial.c
/usr/examples/sunlinsol/spbcgs/serial/CMakeLists.txt
/usr/examples/sunlinsol/spbcgs/serial/Makefile
/usr/examples/sunlinsol/spbcgs/serial/sundials_linearsolver.c
/usr/examples/sunlinsol/spbcgs/serial/sundials_nvector.c
/usr/examples/sunlinsol/spbcgs/serial/test_sunlinsol.c
/usr/examples/sunlinsol/spbcgs/serial/test_sunlinsol.h
/usr/examples/sunlinsol/spbcgs/serial/test_sunlinsol_spbcgs_serial.c
/usr/examples/sunlinsol/spfgmr/serial/CMakeLists.txt
/usr/examples/sunlinsol/spfgmr/serial/Makefile
/usr/examples/sunlinsol/spfgmr/serial/sundials_linearsolver.c
/usr/examples/sunlinsol/spfgmr/serial/sundials_nvector.c
/usr/examples/sunlinsol/spfgmr/serial/test_sunlinsol.c
/usr/examples/sunlinsol/spfgmr/serial/test_sunlinsol.h
/usr/examples/sunlinsol/spfgmr/serial/test_sunlinsol_spfgmr_serial.c
/usr/examples/sunlinsol/spgmr/serial/CMakeLists.txt
/usr/examples/sunlinsol/spgmr/serial/Makefile
/usr/examples/sunlinsol/spgmr/serial/sundials_linearsolver.c
/usr/examples/sunlinsol/spgmr/serial/sundials_nvector.c
/usr/examples/sunlinsol/spgmr/serial/test_sunlinsol.c
/usr/examples/sunlinsol/spgmr/serial/test_sunlinsol.h
/usr/examples/sunlinsol/spgmr/serial/test_sunlinsol_spgmr_serial.c
/usr/examples/sunlinsol/sptfqmr/serial/CMakeLists.txt
/usr/examples/sunlinsol/sptfqmr/serial/Makefile
/usr/examples/sunlinsol/sptfqmr/serial/sundials_linearsolver.c
/usr/examples/sunlinsol/sptfqmr/serial/sundials_nvector.c
/usr/examples/sunlinsol/sptfqmr/serial/test_sunlinsol.c
/usr/examples/sunlinsol/sptfqmr/serial/test_sunlinsol.h
/usr/examples/sunlinsol/sptfqmr/serial/test_sunlinsol_sptfqmr_serial.c
/usr/examples/sunmatrix/band/CMakeLists.txt
/usr/examples/sunmatrix/band/Makefile
/usr/examples/sunmatrix/band/sundials_matrix.c
/usr/examples/sunmatrix/band/sundials_nvector.c
/usr/examples/sunmatrix/band/test_sunmatrix.c
/usr/examples/sunmatrix/band/test_sunmatrix.h
/usr/examples/sunmatrix/band/test_sunmatrix_band.c
/usr/examples/sunmatrix/dense/CMakeLists.txt
/usr/examples/sunmatrix/dense/Makefile
/usr/examples/sunmatrix/dense/sundials_matrix.c
/usr/examples/sunmatrix/dense/sundials_nvector.c
/usr/examples/sunmatrix/dense/test_sunmatrix.c
/usr/examples/sunmatrix/dense/test_sunmatrix.h
/usr/examples/sunmatrix/dense/test_sunmatrix_dense.c
/usr/examples/sunmatrix/sparse/CMakeLists.txt
/usr/examples/sunmatrix/sparse/Makefile
/usr/examples/sunmatrix/sparse/sundials_matrix.c
/usr/examples/sunmatrix/sparse/sundials_nvector.c
/usr/examples/sunmatrix/sparse/test_sunmatrix.c
/usr/examples/sunmatrix/sparse/test_sunmatrix.h
/usr/examples/sunmatrix/sparse/test_sunmatrix_sparse.c

%files dev
%defattr(-,root,root,-)
/usr/include/arkode/arkode.h
/usr/include/arkode/arkode_bandpre.h
/usr/include/arkode/arkode_bbdpre.h
/usr/include/arkode/arkode_direct.h
/usr/include/arkode/arkode_impl.h
/usr/include/arkode/arkode_spils.h
/usr/include/cvode/cvode.h
/usr/include/cvode/cvode_bandpre.h
/usr/include/cvode/cvode_bbdpre.h
/usr/include/cvode/cvode_diag.h
/usr/include/cvode/cvode_direct.h
/usr/include/cvode/cvode_impl.h
/usr/include/cvode/cvode_spils.h
/usr/include/cvodes/cvodes.h
/usr/include/cvodes/cvodes_bandpre.h
/usr/include/cvodes/cvodes_bbdpre.h
/usr/include/cvodes/cvodes_diag.h
/usr/include/cvodes/cvodes_direct.h
/usr/include/cvodes/cvodes_impl.h
/usr/include/cvodes/cvodes_spils.h
/usr/include/ida/ida.h
/usr/include/ida/ida_bbdpre.h
/usr/include/ida/ida_direct.h
/usr/include/ida/ida_impl.h
/usr/include/ida/ida_spils.h
/usr/include/idas/idas.h
/usr/include/idas/idas_bbdpre.h
/usr/include/idas/idas_direct.h
/usr/include/idas/idas_impl.h
/usr/include/idas/idas_spils.h
/usr/include/kinsol/kinsol.h
/usr/include/kinsol/kinsol_bbdpre.h
/usr/include/kinsol/kinsol_direct.h
/usr/include/kinsol/kinsol_impl.h
/usr/include/kinsol/kinsol_spils.h
/usr/include/nvector/nvector_serial.h
/usr/include/sundials/LICENSE
/usr/include/sundials/sundials_band.h
/usr/include/sundials/sundials_config.h
/usr/include/sundials/sundials_dense.h
/usr/include/sundials/sundials_direct.h
/usr/include/sundials/sundials_fconfig.h
/usr/include/sundials/sundials_fnvector.h
/usr/include/sundials/sundials_iterative.h
/usr/include/sundials/sundials_linearsolver.h
/usr/include/sundials/sundials_math.h
/usr/include/sundials/sundials_matrix.h
/usr/include/sundials/sundials_mpi.h
/usr/include/sundials/sundials_mpi_types.h
/usr/include/sundials/sundials_nvector.h
/usr/include/sundials/sundials_pcg.h
/usr/include/sundials/sundials_sparse.h
/usr/include/sundials/sundials_spbcgs.h
/usr/include/sundials/sundials_spfgmr.h
/usr/include/sundials/sundials_spgmr.h
/usr/include/sundials/sundials_sptfqmr.h
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
/usr/lib64/haswell/avx512_1/libsundials_arkode.so
/usr/lib64/haswell/avx512_1/libsundials_cvode.so
/usr/lib64/haswell/avx512_1/libsundials_cvodes.so
/usr/lib64/haswell/avx512_1/libsundials_ida.so
/usr/lib64/haswell/avx512_1/libsundials_idas.so
/usr/lib64/haswell/avx512_1/libsundials_kinsol.so
/usr/lib64/haswell/avx512_1/libsundials_nvecserial.so
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolband.so
/usr/lib64/haswell/avx512_1/libsundials_sunlinsoldense.so
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspbcgs.so
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspfgmr.so
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspgmr.so
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolsptfqmr.so
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixband.so
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixdense.so
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixsparse.so
/usr/lib64/haswell/libsundials_arkode.so
/usr/lib64/haswell/libsundials_cvode.so
/usr/lib64/haswell/libsundials_cvodes.so
/usr/lib64/haswell/libsundials_ida.so
/usr/lib64/haswell/libsundials_idas.so
/usr/lib64/haswell/libsundials_kinsol.so
/usr/lib64/haswell/libsundials_nvecserial.so
/usr/lib64/haswell/libsundials_sunlinsolband.so
/usr/lib64/haswell/libsundials_sunlinsoldense.so
/usr/lib64/haswell/libsundials_sunlinsolpcg.so
/usr/lib64/haswell/libsundials_sunlinsolspbcgs.so
/usr/lib64/haswell/libsundials_sunlinsolspfgmr.so
/usr/lib64/haswell/libsundials_sunlinsolspgmr.so
/usr/lib64/haswell/libsundials_sunlinsolsptfqmr.so
/usr/lib64/haswell/libsundials_sunmatrixband.so
/usr/lib64/haswell/libsundials_sunmatrixdense.so
/usr/lib64/haswell/libsundials_sunmatrixsparse.so
/usr/lib64/libsundials_arkode.so
/usr/lib64/libsundials_cvode.so
/usr/lib64/libsundials_cvodes.so
/usr/lib64/libsundials_ida.so
/usr/lib64/libsundials_idas.so
/usr/lib64/libsundials_kinsol.so
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libsundials_arkode.so.2
/usr/lib64/haswell/avx512_1/libsundials_arkode.so.2.2.1
/usr/lib64/haswell/avx512_1/libsundials_cvode.so.3
/usr/lib64/haswell/avx512_1/libsundials_cvode.so.3.2.1
/usr/lib64/haswell/avx512_1/libsundials_cvodes.so.3
/usr/lib64/haswell/avx512_1/libsundials_cvodes.so.3.2.1
/usr/lib64/haswell/avx512_1/libsundials_ida.so.3
/usr/lib64/haswell/avx512_1/libsundials_ida.so.3.2.1
/usr/lib64/haswell/avx512_1/libsundials_idas.so.2
/usr/lib64/haswell/avx512_1/libsundials_idas.so.2.2.1
/usr/lib64/haswell/avx512_1/libsundials_kinsol.so.3
/usr/lib64/haswell/avx512_1/libsundials_kinsol.so.3.2.1
/usr/lib64/haswell/avx512_1/libsundials_nvecserial.so.3
/usr/lib64/haswell/avx512_1/libsundials_nvecserial.so.3.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolband.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolband.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsoldense.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsoldense.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspbcgs.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspbcgs.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspfgmr.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspfgmr.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspgmr.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolspgmr.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolsptfqmr.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunlinsolsptfqmr.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixband.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixband.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixdense.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixdense.so.1.2.1
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixsparse.so.1
/usr/lib64/haswell/avx512_1/libsundials_sunmatrixsparse.so.1.2.1
/usr/lib64/haswell/libsundials_arkode.so.2
/usr/lib64/haswell/libsundials_arkode.so.2.2.1
/usr/lib64/haswell/libsundials_cvode.so.3
/usr/lib64/haswell/libsundials_cvode.so.3.2.1
/usr/lib64/haswell/libsundials_cvodes.so.3
/usr/lib64/haswell/libsundials_cvodes.so.3.2.1
/usr/lib64/haswell/libsundials_ida.so.3
/usr/lib64/haswell/libsundials_ida.so.3.2.1
/usr/lib64/haswell/libsundials_idas.so.2
/usr/lib64/haswell/libsundials_idas.so.2.2.1
/usr/lib64/haswell/libsundials_kinsol.so.3
/usr/lib64/haswell/libsundials_kinsol.so.3.2.1
/usr/lib64/haswell/libsundials_nvecserial.so.3
/usr/lib64/haswell/libsundials_nvecserial.so.3.2.1
/usr/lib64/haswell/libsundials_sunlinsolband.so.1
/usr/lib64/haswell/libsundials_sunlinsolband.so.1.2.1
/usr/lib64/haswell/libsundials_sunlinsoldense.so.1
/usr/lib64/haswell/libsundials_sunlinsoldense.so.1.2.1
/usr/lib64/haswell/libsundials_sunlinsolpcg.so.1
/usr/lib64/haswell/libsundials_sunlinsolpcg.so.1.2.1
/usr/lib64/haswell/libsundials_sunlinsolspbcgs.so.1
/usr/lib64/haswell/libsundials_sunlinsolspbcgs.so.1.2.1
/usr/lib64/haswell/libsundials_sunlinsolspfgmr.so.1
/usr/lib64/haswell/libsundials_sunlinsolspfgmr.so.1.2.1
/usr/lib64/haswell/libsundials_sunlinsolspgmr.so.1
/usr/lib64/haswell/libsundials_sunlinsolspgmr.so.1.2.1
/usr/lib64/haswell/libsundials_sunlinsolsptfqmr.so.1
/usr/lib64/haswell/libsundials_sunlinsolsptfqmr.so.1.2.1
/usr/lib64/haswell/libsundials_sunmatrixband.so.1
/usr/lib64/haswell/libsundials_sunmatrixband.so.1.2.1
/usr/lib64/haswell/libsundials_sunmatrixdense.so.1
/usr/lib64/haswell/libsundials_sunmatrixdense.so.1.2.1
/usr/lib64/haswell/libsundials_sunmatrixsparse.so.1
/usr/lib64/haswell/libsundials_sunmatrixsparse.so.1.2.1
/usr/lib64/libsundials_arkode.so.2
/usr/lib64/libsundials_arkode.so.2.2.1
/usr/lib64/libsundials_cvode.so.3
/usr/lib64/libsundials_cvode.so.3.2.1
/usr/lib64/libsundials_cvodes.so.3
/usr/lib64/libsundials_cvodes.so.3.2.1
/usr/lib64/libsundials_ida.so.3
/usr/lib64/libsundials_ida.so.3.2.1
/usr/lib64/libsundials_idas.so.2
/usr/lib64/libsundials_idas.so.2.2.1
/usr/lib64/libsundials_kinsol.so.3
/usr/lib64/libsundials_kinsol.so.3.2.1
/usr/lib64/libsundials_nvecserial.so.3
/usr/lib64/libsundials_nvecserial.so.3.2.1
/usr/lib64/libsundials_sunlinsolband.so.1
/usr/lib64/libsundials_sunlinsolband.so.1.2.1
/usr/lib64/libsundials_sunlinsoldense.so.1
/usr/lib64/libsundials_sunlinsoldense.so.1.2.1
/usr/lib64/libsundials_sunlinsolpcg.so.1
/usr/lib64/libsundials_sunlinsolpcg.so.1.2.1
/usr/lib64/libsundials_sunlinsolspbcgs.so.1
/usr/lib64/libsundials_sunlinsolspbcgs.so.1.2.1
/usr/lib64/libsundials_sunlinsolspfgmr.so.1
/usr/lib64/libsundials_sunlinsolspfgmr.so.1.2.1
/usr/lib64/libsundials_sunlinsolspgmr.so.1
/usr/lib64/libsundials_sunlinsolspgmr.so.1.2.1
/usr/lib64/libsundials_sunlinsolsptfqmr.so.1
/usr/lib64/libsundials_sunlinsolsptfqmr.so.1.2.1
/usr/lib64/libsundials_sunmatrixband.so.1
/usr/lib64/libsundials_sunmatrixband.so.1.2.1
/usr/lib64/libsundials_sunmatrixdense.so.1
/usr/lib64/libsundials_sunmatrixdense.so.1.2.1
/usr/lib64/libsundials_sunmatrixsparse.so.1
/usr/lib64/libsundials_sunmatrixsparse.so.1.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sundials/LICENSE
/usr/share/package-licenses/sundials/src_arkode_LICENSE
/usr/share/package-licenses/sundials/src_cvode_LICENSE
/usr/share/package-licenses/sundials/src_cvodes_LICENSE
/usr/share/package-licenses/sundials/src_ida_LICENSE
/usr/share/package-licenses/sundials/src_idas_LICENSE
/usr/share/package-licenses/sundials/src_kinsol_LICENSE
