Name:		mmv
Version:	1.01b
Release:	%mkrel 9
Summary:	Move/copy/append/link multiple files

Group:		File tools
License:	GPL
URL:		http://packages.qa.debian.org/m/mmv.html
Source0:	http://ftp.debian.org/debian/pool/main/m/mmv/mmv_1.01b.orig.tar.gz
Source1:	copyright
Source2:	changelog
Patch0:		mmv-1.01b-debian.patch
Patch1:		mmv-1.01b-makefile.patch
Patch2:		mmv-1.01b-debian-14.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is mmv, a program to move/copy/append/link multiple files
according to a set of wildcard patterns. This multiple action is
performed safely, i.e. without any unexpected deletion of files due to
collisions of target names with existing filenames or with other
target names. Furthermore, before doing anything, mmv attempts to
detect any errors that would result from the entire set of actions
specified and gives the user the choice of either aborting before
beginning, or proceeding by avoiding the offending parts.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp -p %{SOURCE1} . 
cp -p %{SOURCE2} .

%build
%make CONF="%{optflags} -fpie" LDCONF="-pie"

%install
rm -rf %{buildroot}
%makeinstall_std
ln -s mmv %{buildroot}%{_bindir}/mcp
ln -s mmv %{buildroot}%{_bindir}/mad
ln -s mmv %{buildroot}%{_bindir}/mln
ln -s mmv.1%{_extension} %{buildroot}%{_mandir}/man1/mcp.1%{_extension}
ln -s mmv.1%{_extension} %{buildroot}%{_mandir}/man1/mad.1%{_extension}
ln -s mmv.1%{_extension} %{buildroot}%{_mandir}/man1/mln.1%{_extension}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc copyright changelog
%defattr(-,root,root,-)
%doc ANNOUNCE ARTICLE READ.ME
%{_bindir}/mmv
%{_bindir}/mcp
%{_bindir}/mad
%{_bindir}/mln
%{_mandir}/man1/*


