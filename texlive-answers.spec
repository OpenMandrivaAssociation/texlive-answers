%global tl_name answers
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.16
Release:	%{tl_revision}.1
Summary:	Setting questions (or exercises) and answers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/answers
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/answers.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows a lot of flexibility in constructing question and
answer sheets.

