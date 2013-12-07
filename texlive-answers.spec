# revision 20070
# category Package
# catalog-ctan /macros/latex/contrib/answers
# catalog-date 2010-10-12 00:02:51 +0200
# catalog-license lppl
# catalog-version 2.13
Name:		texlive-answers
Version:	2.13
Release:	6
Summary:	Setting questions (or exercises) and answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/answers
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows a lot of flexibility in constructing
question and answer sheets.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/answers/answers.sty
%doc %{_texmfdistdir}/doc/latex/answers/ansexam1.tex
%doc %{_texmfdistdir}/doc/latex/answers/ansexam2.tex
%doc %{_texmfdistdir}/doc/latex/answers/ansexam3.tex
%doc %{_texmfdistdir}/doc/latex/answers/answers.pdf
#- source
%doc %{_texmfdistdir}/source/latex/answers/answers.dtx
%doc %{_texmfdistdir}/source/latex/answers/answers.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.13-2
+ Revision: 749251
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.13-1
+ Revision: 717832
- texlive-answers
- texlive-answers
- texlive-answers
- texlive-answers
- texlive-answers

