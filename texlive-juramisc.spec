Name:		texlive-juramisc
Version:	15878
Release:	1
Summary:	Typesetting German juridical documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/juramisc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juramisc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juramisc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of classes for typesetting court sentences, legal
opinions, and dissertations for German lawyers. The package is
still under development.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/juramisc/jbgoe.clo
%{_texmfdistdir}/tex/latex/juramisc/jbstgallen.clo
%{_texmfdistdir}/tex/latex/juramisc/jbtrier.clo
%{_texmfdistdir}/tex/latex/juramisc/jurabase.sty
%{_texmfdistdir}/tex/latex/juramisc/jurabook.cls
%{_texmfdistdir}/tex/latex/juramisc/juraovw.cls
%{_texmfdistdir}/tex/latex/juramisc/juraurtl.cls
%doc %{_texmfdistdir}/doc/latex/juramisc/README
%doc %{_texmfdistdir}/doc/latex/juramisc/doc/jbook/jbook.dtx
%doc %{_texmfdistdir}/doc/latex/juramisc/doc/jbook/jbook.ins
%doc %{_texmfdistdir}/doc/latex/juramisc/doc/jmgerdoc.pdf
%doc %{_texmfdistdir}/doc/latex/juramisc/doc/jmgerdoc.tex
%doc %{_texmfdistdir}/doc/latex/juramisc/doc/jmgerdoc_scr.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
