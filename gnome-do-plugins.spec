Name:			gnome-do-plugins
Version:		0.8.2.1
Release:		%mkrel 2
Summary:		Creating and managing the plugins that put the 'Do' in 'GNOME Do'
License:		GPLv3+
Group:			Graphical desktop/GNOME
URL:			http://do.davebsd.com/
Source0:		http://launchpad.net/do-plugins/0.8/%version/+download/%name-%version.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:		intltool >= 0.35.0
BuildRequires:		gnome-do >= 0.8
BuildRequires:		banshee-devel >= 1.4.2
Buildrequires:		mono-devel
BuildRequires:		mono-flickrnet
BuildRequires:		mono-addins
BuildRequires:		evolution-sharp-devel
BuildRequires:		gnome-sharp2-devel
BuildRequires:		glade-sharp2
BuildRequires:		glib-sharp2
BuildRequires:		gnome-desktop-sharp-devel
BuildRequires:		gnome-keyring-sharp
BuildRequires:		gtk-sharp2
BuildRequires:		ndesk-dbus
BuildRequires:		ndesk-dbus-glib
BuildRequires:		notify-sharp-devel
BuildRequires:		libgoogle-data-mono-devel

%description
Creating and managing the plugins that put the 'Do' in 'GNOME Do'.

%prep
%setup -q 

%build
%configure2_5x --disable-evolution \
	--disable-gcal
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,-)
%{_libdir}/gnome-do/plugins/*
