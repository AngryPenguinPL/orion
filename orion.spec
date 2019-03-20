Name:		orion
Version:	1.6.6
Release:	1
Summary:	Desktop client for Twitch.
Group:		Video/Players
License:	GPLv3+
URL:		https://github.com/alamminsalo/orion
Source0:	https://github.com/alamminsalo/orion/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5QuickControls2)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	desktop-file-utils
BuildRequires:  qmake5
Requires:	hicolor-icon-theme
Requires:	qtquickcontrols5

%description
Desktop client for Twitch based on QML/C++


%prep
%autosetup -p1 -n %{name}-%{version}

%build
mkdir build
cd build
%{qmake_qt5} ../ "CONFIG+=multimedia"
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/orion
%{_datadir}/metainfo/Orion.appdata.xml
%{_datadir}/applications/Orion.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%license COPYING LICENSE.txt
