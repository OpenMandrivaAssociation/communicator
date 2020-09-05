Name:		contacts
Version:	1.1.1
Release:	1
Source0:	https://invent.kde.org/maui/communicator/-/archive/v%{version}/communicator-v%{version}.tar.bz2
Group:		Applications/Productivity
Summary:	Contact management for Plasma Mobile
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
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(PhoneNumber)
BuildRequires:	%{_lib}phonenumber-devel

%description
Contact management for Plasma Mobile

%prep
%autosetup -p1 -n communicator-v%{version}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/contacts
%{_datadir}/applications/org.kde.contacts.desktop
%{_datadir}/icons/hicolor/scalable/apps/contacts.svg
%{_datadir}/maui-accounts
