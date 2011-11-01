Name:		texlive-answers
Version:	2.13
Release:	1
Summary:	Setting questions (or exercises) and answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/answers
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows a lot of flexibility in constructing
question and answer sheets.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
