%define debug_package %{nil}

Name:          paella-opencast
Summary:       Paella Player for Opencast
Version:       5.2.1
Release:       1%{?dist}
License:       GPLv3+

Source:        paella-engage-ui-%{version}.jar
URL:           https://github.com/polimediaupv/paella-matterhorn
BuildRoot:     %{_tmppath}/%{name}-root


%description
The Paella (pronounce “paeja”) Player is a HTML5 multistream video player
capable of playing multiple audio & video streams synchronously and supporting
a number of user plugins. It is specially designed for lecture recordings, like
Matterhorn Lectures or Polimedia pills.

By using Paella students can view both the lecture hall and the teacher's
screen, get info about the lecture (slides, OCR, series videos, footprints) and
interact with the lecture (views, comments). Teachers can also soft edit the
lecture to set the start and end point or make breaks in the recording.


%prep


%build


%install
rm -rf %{buildroot}
install -p -d -m 0755 %{buildroot}%{_datadir}/opencast/dist
install -p %{SOURCE0} %{buildroot}%{_datadir}/opencast/dist/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/opencast/dist/


%changelog
* Fri Jul 07 2017 Lars Kiesow <lkiesow@uos.de> - 5.2.1-1
- Initial Paella build
