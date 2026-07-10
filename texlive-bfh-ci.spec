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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bfh-ci
%dir %{_datadir}/texmf-dist/tex/latex/bfh-ci
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHBeamer-Sidebar.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHBeamer-Sidebar.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHBeamer.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHBeamer.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHFactsheet.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHFactsheet.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHLetter.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHLetter.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHProjektProposal.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHProjektProposal.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHPub.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHPub.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHSciPoster.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHSciPoster.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHThesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEMO-BFHThesis.tex
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/DEPENDS.txt
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bfh-ci/bfh-hkb-doc.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/beamercolorthemeBFH.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/beamerfontthemeBFH.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/beamerinnerthemeBFH.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/beamerouterthemeBFH-sidebar.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/beamerouterthemeBFH.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/beamerthemeBFH.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-a0paper.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-a1paper.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-a2paper.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-a3paper.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-a4paper.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-a5paper.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-a6paper.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-beamerarticle.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-factsheet.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-layout-boxes.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-layout-listings.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-layout-rules.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-layout-tabular.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-layout-terminal.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfh-projectproposal.cfg
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhbeamer.cls
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhcolors.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhfonts.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhlayout.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhletter.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhlettersize9.5pt.clo
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhmodule.sty
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhpub.cls
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhsciposter.cls
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhthesis.cls
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhtranslations-english.trsl
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhtranslations-french.trsl
%{_datadir}/texmf-dist/tex/latex/bfh-ci/bfhtranslations-german.trsl
