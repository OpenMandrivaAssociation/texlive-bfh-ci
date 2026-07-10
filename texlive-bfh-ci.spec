%global tl_name bfh-ci
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2.6
Release:	%{tl_revision}.1
Summary:	Corporate Design for Bern University of Applied Sciences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bfh-ci
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bfh-ci.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bfh-ci.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(adjustbox)
Requires:	texlive(amsfonts)
Requires:	texlive(amsmath)
Requires:	texlive(anyfontsize)
Requires:	texlive(beamer)
Requires:	texlive(fontawesome)
Requires:	texlive(fontspec)
Requires:	texlive(geometry)
Requires:	texlive(graphics)
Requires:	texlive(handoutwithnotes)
Requires:	texlive(hyperref)
Requires:	texlive(iftex)
Requires:	texlive(koma-script)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Requires:	texlive(listings)
Requires:	texlive(nunito)
Requires:	texlive(pgf)
Requires:	texlive(qrcode)
Requires:	texlive(sourceserif)
Requires:	texlive(tcolorbox)
Requires:	texlive(tools)
Requires:	texlive(translations)
Requires:	texlive(url)
Requires:	texlive(xcolor)
Requires:	texlive(zref)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides possibilities to use the Corporate Design of Bern
University of Applied Sciences (BFH) with LaTeX. To this end it contains
classes as well as some helper packages and config files together with
some demo files.

