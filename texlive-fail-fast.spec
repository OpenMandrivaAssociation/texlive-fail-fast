%global tl_name fail-fast
%global tl_revision 67543

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.2
Release:	%{tl_revision}.1
Summary:	Turn warnings into errors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fail-fast
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fail-fast.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fail-fast.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fail-fast.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package helps you make the build more fragile by turning
warnings into errors. This may be a good practice if you care about the
quality of your documents.

