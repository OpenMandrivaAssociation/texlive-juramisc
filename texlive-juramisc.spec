# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/juramisc
# catalog-date 2007-11-23 19:34:36 +0100
# catalog-license lppl
# catalog-version 0.91
Name:		texlive-juramisc
Version:	0.91
Release:	8
Summary:	Typesetting German juridical documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/juramisc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juramisc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juramisc.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.91-2
+ Revision: 752939
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.91-1
+ Revision: 718763
- texlive-juramisc
- texlive-juramisc
- texlive-juramisc
- texlive-juramisc

