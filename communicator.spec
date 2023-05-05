#define snapshot 20220107

Name:		communicator
Version:	2.2.2
Release:	%{?snapshot:0.%{snapshot}.}1
Source0:	https://invent.kde.org/maui/communicator/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/communicator-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/communicator-%{snapshot}.tar.bz2}
Group:		Applications/Productivity
Summary:	Communicator management for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(MauiKit)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5People)
BuildRequires:  cmake(KF5Service)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(PhoneNumber)
BuildRequires:	cmake(MauiKitFileBrowsing)
BuildRequires:	%{_lib}phonenumber-devel

Provides:   contacts = %{version}-%{release}

Obsoletes:  contacts <= 1.1.2-2

%description
Communicator management for Plasma Mobile

%prep
%autosetup -p1 -n communicator-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
#sed -i -e 's,Icon=maui-communicator,Icon=communicator,g' %{buildroot}%{_datadir}/applications/org.maui.communicator.desktop

%find_lang communicator

%files -f communicator.lang
%{_bindir}/communicator
%{_datadir}/applications/org.kde.communicator.desktop
%{_datadir}/icons/hicolor/scalable/apps/communicator.svg
%{_datadir}/maui-accounts
%{_datadir}/metainfo/org.kde.communicator.appdata.xml
