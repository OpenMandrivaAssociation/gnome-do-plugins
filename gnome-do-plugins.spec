Name:			gnome-do-plugins
Version:		0.8.1.1
Release:		%mkrel 1
Summary:		Creating and managing the plugins that put the 'Do' in 'GNOME Do'
License:		GPLv3+
Group:			Graphical desktop/GNOME
URL:			http://do.davebsd.com/
Source0:		http://launchpad.net/do-plugins/0.8/%version/+download/%name-%version.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:		noarch
BuildRequires:		intltool >= 0.35.0
BuildRequires:		gnome-do >= 0.8
BuildRequires:		banshee >= 1.4.2
Buildrequires:		mono-devel
BuildRequires:		mono-flickrnet
BuildRequires:		mono-addins
BuildRequires:		evolution-sharp
BuildRequires:		gnome-sharp2-devel
BuildRequires:		glade-sharp2
BuildRequires:		glib-sharp2
BuildRequires:		gnome-desktop-sharp-devel
BuildRequires:		gnome-keyring-sharp
BuildRequires:		gtk-sharp2
BuildRequires:		ndesk-dbus
BuildRequires:		ndesk-dbus-glib
BuildRequires:		notify-sharp

%description
Creating and managing the plugins that put the 'Do' in 'GNOME Do'.

%prep
%setup -q 

%build
%configure2_5x
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/gnome-do/plugins/*
