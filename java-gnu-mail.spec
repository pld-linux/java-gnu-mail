#
Summary:	GNU JavaMail
Name:		java-gnu-mail
Version:	1.1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/classpathx/mail-%{version}.tar.gz
# Source0-md5:	27bb68ef61dd9a967b375b7798c2524d
URL:		http://www.gnu.org/software/classpathx/javamail/javamail.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	java-gnu-inetlib
Requires:	jre
Provides:	javamail = 1.3
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU JavaMail is a free implementation of the JavaMail API
specification, version 1.3. All the code has been written from scratch
without reference to Sun's code, which allows GNU JavaMail to be used
on a completely free operating system such as GNU/Linux or the Hurd.
The code is optimized to work with free Java implementations, nothing
prevents it from being used with any compliant JVM.

%package doc
Summary:	API documentation for GNU JavaMail
Summary(pl):	Dokumentacja API GNU JavaMail
Group:		Documentation

%description doc
API documentation for GNU JavaMail.

%description doc -l pl
Dokumentacja API GNU JavaMail.

%prep
%setup -q -n mail-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
# Sun java requires . in CLASSPATH for configure test
export CLASSPATH=.
export JAVAC=%{_bindir}/javac
export JAVA=%{_bindir}/java
%configure

%{__make}
%{__make} javadoc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* source/javax/mail/*.html
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*
