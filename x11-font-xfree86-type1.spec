Name: x11-font-xfree86-type1
Version: 1.0.4
Release: 13
Summary: Xorg X11 font xfree86-type1
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-xfree86-type1-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.2
Conflicts: xorg-x11 <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font xfree86-type1

%prep
%setup -q -n font-xfree86-type1-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/Type1

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/fonts/Type1/fonts.{dir,scale}

%post
mkfontscale %{_datadir}/fonts/Type1
mkfontdir %{_datadir}/fonts/Type1

%postun
mkfontscale %{_datadir}/fonts/Type1
mkfontdir %{_datadir}/fonts/Type1

%files
%doc COPYING
%{_datadir}/fonts/Type1/cursor.pfa


