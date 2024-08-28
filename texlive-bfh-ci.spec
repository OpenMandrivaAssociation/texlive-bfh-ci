Name:		texlive-bfh-ci
Version:	70623
Release:	1
Summary:	Corporate Design for Bern University of Applied Sciences
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bfh-ci
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bfh-ci.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bfh-ci.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides possibilities to use the Corporate Design
of Bern University of Applied Sciences (BFH) with LaTeX. To
this end it contains classes as well as some helper packages
and config files together with some demo files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bfh-ci
%doc %{_texmfdistdir}/doc/latex/bfh-ci

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
