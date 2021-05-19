#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-snakecase
Version  : 0.11.0
Release  : 27
URL      : https://cran.r-project.org/src/contrib/snakecase_0.11.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/snakecase_0.11.0.tar.gz
Summary  : Convert Strings into any Case
Group    : Development/Tools
License  : GPL-3.0
Requires: R-stringi
Requires: R-stringr
BuildRequires : R-stringi
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n snakecase
cd %{_builddir}/snakecase

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589587378

%install
export SOURCE_DATE_EPOCH=1589587378
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc snakecase || :


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
/usr/lib64/R/library/snakecase/doc/introducing-the-snakecase-package.R
/usr/lib64/R/library/snakecase/doc/introducing-the-snakecase-package.Rmd
/usr/lib64/R/library/snakecase/doc/introducing-the-snakecase-package.html
/usr/lib64/R/library/snakecase/help/AnIndex
/usr/lib64/R/library/snakecase/help/aliases.rds
/usr/lib64/R/library/snakecase/help/figures/snakecase05.png
/usr/lib64/R/library/snakecase/help/paths.rds
/usr/lib64/R/library/snakecase/help/snakecase.rdb
/usr/lib64/R/library/snakecase/help/snakecase.rdx
/usr/lib64/R/library/snakecase/html/00Index.html
/usr/lib64/R/library/snakecase/html/R.css
/usr/lib64/R/library/snakecase/tests/testthat.R
/usr/lib64/R/library/snakecase/tests/testthat/helper-examples.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_any_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_lower_camel_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_lower_upper_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_mixed_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_parsed_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_parsed_case_internal.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_random_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_screaming_snake_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_sentence_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_snake_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_swap_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_title_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_upper_camel_case.R
/usr/lib64/R/library/snakecase/tests/testthat/test-to_upper_lower_case.R
