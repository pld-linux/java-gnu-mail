Summary:	GNU implementation of JavaMail API specification
Summary(pl.UTF-8):	Implementacja GNU specyfikacji JavaMail
Name:		java-gnu-mail
Version:	1.1.2
Release:	1
License:	GPL
Group:		Libraries/Java
Source0:	http://ftp.gnu.org/gnu/classpathx/mail-%{version}.tar.gz
# Source0-md5:	0a94ff4328ceb6a4131be96946976a33
URL:		http://www.gnu.org/software/classpathx/javamail/javamail.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	java-gnu-activation
BuildRequires:	java-gnu-inetlib
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
Provides:	javamail = 1.3
Obsoletes:	javamail
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU JavaMail is a free implementation of the JavaMail API
specification, version 1.3. All the code has been written from scratch
without reference to Sun's code, which allows GNU JavaMail to be used
on a completely free operating system such as GNU/Linux or the Hurd.
The code is optimized to work with free Java implementations, nothing
prevents it from being used with any compliant JVM.

%description -l pl.UTF-8
GNU JavaMail to wolnodostępna implementacja specyfikacji API JavaMail
w wersji 1.3. Cały kod został napisany od zera bez wykorzystania kodu
Suna, co pozwala na używanie GNU JavaMail w całkowicie wolnodostępnych
systemach, takich jak GNU/Linux czy Hurd. Kod został zoptymalizowany
pod kątem wolnodostępnych implementacji Javy, ale nic nie powstrzymuje
przed wykorzystaniem go z dowolnym zgodnym JVM-em.

%package javadoc
Summary:	API documentation for GNU JavaMail
Summary(pl.UTF-8):	Dokumentacja API GNU JavaMail
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	java-gnu-mail-doc

%description javadoc
API documentation for GNU JavaMail.

%description javadoc -l pl.UTF-8
Dokumentacja API GNU JavaMail.

%prep
%setup -q -n mail-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
unset CLASSPATH || :
export JAVAC=%{javac}
export JAVA=%{java}
%configure

%{__make}
%{__make} javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_javadir}/{gnumail.jar,gnumail-%{version}.jar}
mv $RPM_BUILD_ROOT%{_javadir}/{gnumail-providers.jar,gnumail-providers-%{version}.jar}
ln -s gnumail-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/gnumail.jar
ln -s gnumail-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mail.jar
ln -s gnumail-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mailapi.jar

install -d $RPM_BUILD_ROOT%{_javadir}/javamail
for prov in imap smtp pop3 nntp mbox maildir; do
	ln -s ../gnumail-providers-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/javamail/$prov.jar
done

cp -R docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* source/javax/mail/*.html
%{_javadir}/*.jar
%dir %{_javadir}/javamail
%{_javadir}/javamail/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
