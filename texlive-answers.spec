Name:		texlive-answers
Version:	35032
Release:	2
Summary:	Setting questions (or exercises) and answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/answers
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/answers
%doc %{_texmfdistdir}/doc/latex/answers
#- source
%doc %{_texmfdistdir}/source/latex/answers

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
