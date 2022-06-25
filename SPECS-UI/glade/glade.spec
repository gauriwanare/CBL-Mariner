%define _unpackaged_files_terminate_build 0
Name:           glade
Version:        3.22.1
Release:        2%{?dist}
Summary:        User Interface Builder for GTK+ 3
License:        GPL-2.0-or-later
Group:          Development/Tools/GUI Builders
URL:            https://glade.gnome.org/
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:         http://download.gnome.org/sources/glade/3.22/%{name}-%{version}.tar.xz
%define sha1 glade=395728b7f0b4c3a0acadd7e12c39db6296761b22
BuildRequires:  gobject-introspection-devel libxml2
BuildRequires:  gtk3 gtk3-immodules gtk3-immodule-xim gtk-doc gtk3-devel glib fontconfig-devel
BuildRequires:  intltool  libXinerama libpng-devel
BuildRequires:  pkg-config pango-devel cairo-devel itstool gdk-pixbuf2-devel atk-devel
BuildRequires:  python3-devel freetype-devel libXdamage-devel at-spi2-atk-devel at-spi2-core-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:	gtk3 gdk-pixbuf2 atk at-spi2-atk at-spi2-core
Recommends:     %{name}-lang

%description
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

%package -n libgladeui-2-6
Summary:        Core library of the GLADE User Interface Builder
Group:          System/Libraries
Recommends:     %{name}-lang

%description -n libgladeui-2-6
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

%package -n typelib-1_0-Gladeui-2_0
Summary:        Introspection bindins for libgladeui
Group:          System/Libraries

%description -n typelib-1_0-Gladeui-2_0
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

This package provides the GObject Introspection bindings for the
libgladeui library.

%package -n libgladeui-2-devel
Summary:        Development files for libgladeui
Group:          Development/Libraries/C and C++
Requires:       libgladeui-2-6 = %{version}
Requires:       typelib-1_0-Gladeui-2_0 = %{version}
# The gtk-doc documentation is not parallel installable (bnc#646997)
Conflicts:      libgladeui-1-devel

%description -n libgladeui-2-devel
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

This subpackage contains the header files for developing
applications that want to make use of libgladeui.

%lang_package

%prep
%setup -q

%build
%configure \
    --disable-static \
    --disable-gtk-doc \
    --disable-man-pages
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%post -n libgladeui-2-6 -p /sbin/ldconfig
%postun -n libgladeui-2-6 -p /sbin/ldconfig

%files
%license COPYING COPYING.GPL COPYING.LGPL
%doc NEWS README
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/glade
%{_bindir}/glade-previewer
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/glade.appdata.xml
%{_datadir}/applications/glade.desktop
%{_datadir}/glade/
%{_datadir}/icons/hicolor/*/apps/*.*
%{_libdir}/glade/modules/libgladegtk.so
#%{_libdir}/glade/modules/libgladepython.so
#%{_libdir}/glade/modules/libgladewebkit2gtk.so
%{_datadir}/locale/*

%files -n libgladeui-2-6
%{_libdir}/libgladeui*.so.*
# These directories are needed by third-party catalogs, and are explicitly
# referenced in the pkg-config file, so it makes sense to own them here
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%dir %{_datadir}/glade/pixmaps
%dir %{_datadir}/glade/pixmaps/hicolor
%dir %{_datadir}/glade/pixmaps/hicolor/*
%dir %{_datadir}/glade/pixmaps/hicolor/*/actions
%dir %{_libdir}/glade
%dir %{_libdir}/glade/modules

%files -n typelib-1_0-Gladeui-2_0
%{_libdir}/girepository-1.0/Gladeui-2.0.typelib

%files -n libgladeui-2-devel
%doc AUTHORS ChangeLog TODO
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/gladeui-2
%{_includedir}/libgladeui-2.0/
%{_libdir}/pkgconfig/gladeui-2.0.pc
%{_libdir}/libgladeui*.so
%{_datadir}/gir-1.0/*.gir

# %files lang -f %{name}.lang

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 3.22.1-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 3.22.1-1
-	Mariner initial version

