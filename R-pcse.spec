#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pcse
Version  : 1.9.1.1
Release  : 7
URL      : https://cran.r-project.org/src/contrib/pcse_1.9.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pcse_1.9.1.1.tar.gz
Summary  : Panel-Corrected Standard Error Estimation in R
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
panel-corrected standard errors. Data may contain balanced or
        unbalanced panels.

%prep
%setup -q -c -n pcse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552933804

%install
export SOURCE_DATE_EPOCH=1552933804
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pcse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pcse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pcse
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  pcse || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pcse/CITATION
/usr/lib64/R/library/pcse/DESCRIPTION
/usr/lib64/R/library/pcse/INDEX
/usr/lib64/R/library/pcse/Meta/Rd.rds
/usr/lib64/R/library/pcse/Meta/data.rds
/usr/lib64/R/library/pcse/Meta/demo.rds
/usr/lib64/R/library/pcse/Meta/features.rds
/usr/lib64/R/library/pcse/Meta/hsearch.rds
/usr/lib64/R/library/pcse/Meta/links.rds
/usr/lib64/R/library/pcse/Meta/nsInfo.rds
/usr/lib64/R/library/pcse/Meta/package.rds
/usr/lib64/R/library/pcse/Meta/vignette.rds
/usr/lib64/R/library/pcse/NAMESPACE
/usr/lib64/R/library/pcse/R/pcse
/usr/lib64/R/library/pcse/R/pcse.rdb
/usr/lib64/R/library/pcse/R/pcse.rdx
/usr/lib64/R/library/pcse/data/agl.tab.gz
/usr/lib64/R/library/pcse/data/aglUn.tab.gz
/usr/lib64/R/library/pcse/demo/pcse.R
/usr/lib64/R/library/pcse/doc/index.html
/usr/lib64/R/library/pcse/doc/pcse.R
/usr/lib64/R/library/pcse/doc/pcse.Rnw
/usr/lib64/R/library/pcse/doc/pcse.bib
/usr/lib64/R/library/pcse/doc/pcse.pdf
/usr/lib64/R/library/pcse/help/AnIndex
/usr/lib64/R/library/pcse/help/aliases.rds
/usr/lib64/R/library/pcse/help/paths.rds
/usr/lib64/R/library/pcse/help/pcse.rdb
/usr/lib64/R/library/pcse/help/pcse.rdx
/usr/lib64/R/library/pcse/html/00Index.html
/usr/lib64/R/library/pcse/html/R.css
