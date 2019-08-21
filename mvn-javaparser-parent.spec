#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-javaparser-parent
Version  : 2.4.0
Release  : 2
URL      : https://github.com/javaparser/javaparser/archive/javaparser-parent-2.4.0.tar.gz
Source0  : https://github.com/javaparser/javaparser/archive/javaparser-parent-2.4.0.tar.gz
Source1  : https://repo.gradle.org/gradle/libs-releases/com/github/javaparser/javaparser-core/2.4.0/javaparser-core-2.4.0.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/com/github/javaparser/javaparser-core/2.4.0/javaparser-core-2.4.0.pom
Source3  : https://repo.gradle.org/gradle/libs-releases/com/github/javaparser/javaparser-parent/2.4.0/javaparser-parent-2.4.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 LGPL-3.0
Requires: mvn-javaparser-parent-data = %{version}-%{release}
Requires: mvn-javaparser-parent-license = %{version}-%{release}

%description
## Java Parser and Abstract Syntax Tree
This package contains a Java 1.8 Parser with AST generation and visitor support.

%package data
Summary: data components for the mvn-javaparser-parent package.
Group: Data

%description data
data components for the mvn-javaparser-parent package.


%package license
Summary: license components for the mvn-javaparser-parent package.
Group: Default

%description license
license components for the mvn-javaparser-parent package.


%prep
%setup -q -n javaparser-javaparser-parent-2.4.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-javaparser-parent
cp LICENSE.APACHE %{buildroot}/usr/share/package-licenses/mvn-javaparser-parent/LICENSE.APACHE
cp LICENSE.GPL %{buildroot}/usr/share/package-licenses/mvn-javaparser-parent/LICENSE.GPL
cp LICENSE.LGPL %{buildroot}/usr/share/package-licenses/mvn-javaparser-parent/LICENSE.LGPL
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/javaparser/javaparser-core/2.4.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/github/javaparser/javaparser-core/2.4.0/javaparser-core-2.4.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/javaparser/javaparser-core/2.4.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/github/javaparser/javaparser-core/2.4.0/javaparser-core-2.4.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/javaparser/javaparser-parent/2.4.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/github/javaparser/javaparser-parent/2.4.0/javaparser-parent-2.4.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/github/javaparser/javaparser-core/2.4.0/javaparser-core-2.4.0.jar
/usr/share/java/.m2/repository/com/github/javaparser/javaparser-core/2.4.0/javaparser-core-2.4.0.pom
/usr/share/java/.m2/repository/com/github/javaparser/javaparser-parent/2.4.0/javaparser-parent-2.4.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-javaparser-parent/LICENSE.APACHE
/usr/share/package-licenses/mvn-javaparser-parent/LICENSE.GPL
/usr/share/package-licenses/mvn-javaparser-parent/LICENSE.LGPL
