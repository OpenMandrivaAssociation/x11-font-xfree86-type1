Name: x11-font-xfree86-type1
Version: 1.0.4
Release: 7
Summary: Xorg X11 font xfree86-type1
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-xfree86-type1-%{version}.tar.bz2
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
./configure --prefix=/usr \
            --x-includes=%_includedir \
            --x-libraries=%_libdir \
            --with-fontdir=%_datadir/fonts/Type1

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_datadir}/fonts/Type1/fonts.{dir,scale}

%post
mkfontscale %{_datadir}/fonts/Type1
mkfontdir %{_datadir}/fonts/Type1

%postun
mkfontscale %{_datadir}/fonts/Type1
mkfontdir %{_datadir}/fonts/Type1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_datadir}/fonts/Type1/cursor.pfa


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.4-3mdv2011.0
+ Revision: 675498
+ rebuild (emptylog)

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2
+ Revision: 671225
- mass rebuild

* Fri Dec 10 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 620435
- workaround new rpm breakage
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 583219
- new release

* Wed Jan 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 490707
- Fix license
- New version: 1.0.2

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-3mdv2009.1
+ Revision: 351260
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2009.0
+ Revision: 266053
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-1mdv2009.0
+ Revision: 193500
- Update to version 1.0.1.

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2008.1
+ Revision: 179643
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdv2008.0
+ Revision: 75832
- rebuild


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 18:01:24 (48064)
- Fonts packages now are noarch. Moved for new place /usr/share/fonts. Approved by Boiko

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 21:57:49 (31395)
- fix license

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

