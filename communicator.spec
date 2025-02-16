#define snapshot 20220107

Name:		communicator
Version:	4.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Url:      https://invent.kde.org/maui/communicator/
Source0:	https://invent.kde.org/maui/communicator/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/maui-communicator-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/maui-communicator-%{snapshot}.tar.bz2}
#Patch0:   https://invent.kde.org/maui/maui-communicator/-/merge_requests/4.patch
Group:		Applications/Productivity
Summary:	Communicator management for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(MauiKit4)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6People)
BuildRequires:  cmake(KF6Service)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(PhoneNumber)
BuildRequires:	cmake(MauiKitFileBrowsing4)
BuildRequires:	%{_lib}phonenumber-devel

Provides:   contacts = %{version}-%{release}

Obsoletes:  contacts <= 1.1.2-2

%description
Communicator management for Plasma Mobile

%prep
%autosetup -p1 -n maui-communicator-%{?snapshot:master}%{!?snapshot:v%{version}}
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
