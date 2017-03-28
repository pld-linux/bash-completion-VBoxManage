#
Summary:	bash-completion for VBoxManage command
Name:		bash-completion-VBoxManage
Version:	5.0.32
Release:	1
License:	BSD
Group:		Applications/Shells
Source0:	https://github.com/gryf/vboxmanage-bash-completion/raw/%{version}/VBoxManage
# Source0-md5:	be1693611ab91abc62b342ce5f7c6097
URL:		https://github.com/gryf/vboxmanage-bash-completion/
Requires:	bash-completion
Requires:	VirtualBox
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/bash_completion.d

%description
bash-completion for VBoxManage command.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/VBoxManage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/*
