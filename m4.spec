# >> macros
# << macros

Name:       m4
Summary:    The GNU macro processor
Version:    1.4.16
Release:    1
Group:      Applications/Text
License:    GPLv3+
URL:        http://www.gnu.org/software/m4/
Source0:    ftp://ftp.gnu.org/gnu/m4/m4-%{version}.tar.bz2
Patch0:     m4-aarch64.patch
Patch1:     m4-gets-aarch64.patch
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info


%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

Install m4 if you need a macro processor.




%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post
%install_info --info-dir=%_infodir %{_infodir}/m4.info.gz

%postun
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/m4.info.gz
fi


%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_bindir}/m4
%doc %{_infodir}/m4.info-1.gz
%doc %{_infodir}/m4.info-2.gz
%doc %{_infodir}/m4.info.gz
%doc %{_mandir}/man1/m4.1*
# << files


