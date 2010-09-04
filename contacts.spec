%define	name	contacts
%define	version	0.12
%define	release	%mkrel 1

Summary:	Small, lightweight addressbook
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://ftp.gnome.org/pub/GNOME/sources/contacts/%{version}/%{name}-%{version}.tar.bz2
Patch0:		contacts-0.11-fix-str-fmt.patch
Patch1:		contacts-0.12-fix-build.patch
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://pimlico-project.org/contacts.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libedataserver-devel
BuildRequires:	libgtk+2-devel intltool gnome-vfs2-devel
BuildRequires:	desktop-file-utils

%description
Contacts is a small, lightweight addressbook that uses libebook, part of EDS.
This is the same library that GNOME Evolution uses, so all contact data that
exists in your Evolution addressbook is accessible via Contacts.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --remove-category="Application" \
  --remove-category="Office" \
  --remove-category="Project Management" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
$RPM_BUILD_ROOT%{_datadir}/applications/*

%define schemas %name

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%update_menus
%post_install_gconf_schemas %{schemas}
%endif

%preun
%preun_uninstall_gconf_schemas %{schemas}

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%_sysconfdir/gconf/schemas/
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_mandir/man1/*
%_iconsdir/*/*/apps/*.png
%_iconsdir/*/*/apps/*.svg

%lang(all) %{_datadir}/locale/*/LC_MESSAGES/*


