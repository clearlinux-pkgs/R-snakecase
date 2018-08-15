#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-snakecase
Version  : 0.9.2
Release  : 2
URL      : https://cran.r-project.org/src/contrib/snakecase_0.9.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/snakecase_0.9.2.tar.gz
Summary  : Convert Strings into any Case
Group    : Development/Tools
License  : GPL-3.0
Requires: R-markdown
Requires: R-tibble
BuildRequires : R-markdown
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n snakecase

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534352094

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1534352094
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snakecase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snakecase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snakecase
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library snakecase|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/snakecase/DESCRIPTION
/usr/lib64/R/library/snakecase/INDEX
/usr/lib64/R/library/snakecase/Meta/Rd.rds
/usr/lib64/R/library/snakecase/Meta/features.rds
/usr/lib64/R/library/snakecase/Meta/hsearch.rds
/usr/lib64/R/library/snakecase/Meta/links.rds
/usr/lib64/R/library/snakecase/Meta/nsInfo.rds
/usr/lib64/R/library/snakecase/Meta/package.rds
/usr/lib64/R/library/snakecase/Meta/vignette.rds
/usr/lib64/R/library/snakecase/NAMESPACE
/usr/lib64/R/library/snakecase/NEWS.md
/usr/lib64/R/library/snakecase/R/snakecase
/usr/lib64/R/library/snakecase/R/snakecase.rdb
/usr/lib64/R/library/snakecase/R/snakecase.rdx
/usr/lib64/R/library/snakecase/doc/caseconverters.R
/usr/lib64/R/library/snakecase/doc/caseconverters.Rmd
/usr/lib64/R/library/snakecase/doc/caseconverters.html
/usr/lib64/R/library/snakecase/doc/index.html
/usr/lib64/R/library/snakecase/help/AnIndex
/usr/lib64/R/library/snakecase/help/aliases.rds
/usr/lib64/R/library/snakecase/help/figures/snakecase05.png
/usr/lib64/R/library/snakecase/help/paths.rds
/usr/lib64/R/library/snakecase/help/snakecase.rdb
/usr/lib64/R/library/snakecase/help/snakecase.rdx
/usr/lib64/R/library/snakecase/html/00Index.html
/usr/lib64/R/library/snakecase/html/R.css
