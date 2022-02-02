%define		plugin	nnn
Summary:	Vim plugin: File manager for powered by n³
Name:		vim-plugin-%{plugin}
Version:	3.6
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/mcchrish/nnn.vim/archive/v%{version}/nnn.vim-%{version}.tar.gz
# Source0-md5:	d517c282ea2158c5c65ee3c138649e7c
URL:		https://github.com/mcchrish/nnn.vim
Requires:	nnn >= 4.3
Requires:	vim-rt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
File manager for vim/neovim powered by n³.

%package doc
Summary:	Documentation for nnn Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt

%description doc
Documentation for nnn Vim plugin.

%prep
%setup -qn nnn.vim-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/
cp -pr autoload doc ftplugin plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%{_vimdatadir}/autoload/nnn.vim
%{_vimdatadir}/ftplugin/nnn.vim
%{_vimdatadir}/plugin/nnn.vim

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/nnn.txt
